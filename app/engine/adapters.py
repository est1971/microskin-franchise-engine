from __future__ import annotations

import os
import time

import httpx

from app.core.contracts import BusinessRecord
from app.data.fixtures.demo_data import BUSINESS_FIXTURES, CITY_FIXTURES

GOOGLE_API_KEY = os.getenv("GOOGLE_PLACES_API_KEY", "")

PLACES_NEARBY_URL = "https://places.googleapis.com/v1/places:searchNearby"
PLACES_TEXT_URL   = "https://places.googleapis.com/v1/places:searchText"

FIELD_MASK = (
    "places.id,places.displayName,places.formattedAddress,"
    "places.location,places.rating,places.userRatingCount,"
    "places.websiteUri,places.types,places.businessStatus"
)

# ── Medical / aesthetic categories ────────────────────────────────────────────
# Use searchText (keyword-driven) for precision — avoids the catch-all "doctor"
# type that returns dentists, physios, astrologers, parking lots, etc.
# Multiple query strings per category; results are deduplicated by seen_ids.
TEXT_SEARCH_MAP: list[tuple[str, list[str]]] = [
    ("dermatologist", [
        "dermatology clinic",
        "skin specialist",
        "dermatologist",
        "skin doctor clinic",
    ]),
    ("aesthetic_clinic", [
        "aesthetic clinic",
        "cosmetic clinic",
        "skin care clinic",
        "facial aesthetic centre",
    ]),
    ("med_spa", [
        "medical spa",
        "medi spa",
        "medispa aesthetic",
    ]),
    ("hospital_dermatology_department", [
        "hospital dermatology department",
        "skin hospital",
        "dermatology hospital",
    ]),
]

# ── Venue categories ───────────────────────────────────────────────────────────
# searchNearby works well here — these map cleanly to Google place types.
NEARBY_SEARCH_MAP: list[tuple[str, list[str]]] = [
    ("pmu_artist",    ["beauty_salon"]),
    ("premium_salon", ["hair_salon", "beauty_salon"]),
]

# Google place types that flag a business as irrelevant for Microskin —
# applied as a post-filter after every search.
EXCLUDE_TYPES: set[str] = {
    "dentist", "dental_clinic", "orthodontist",
    "eye_care_clinic", "optometrist", "optician", "ophthalmologist",
    "physiotherapist", "physical_therapist",
    "parking", "parking_lot", "car_wash", "gas_station",
    "restaurant", "cafe", "food", "bar", "night_club",
    "real_estate_agency", "lodging", "hotel",
    "veterinary_care", "astrologer",
}


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
            # No API key — fall back to fixtures so the engine still runs
            return super().discover(city_id)

        city = next((c for c in CITY_FIXTURES if c["id"] == city_id), None)
        if not city:
            return []

        records: list[BusinessRecord] = []
        seen_ids: set[str] = set()

        for core in city["cores"]:
            center_lat, center_lng = core["center"]

            # ── searchText: medical / aesthetic categories ─────────────────
            for internal_category, queries in TEXT_SEARCH_MAP:
                for query in queries:
                    try:
                        batch = self._text_search(
                            query=query,
                            lat=center_lat,
                            lng=center_lng,
                            radius_m=5000,
                            city_id=city_id,
                            country_code=city["country_code"],
                            internal_category=internal_category,
                        )
                        for record in batch:
                            if record.record_id not in seen_ids:
                                seen_ids.add(record.record_id)
                                records.append(record)
                        time.sleep(0.08)
                    except Exception as exc:  # noqa: BLE001
                        print(
                            f"[GooglePlaces:text] {city_id}/{internal_category}"
                            f" '{query}' failed: {exc}"
                        )

            # ── searchNearby: venue categories ─────────────────────────────
            for internal_category, google_types in NEARBY_SEARCH_MAP:
                try:
                    batch = self._nearby_search(
                        lat=center_lat,
                        lng=center_lng,
                        radius_m=5000,
                        included_types=google_types,
                        city_id=city_id,
                        country_code=city["country_code"],
                        internal_category=internal_category,
                    )
                    for record in batch:
                        if record.record_id not in seen_ids:
                            seen_ids.add(record.record_id)
                            records.append(record)
                    time.sleep(0.08)
                except Exception as exc:  # noqa: BLE001
                    print(
                        f"[GooglePlaces:nearby] {city_id}/{internal_category} failed: {exc}"
                    )

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

        resp = httpx.post(
            PLACES_TEXT_URL, json=payload, headers=headers, timeout=15
        )
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

        resp = httpx.post(
            PLACES_NEARBY_URL, json=payload, headers=headers, timeout=15
        )
        resp.raise_for_status()

        return [
            self._to_record(place, city_id, country_code, internal_category)
            for place in resp.json().get("places", [])
            if self._is_relevant(place)
        ]

    # ── helpers ────────────────────────────────────────────────────────────────
    @staticmethod
    def _is_relevant(place: dict) -> bool:
        """Return False if Google's type list contains an excluded category."""
        place_types = set(place.get("types", []))
        return not (place_types & EXCLUDE_TYPES)

    @staticmethod
    def _to_record(
        place: dict,
        city_id: str,
        country_code: str,
        internal_category: str,
    ) -> BusinessRecord:
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
    """Overture Maps open-data integration — planned Phase 2."""
    provider_name = "overture"


class MapboxSearchAdapter(ProviderAdapter):
    """Mapbox Search integration — planned Phase 2."""
    provider_name = "mapbox_search"


def adapter_stack() -> list[ProviderAdapter]:
    return [GooglePlacesAdapter(), OvertureAdapter(), MapboxSearchAdapter()]
