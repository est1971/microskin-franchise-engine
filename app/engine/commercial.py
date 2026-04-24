from __future__ import annotations

"""
Territory valuation engine.

Value is driven by what is actually inside the territory:
  - Count and category of viable businesses
  - Quality of those businesses (rating, reviews, website presence)
  - Revenue a franchisee can realistically earn

GDP per capita is used only as a floor signal — it can raise a minimum
franchise fee slightly but cannot reduce a high-opportunity territory's value.
Maximum GDP influence is capped at 12% of the final fee.

Market maturity adjusts for how developed the aesthetic treatment industry
is in each country — again a soft modifier, not a ceiling.
"""

from app.core.config import config
from app.core.contracts import ClusterResult, CommercialScenario


# GDP per capita approximate 2024 USD — used ONLY as minimum floor.
# Source: World Bank / IMF estimates.  Does not drive primary valuation.
_GDP_PER_CAPITA: dict[str, float] = {
    "AU": 65_000, "GB": 46_000, "US": 80_000, "CA": 55_000,
    "DE": 51_000, "FR": 43_000, "SE": 57_000, "NO": 90_000,
    "DK": 67_000, "FI": 50_000, "NL": 57_000, "CH": 98_000,
    "ES": 33_000, "PT": 24_000, "IT": 36_000, "PL": 19_000,
    "EE": 27_000, "SG": 65_000, "JP": 34_000, "KR": 33_000,
    "TH": 7_000,  "MY": 12_000, "IN": 2_500,  "BR": 9_000,
    "MX": 11_000, "JO": 4_000,  "ZA": 6_000,  "AE": 44_000,
}
_GDP_FLOOR_WEIGHT = 0.12   # GDP can influence at most 12% of final fee
_GDP_FLOOR_DIVISOR = 8     # gdp_per_capita / 8 = approx minimum annual investment capacity


def _territory_tier(opportunity_score: float) -> str:
    for tier, threshold in config.territory_tiers.items():
        if opportunity_score >= threshold:
            return tier
    return "Standard"


def _market_maturity(profile: dict) -> str:
    return profile.get("market_defaults", {}).get("market_maturity", "developing")


def project_territory(
    cluster: ClusterResult,
    validation: dict,
    profile: dict | None = None,
) -> list[CommercialScenario]:
    """
    Project revenue scenarios for a territory.
    Uses the country's local currency and financial profile if provided.
    Falls back to GBP-equivalent constants if not.
    """
    md = (profile or {}).get("market_defaults", {})

    # Local financial parameters
    product_price     = md.get("product_price_local", 900.0)
    consult_fee       = md.get("consultation_fee_default", 150.0)
    product_margin    = md.get("product_margin", 0.63)
    royalty_rate      = md.get("royalty_rate", 0.08)
    marketing_rate    = md.get("marketing_contribution_rate", 0.03)
    platform_rate     = md.get("platform_fee_rate", 0.02)
    operating_costs   = md.get("annual_operating_costs_local", 50_000.0)
    market_maturity   = _market_maturity(profile or {})
    country_code      = (profile or {}).get("code", "GB")

    # Opportunity score drives tier and payback target
    opp_score   = cluster.opportunity_score
    tier        = _territory_tier(opp_score)
    payback_yrs = config.tier_payback_years[tier]
    maturity_mult = config.market_maturity_multipliers.get(market_maturity, 0.88)

    # Base consult capacity from viable business count
    viable       = cluster.viable_business_count
    active_rota  = round(viable * 0.45)
    base_consults_per_day = max(2.5, min(4.5, active_rota / 12))

    scenarios: list[CommercialScenario] = []

    for name, multiplier in config.scenario_multipliers.items():
        clinic_days = 18 if name == "expected" else (16 if name == "conservative" else 20)
        consults_per_day    = round(base_consults_per_day * multiplier, 1)
        monthly_consults    = round(clinic_days * consults_per_day, 1)

        annual_product_rev  = round(monthly_consults * 12 * product_price * multiplier, 2)
        annual_consult_rev  = round(monthly_consults * 12 * consult_fee * multiplier, 2)
        gross_profit        = round((annual_product_rev * product_margin) + annual_consult_rev, 2)
        royalties           = round(annual_product_rev * royalty_rate, 2)
        marketing           = round(annual_product_rev * marketing_rate, 2)
        platform_fee        = round(annual_product_rev * platform_rate, 2)
        net_income          = round(gross_profit - royalties - marketing - platform_fee - operating_costs, 2)

        # Franchise fee: net income × payback years × maturity multiplier
        base_fee = net_income * payback_yrs * maturity_mult

        # GDP floor: a gentle minimum, capped at 12% influence
        gdp     = _GDP_PER_CAPITA.get(country_code, 10_000)
        gdp_min = gdp / _GDP_FLOOR_DIVISOR  # approx minimum annual investment capacity
        # Only raise the fee if base_fee is below the floor — never lowers it
        fee_with_floor = max(base_fee, base_fee * (1 - _GDP_FLOOR_WEIGHT) + gdp_min * _GDP_FLOOR_WEIGHT)

        fee_low  = round(max(15_000, fee_with_floor * 0.82), 2)
        fee_high = round(max(25_000, fee_with_floor * 1.18), 2)

        scenarios.append(CommercialScenario(
            name=name,
            monthly_clinic_days=clinic_days,
            consults_per_day=consults_per_day,
            monthly_consults=monthly_consults,
            annual_product_revenue=annual_product_rev,
            annual_consultation_revenue=annual_consult_rev,
            gross_profit=gross_profit,
            royalties=royalties,
            marketing_contribution=marketing,
            platform_fee=platform_fee,
            net_franchisee_income=net_income,
            recommended_franchise_price_low=fee_low,
            recommended_franchise_price_high=fee_high,
        ))

    return scenarios


def territory_tier_for_cluster(cluster: ClusterResult) -> str:
    return _territory_tier(cluster.opportunity_score)
