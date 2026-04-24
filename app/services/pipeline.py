from __future__ import annotations

from dataclasses import dataclass

from app.core.contracts import BusinessRecord
from app.data.fixtures.demo_data import CITY_FIXTURES
from app.data.business_store import has_city_data, load_city_businesses, save_city_businesses
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

    # ── Business discovery with DB cache ──────────────────────────────────────
    # Google Places is called exactly once per city — ever.  After that,
    # records are loaded from SQLite instantly.  The grid search covers the
    # entire metro; no hardcoded cores, no demographic assumptions.
    raw_records: list[BusinessRecord] = []
    if has_city_data(city_id):
        raw_records = load_city_businesses(city_id)
    else:
        for adapter in adapter_stack():
            raw_records.extend(adapter.discover(city_id))
        save_city_businesses(city_id, raw_records)

    canonical_businesses = score_businesses(reconcile_businesses(raw_records))
    businesses_by_id = {b.canonical_id: b for b in canonical_businesses}

    # ── Data-driven clustering ────────────────────────────────────────────────
    # DBSCAN finds natural density clusters across the full metro.
    # Each cluster → one territory.  No manual core input.
    clusters = detect_clusters(city_id, canonical_businesses)

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
    """Run pipelines for cities flagged run_on_startup=True (none by default)."""
    active = [city for city in CITY_FIXTURES if city.get("run_on_startup", False)]
    return {city["id"]: run_city_pipeline(city["id"]) for city in active}


def global_summary() -> dict:
    all_results = run_all_pipelines()
    city_analyses = all_city_analyses()
    territories = [t for result in all_results.values() for t in result.territories]
    return {
        "countries": sorted({result.city["country_code"] for result in all_results.values()}),
        "cities": len(all_results),
        "territories": len(territories),
        "contract_ready": len([t for t in territories if t.validation_status.startswith("valid")]),
        "population_logic_warning_count": len([a for a in city_analyses if a["population_only_is_flawed"]]),
    }
