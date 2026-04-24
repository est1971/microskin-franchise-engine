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

# Maps our internal category → Google Places included types
CATEGORY_TYPE_MAP: list[tuple[str, list[str]]] = [
    ("dermatologist",                    ["doctor"]),
    ("aesthetic_clinic",                 ["beauty_salon", "skin_care"]),
    ("med_spa",                          ["spa"]),
    ("hospital_dermatology_department",  ["hospital"]),
    ("pmu_artist",                       ["beauty_salon"]),
    ("premium_salon",                    ["hair_salon", "beauty_salon"]),
]


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

            for internal_category, google_types in CATEGORY_TYPE_MAP:
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

                    time.sleep(0.08)  # ~12 req/s — well within quota

                except Exception as exc:  # noqa: BLE001
                    print(
                        f"[GooglePlaces] {city_id}/{internal_category} failed: {exc}"
                    )

        return records

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
        ]

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
