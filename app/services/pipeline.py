from __future__ import annotations

from dataclasses import dataclass

from app.core.contracts import BusinessRecord
from app.data.fixtures.demo_data import CITY_FIXTURES
from app.engine.adapters import adapter_stack
from app.engine.city_discovery import analyze_city_market, all_city_analyses
from app.engine.country_profiles import load_country_profiles
from app.engine.clustering import detect_clusters
from app.engine.reconciliation import reconcile_businesses
from app.engine.scoring import score_businesses
from app.engine.territories import generate_territories


@dataclass(slots=True)
class CityPipelineResult:
    city: dict
    city_analysis: dict
    businesses: list
    clusters: list
    territories: list


def run_city_pipeline(city_id: str) -> CityPipelineResult:
    city = next(city for city in CITY_FIXTURES if city["id"] == city_id)
    profiles = load_country_profiles()
    profile = profiles[city["country_code"]]
    raw_records: list[BusinessRecord] = []
    for adapter in adapter_stack():
        raw_records.extend(adapter.discover(city_id))
    canonical_businesses = score_businesses(reconcile_businesses(raw_records))
    businesses_by_id = {business.canonical_id: business for business in canonical_businesses}
    clusters = []
    for core in city["cores"]:
        clusters.extend(detect_clusters(city_id, core["id"], canonical_businesses, tuple(core["center"])))
    territories = generate_territories(
        {**city, "country_code": city["country_code"]},
        clusters,
        businesses_by_id,
        profile.model_dump(),
    )
    return CityPipelineResult(
        city=city,
        city_analysis=analyze_city_market(city),
        businesses=canonical_businesses,
        clusters=clusters,
        territories=territories,
    )


def run_all_pipelines() -> dict[str, CityPipelineResult]:
    return {city["id"]: run_city_pipeline(city["id"]) for city in CITY_FIXTURES}


def global_summary() -> dict:
    all_results = run_all_pipelines()
    city_analyses = all_city_analyses()
    territories = [territory for result in all_results.values() for territory in result.territories]
    return {
        "countries": sorted({result.city["country_code"] for result in all_results.values()}),
        "cities": len(all_results),
        "territories": len(territories),
        "contract_ready": len([item for item in territories if item.validation_status.startswith("valid")]),
        "population_logic_warning_count": len([item for item in city_analyses if item["population_only_is_flawed"]]),
    }

