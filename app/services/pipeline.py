from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass

from app.core.contracts import BusinessRecord, CanonicalBusiness
from app.core.utils import haversine_km
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


def _nearest_core_id(business: CanonicalBusiness, cores: list[dict]) -> str:
    """Return the id of whichever core centre is geographically closest."""
    return min(
        cores,
        key=lambda c: haversine_km(
            business.latitude, business.longitude,
            c["center"][0], c["center"][1],
        ),
    )["id"]


def run_city_pipeline(city_id: str) -> CityPipelineResult:
    city = next(city for city in CITY_FIXTURES if city["id"] == city_id)
    profiles = load_country_profiles()
    profile = profiles[city["country_code"]]
    # ── Business discovery with DB cache ──────────────────────────────────────
    # Google Places is called exactly once per city.  On every subsequent run
    # (including server restarts) the records are loaded from SQLite instead.
    raw_records: list[BusinessRecord] = []
    if has_city_data(city_id):
        raw_records = load_city_businesses(city_id)
    else:
        for adapter in adapter_stack():
            raw_records.extend(adapter.discover(city_id))
        save_city_businesses(city_id, raw_records)
    canonical_businesses = score_businesses(reconcile_businesses(raw_records))
    businesses_by_id = {business.canonical_id: business for business in canonical_businesses}

    # ── Voronoi-style core assignment ─────────────────────────────────────────
    # Each business is assigned exclusively to its nearest core.  This prevents
    # the same business appearing in clusters for two adjacent cores (which was
    # producing overlapping territories).
    core_businesses: dict[str, list[CanonicalBusiness]] = defaultdict(list)
    for business in canonical_businesses:
        core_businesses[_nearest_core_id(business, city["cores"])].append(business)

    clusters = []
    for core in city["cores"]:
        assigned = core_businesses.get(core["id"], [])
        if assigned:
            clusters.extend(
                detect_clusters(city_id, core["id"], assigned, tuple(core["center"]))
            )

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
    """Run pipelines for cities flagged run_on_startup=True.

    Cities with run_on_startup=False load lazily via city_detail() on first
    request.  This keeps cold-start time predictable regardless of how many
    cities are in the fixture list.
    """
    active = [city for city in CITY_FIXTURES if city.get("run_on_startup", True)]
    return {city["id"]: run_city_pipeline(city["id"]) for city in active}


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

