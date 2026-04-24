from __future__ import annotations

from app.data.fixtures.demo_data import BUSINESS_FIXTURES, CITY_FIXTURES


def analyze_city_market(city: dict) -> dict:
    """
    Fixture-level analysis — runs from static data before any Google Places
    call is made.  Used to populate the country analysis panel instantly
    on page load.  Once a city is fully discovered, the live pipeline results
    supersede these estimates.
    """
    businesses       = [item for item in BUSINESS_FIXTURES if item["city_id"] == city["id"]]
    business_density = len(businesses) / max(city["population_context"] / 1_000_000, 1)
    premium_ratio    = sum(1 for item in businesses if item.get("premium_corridor")) / max(len(businesses), 1)
    high_quality_ratio = sum(1 for item in businesses if item.get("rating", 0) >= 4.5) / max(len(businesses), 1)
    opportunity_score  = round((business_density * 0.25) + (premium_ratio * 4.0) + (high_quality_ratio * 3.0), 2)
    maturity_bonus     = {"viable_now": 2.2, "developing_market": 1.2}.get(city.get("maturity", ""), 0.4)

    # search_radius_km as a proxy for metro coverage potential (replaces old cores count)
    radius_km = city.get("search_radius_km", 20)
    coverage_score = round(radius_km / 20, 2)   # normalised; 20km → 1.0

    score = round(opportunity_score + maturity_bonus + coverage_score, 2)

    if score >= 8:
        classification = "viable now"
    elif score >= 6:
        classification = "outlet-constrained"
    elif score >= 4:
        classification = "developing market"
    else:
        classification = "not yet viable"

    # suggested_economic_cores is now an estimate based on metro radius —
    # the real number comes from DBSCAN after discovery.
    estimated_cores = max(1, round(radius_km / 8))

    return {
        "city_id":                     city["id"],
        "city_name":                   city["name"],
        "classification":              classification,
        "launch_phase_recommendation": city.get("launch_phase", "TBC"),
        "city_score":                  score,
        "suggested_economic_cores":    estimated_cores,
        "business_density_proxy":      round(business_density, 2),
        "premium_demand_proxy":        round(premium_ratio, 2),
        "maturity_score":              maturity_bonus,
        "population_rank":             city.get("population_rank", 0),
        "population_only_is_flawed":   score > 6 and business_density > 0.35,
    }


def all_city_analyses() -> list[dict]:
    return [analyze_city_market(city) for city in CITY_FIXTURES]
