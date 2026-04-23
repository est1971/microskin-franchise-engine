from __future__ import annotations

from app.core.contracts import BusinessRecord
from app.data.fixtures.demo_data import BUSINESS_FIXTURES


class ProviderAdapter:
    provider_name = "base"

    def discover(self, city_id: str) -> list[BusinessRecord]:
        return [BusinessRecord(**item) for item in BUSINESS_FIXTURES if item["city_id"] == city_id and item["source"] == self.provider_name]


class GooglePlacesAdapter(ProviderAdapter):
    provider_name = "google_places"


class OvertureAdapter(ProviderAdapter):
    provider_name = "overture"


class MapboxSearchAdapter(ProviderAdapter):
    provider_name = "mapbox_search"


def adapter_stack() -> list[ProviderAdapter]:
    return [GooglePlacesAdapter(), OvertureAdapter(), MapboxSearchAdapter()]

