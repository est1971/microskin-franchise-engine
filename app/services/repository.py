from __future__ import annotations

from functools import lru_cache

from app.data.fixtures.demo_data import CITY_FIXTURES, COUNTRY_FIXTURES
from app.engine.city_discovery import all_city_analyses
from app.services.pipeline import run_all_pipelines, run_city_pipeline

# ── In-memory cache for lazy-loaded city results ──────────────────────────────
# Startup results come from cached_results().
# Cities loaded on-demand are stored here so they survive across requests
# without re-running the pipeline.  On Railway with a persistent volume,
# the business data is also in SQLite so restarts are fast.
_lazy_cache: dict = {}


@lru_cache(maxsize=1)
def cached_results() -> dict:
    return run_all_pipelines()


def refresh_results() -> dict:
    cached_results.cache_clear()
    _lazy_cache.clear()
    return cached_results()


def _all_results() -> dict:
    """Merge startup results and lazy-loaded results."""
    return {**cached_results(), **_lazy_cache}


def get_summary() -> dict:
    results = _all_results()
    city_analyses = all_city_analyses()
    territories = [t for r in results.values() for t in r.territories]
    return {
        "countries": sorted({city["country_code"] for city in CITY_FIXTURES}),
        "cities_total": len(CITY_FIXTURES),
        "cities_loaded": len(results),
        "territories": len(territories),
        "contract_ready": len([t for t in territories if t.validation_status.startswith("valid")]),
        "population_logic_warning_count": len([a for a in city_analyses if a["population_only_is_flawed"]]),
    }


def list_countries() -> list[dict]:
    results = _all_results()
    output = []
    for country in COUNTRY_FIXTURES:
        cities = [city for city in CITY_FIXTURES if city["country_code"] == country["code"]]
        country_territories = [
            territory
            for result in results.values()
            for territory in result.territories
            if territory.country_code == country["code"]
        ]
        md = country["profile"].get("market_defaults", {})
        output.append({
            "code": country["code"],
            "name": country["name"],
            "region": country["region"],
            "supported": True,
            "cities": len(cities),
            "territories": len(country_territories),
            "contract_ready": len([t for t in country_territories if t.validation_status.startswith("valid")]),
            "currency_code": md.get("currency_code", "USD"),
            "currency_symbol": md.get("currency_symbol", "$"),
            "gbp_rate": md.get("gbp_rate", 1.27),
            "product_price_local": md.get("product_price_local", 115.0),
            "consultation_fee_default": md.get("consultation_fee_default", 150.0),
            "royalty_rate": md.get("royalty_rate", 0.06),
            "marketing_contribution_rate": md.get("marketing_contribution_rate", 0.01),
            "connect_fee_monthly_local": md.get("connect_fee_monthly_local", 120.0),
        })
    return output


def country_detail(country_code: str) -> dict:
    country = next(item for item in COUNTRY_FIXTURES if item["code"] == country_code)
    results = _all_results()
    city_details = []
    for city in [item for item in CITY_FIXTURES if item["country_code"] == country_code]:
        result = results.get(city["id"])
        if result:
            city_details.append({
                "city": city,
                "loaded": True,
                "analysis": result.city_analysis,
                "territories": [t.model_dump(mode="json") for t in result.territories],
                "clusters": [c.model_dump(mode="json") for c in result.clusters],
            })
        else:
            city_details.append({
                "city": city,
                "loaded": False,
                "analysis": None,
                "territories": [],
                "clusters": [],
            })
    return {"country": country, "cities": city_details}


def city_detail(city_id: str) -> dict:
    # Check both caches first — avoid re-running the pipeline if we have results
    result = _all_results().get(city_id)
    if result is None:
        result = run_city_pipeline(city_id)
        _lazy_cache[city_id] = result   # store so subsequent requests are instant
    return {
        "city": result.city,
        "analysis": result.city_analysis,
        "businesses": [b.model_dump(mode="json") for b in result.businesses],
        "clusters": [c.model_dump(mode="json") for c in result.clusters],
        "territories": [t.model_dump(mode="json") for t in result.territories],
    }


def territory_detail(territory_id: str):
    # Search all results including lazy-loaded ones
    for result in _all_results().values():
        for territory in result.territories:
            if territory.territory_id == territory_id:
                return territory
    raise KeyError(territory_id)
