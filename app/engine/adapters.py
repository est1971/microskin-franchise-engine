from __future__ import annotations

import math
import os
import time

import httpx

from app.core.contracts import BusinessRecord
from app.core.utils import haversine_km
from app.data.fixtures.demo_data import BUSINESS_FIXTURES, CITY_FIXTURES

GOOGLE_API_KEY = os.getenv("GOOGLE_PLACES_API_KEY", "")

PLACES_NEARBY_URL = "https://places.googleapis.com/v1/places:searchNearby"
PLACES_TEXT_URL   = "https://places.googleapis.com/v1/places:searchText"

FIELD_MASK = (
    "places.id,places.displayName,places.formattedAddress,"
    "places.location,places.rating,places.userRatingCount,"
    "places.websiteUri,places.types,places.businessStatus"
)

# ── Search categories ─────────────────────────────────────────────────────────
# Text search: keyword-driven, catches the full range of Microskin-relevant
# business types.  No demographic filtering — we search the entire metro.
TEXT_SEARCH_MAP: list[tuple[str, list[str]]] = [
    ("hospital", [
        "private hospital",
        "medical centre",
        "health clinic hospital",
    ]),
    ("dermatologist", [
        "dermatologist",
        "dermatology clinic",
        "skin specialist",
    ]),
    ("aesthetic_clinic", [
        "aesthetic clinic",
        "cosmetic clinic",
        "skin care clinic",
    ]),
    ("plastic_surgery", [
        "plastic surgeon",
        "cosmetic surgery clinic",
    ]),
    ("med_spa", [
        "medical spa",
        "medi spa",
        "skin rejuvenation clinic",
    ]),
    ("general_practice", [
        "GP clinic",
        "family medical practice",
    ]),
]

# Nearby search: maps to Google place types cleanly
NEARBY_SEARCH_MAP: list[tuple[str, list[str]]] = [
    ("beauty_spa",     ["spa", "beauty_salon"]),
    ("premium_salon",  ["hair_salon"]),
]

# Post-filter: remove clearly irrelevant businesses returned by Google
EXCLUDE_TYPES: set[str] = {
    "dentist", "dental_clinic", "orthodontist",
    "eye_care_clinic", "optometrist", "optician", "ophthalmologist",
    "physiotherapist", "physical_therapist",
    "parking", "parking_lot", "car_wash", "gas_station",
    "restaurant", "cafe", "food", "bar", "night_club",
    "real_estate_agency", "lodging", "hotel",
    "veterinary_care", "astrologer",
}

# ── Grid spacing and search radius per grid point ─────────────────────────────
# Grid points are spaced GRID_SPACING_KM apart.  Each point searches
# SEARCH_RADIUS_M around itself.  Overlap ensures no gaps between cells.
GRID_SPACING_KM  = 5.0
SEARCH_RADIUS_M  = 5000      # 5 km per grid point — overlaps adjacent cells


def _metro_grid(center_lat: float, center_lng: float, metro_radius_km: float) -> list[tuple[float, float]]:
    """
    Generate a lat/lng grid covering the full metro area.
    Returns points within metro_radius_km of the city centre.
    Grid is spaced GRID_SPACING_KM apart, giving overlapping 5 km search circles.
    """
    lat_step  = GRID_SPACING_KM / 111.0
    lng_step  = GRID_SPACING_KM / (111.0 * max(math.cos(math.radians(center_lat)), 0.01))

    lat_extent = metro_radius_km / 111.0
    lng_extent = metro_radius_km / (111.0 * max(math.cos(math.radians(center_lat)), 0.01))

    points: list[tuple[float, float]] = []
    lat = center_lat - lat_extent
    while lat <= center_lat + lat_extent + lat_step * 0.5:
        lng = center_lng - lng_extent
        while lng <= center_lng + lng_extent + lng_step * 0.5:
            if haversine_km(center_lat, center_lng, lat, lng) <= metro_radius_km:
                points.append((round(lat, 6), round(lng, 6)))
            lng += lng_step
        lat += lat_step
    return points


def _search_radius_km(city: dict) -> float:
    """Derive metro search radius from population context if not explicitly set."""
    if "search_radius_km" in city:
        return float(city["search_radius_km"])
    pop = city.get("population_context", 500_000)
    if pop >= 8_000_000:
        return 40.0
    if pop >= 5_000_000:
        return 35.0
    if pop >= 2_000_000:
        return 28.0
    if pop >= 1_000_000:
        return 22.0
    if pop >= 500_000:
        return 16.0
    return 12.0


class ProviderAdapter:
    provider_name = "base"

    def discover(self, city_id: str) -> list[BusinessRecord]:
        return [
            BusinessRecord(**item)
            for item in BUSINESS_FIXTURES
            if item["city_id"] == city_id and item["source"] == self.provider_name
        ]


class GooglePlacesAdapter(ProviderAdapter):
    provider_name = "google_places"

    def discover(self, city_id: str) -> list[BusinessRecord]:
        if not GOOGLE_API_KEY:
            # No key — fall back to fixtures so the engine still runs in dev
            return super().discover(city_id)

        city = next((c for c in CITY_FIXTURES if c["id"] == city_id), None)
        if not city:
            return []

        center_lat, center_lng = city["center"]
        radius_km = _search_radius_km(city)
        grid_points = _metro_grid(center_lat, center_lng, radius_km)

        records: list[BusinessRecord] = []
        seen_ids: set[str] = set()

        total_points = len(grid_points)
        print(f"[GooglePlaces] {city_id}: {total_points} grid points × {radius_km} km radius")

        for idx, (pt_lat, pt_lng) in enumerate(grid_points):
            # ── Text search: medical/aesthetic categories ──────────────────
            for internal_category, queries in TEXT_SEARCH_MAP:
                for query in queries:
                    try:
                        batch = self._text_search(
                            query=query,
                            lat=pt_lat,
                            lng=pt_lng,
                            radius_m=SEARCH_RADIUS_M,
                            city_id=city_id,
                            country_code=city["country_code"],
                            internal_category=internal_category,
                        )
                        for record in batch:
                            if record.record_id not in seen_ids:
                                seen_ids.add(record.record_id)
                                records.append(record)
                        time.sleep(0.06)
                    except Exception as exc:  # noqa: BLE001
                        print(f"[GooglePlaces:text] {city_id}/{internal_category} '{query}' @ pt{idx} failed: {exc}")

            # ── Nearby search: beauty/salon categories ─────────────────────
            for internal_category, google_types in NEARBY_SEARCH_MAP:
                try:
                    batch = self._nearby_search(
                        lat=pt_lat,
                        lng=pt_lng,
                        radius_m=SEARCH_RADIUS_M,
                        included_types=google_types,
                        city_id=city_id,
                        country_code=city["country_code"],
                        internal_category=internal_category,
                    )
                    for record in batch:
                        if record.record_id not in seen_ids:
                            seen_ids.add(record.record_id)
                            records.append(record)
                    time.sleep(0.06)
                except Exception as exc:  # noqa: BLE001
                    print(f"[GooglePlaces:nearby] {city_id}/{internal_category} @ pt{idx} failed: {exc}")

        print(f"[GooglePlaces] {city_id}: discovered {len(records)} unique businesses")
        return records

    # ── searchText ─────────────────────────────────────────────────────────────
    def _text_search(
        self,
        query: str,
        lat: float,
        lng: float,
        radius_m: float,
        city_id: str,
        country_code: str,
        internal_category: str,
    ) -> list[BusinessRecord]:
        headers = {
            "X-Goog-Api-Key": GOOGLE_API_KEY,
            "Content-Type": "application/json",
            "X-Goog-FieldMask": FIELD_MASK,
        }
        payload = {
            "textQuery": query,
            "locationRestriction": {
                "circle": {
                    "center": {"latitude": lat, "longitude": lng},
                    "radius": float(radius_m),
                }
            },
            "maxResultCount": 20,
        }
        resp = httpx.post(PLACES_TEXT_URL, json=payload, headers=headers, timeout=15)
        resp.raise_for_status()
        return [
            self._to_record(place, city_id, country_code, internal_category)
            for place in resp.json().get("places", [])
            if self._is_relevant(place)
        ]

    # ── searchNearby ───────────────────────────────────────────────────────────
    def _nearby_search(
        self,
        lat: float,
        lng: float,
        radius_m: float,
        included_types: list[str],
        city_id: str,
        country_code: str,
        internal_category: str,
    ) -> list[BusinessRecord]:
        headers = {
            "X-Goog-Api-Key": GOOGLE_API_KEY,
            "Content-Type": "application/json",
            "X-Goog-FieldMask": FIELD_MASK,
        }
        payload = {
            "locationRestriction": {
                "circle": {
                    "center": {"latitude": lat, "longitude": lng},
                    "radius": float(radius_m),
                }
            },
            "includedTypes": included_types,
            "maxResultCount": 20,
            "rankPreference": "DISTANCE",
        }
        resp = httpx.post(PLACES_NEARBY_URL, json=payload, headers=headers, timeout=15)
        resp.raise_for_status()
        return [
            self._to_record(place, city_id, country_code, internal_category)
            for place in resp.json().get("places", [])
            if self._is_relevant(place)
        ]

    @staticmethod
    def _is_relevant(place: dict) -> bool:
        return not (set(place.get("types", [])) & EXCLUDE_TYPES)

    @staticmethod
    def _to_record(place: dict, city_id: str, country_code: str, internal_category: str) -> BusinessRecord:
        loc = place.get("location", {})
        return BusinessRecord(
            record_id=f"gp_{place['id']}",
            source="google_places",
            source_confidence=0.92,
            city_id=city_id,
            country_code=country_code,
            name=place.get("displayName", {}).get("text", "Unknown"),
            address=place.get("formattedAddress", ""),
            region="",
            city=city_id,
            latitude=float(loc.get("latitude", 0.0)),
            longitude=float(loc.get("longitude", 0.0)),
            category_hint=internal_category,
            rating=float(place.get("rating", 0.0)),
            review_count=int(place.get("userRatingCount", 0)),
            website_present=bool(place.get("websiteUri")),
            premium_corridor=False,
            completeness=0.85,
            stale=False,
            metadata={"google_types": place.get("types", [])},
        )


class OvertureAdapter(ProviderAdapter):
    """Overture Maps open-data — planned Phase 2."""
    provider_name = "overture"


class MapboxSearchAdapter(ProviderAdapter):
    """Mapbox Search — planned Phase 2."""
    provider_name = "mapbox_search"


def adapter_stack() -> list[ProviderAdapter]:
    return [GooglePlacesAdapter(), OvertureAdapter(), MapboxSearchAdapter()]
