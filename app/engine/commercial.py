from __future__ import annotations

from app.core.config import config
from app.core.contracts import ClusterResult, CommercialScenario


def project_territory(cluster: ClusterResult, validation: dict) -> list[CommercialScenario]:
    scenarios: list[CommercialScenario] = []
    weighted_businesses = cluster.weighted_business_count * 10.5
    base_consults_per_day = max(3.0, min(4.2, weighted_businesses / 30))

    for name, multiplier in config.scenario_multipliers.items():
        clinic_days = 18 if name == "expected" else (16 if name == "conservative" else 20)
        consults_per_day = round(base_consults_per_day * multiplier, 1)
        monthly_consults = round(clinic_days * consults_per_day, 1)
        annual_product_revenue = round(monthly_consults * 12 * 900 * multiplier, 2)
        annual_consultation_revenue = round(monthly_consults * 12 * 180 * multiplier, 2)
        gross_profit = round((annual_product_revenue * 0.63) + annual_consultation_revenue, 2)
        royalties = round(annual_product_revenue * 0.08, 2)
        marketing = round(annual_product_revenue * 0.03, 2)
        platform_fee = round(annual_product_revenue * 0.02, 2)
        net_income = round(gross_profit - royalties - marketing - platform_fee - 86000, 2)
        scenarios.append(
            CommercialScenario(
                name=name,
                monthly_clinic_days=clinic_days,
                consults_per_day=consults_per_day,
                monthly_consults=monthly_consults,
                annual_product_revenue=annual_product_revenue,
                annual_consultation_revenue=annual_consultation_revenue,
                gross_profit=gross_profit,
                royalties=royalties,
                marketing_contribution=marketing,
                platform_fee=platform_fee,
                net_franchisee_income=net_income,
                recommended_franchise_price_low=round(max(35000, net_income * 0.28), 2),
                recommended_franchise_price_high=round(max(50000, net_income * 0.44), 2),
            )
        )
    return scenarios

