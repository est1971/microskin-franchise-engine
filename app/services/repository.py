from __future__ import annotations

from functools import lru_cache

from app.data.fixtures.demo_data import CITY_FIXTURES, COUNTRY_FIXTURES
from app.engine.city_discovery import all_city_analyses
from app.services.pipeline import run_all_pipelines, run_city_pipeline


@lru_cache(maxsize=1)
def cached_results() -> dict:
    return run_all_pipelines()


def refresh_results() -> dict:
    cached_results.cache_clear()
    return cached_results()


def get_summary() -> dict:
    """Return a summary that reflects all fixture cities, not just startup-loaded ones.

    Territory/contract counts come from cached (startup-loaded) cities.
    Total city count comes from CITY_FIXTURES so the summary shows the full
    scope of the network even before lazy cities have been loaded.
    """
    results = cached_results()
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
    results = cached_results()
    output = []
    for country in COUNTRY_FIXTURES:
        cities = [city for city in CITY_FIXTURES if city["country_code"] == country["code"]]
        country_territories = [territory for result in results.values() for territory in result.territories if territory.country_code == country["code"]]
        md = country["profile"].get("market_defaults", {})
        output.append(
            {
                "code": country["code"],
                "name": country["name"],
                "region": country["region"],
                "supported": True,
                "cities": len(cities),
                "territories": len(country_territories),
                "contract_ready": len([territory for territory in country_territories if territory.validation_status.startswith("valid")]),
                # Financial profile — used by the calculator in the frontend
                "currency_code": md.get("currency_code", "USD"),
                "currency_symbol": md.get("currency_symbol", "$"),
                "gbp_rate": md.get("gbp_rate", 1.27),
                "product_price_local": md.get("product_price_local", 115.0),
                "consultation_fee_default": md.get("consultation_fee_default", 150.0),
                "royalty_rate": md.get("royalty_rate", 0.06),
                "marketing_contribution_rate": md.get("marketing_contribution_rate", 0.01),
                "connect_fee_monthly_local": md.get("connect_fee_monthly_local", 120.0),
            }
        )
    return output


def country_detail(country_code: str) -> dict:
    country = next(item for item in COUNTRY_FIXTURES if item["code"] == country_code)
    results = cached_results()
    city_details = []
    for city in [item for item in CITY_FIXTURES if item["country_code"] == country_code]:
        # Use cached result if available; otherwise return fixture metadata only
        result = results.get(city["id"])
        if result:
            city_details.append(
                {
                    "city": city,
                    "loaded": True,
                    "analysis": result.city_analysis,
                    "territories": [territory.model_dump(mode="json") for territory in result.territories],
                    "clusters": [cluster.model_dump(mode="json") for cluster in result.clusters],
                }
            )
        else:
            city_details.append(
                {
                    "city": city,
                    "loaded": False,
                    "analysis": None,
                    "territories": [],
                    "clusters": [],
                }
            )
    return {"country": country, "cities": city_details}


def city_detail(city_id: str) -> dict:
    result = cached_results().get(city_id) or run_city_pipeline(city_id)
    return {
        "city": result.city,
        "analysis": result.city_analysis,
        "businesses": [business.model_dump(mode="json") for business in result.businesses],
        "clusters": [cluster.model_dump(mode="json") for cluster in result.clusters],
        "territories": [territory.model_dump(mode="json") for territory in result.territories],
    }


def territory_detail(territory_id: str):
    for result in cached_results().values():
        for territory in result.territories:
            if territory.territory_id == territory_id:
                return territory
    raise KeyError(territory_id)

