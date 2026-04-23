from __future__ import annotations

from app.core.config import config
from app.core.contracts import ClusterResult


def validate_territory(cluster: ClusterResult, opportunity_summary: dict) -> dict:
    viable_count = opportunity_summary["weighted_viable_count"]
    travel_efficiency = opportunity_summary["travel_efficiency"]
    dead_space_penalty = max(0, cluster.radius_km - 5) * 0.05
    viability_score = round(
        min(
            1.0,
            ((viable_count / config.operating_model["viable_opportunities_min"]) * 0.5)
            + (travel_efficiency * 0.25)
            + (cluster.confidence_score * 0.15)
            + (cluster.density_score * 0.1)
            - dead_space_penalty,
        ),
        2,
    )
    active_rotation = round(viable_count * 0.45)
    revisit_feasible = config.operating_model["active_clinic_rotation_min"] <= active_rotation <= config.operating_model["active_clinic_rotation_max"] + 12
    consult_capacity = round(min(config.operating_model["consultations_per_month_target"] * 1.2, active_rotation * 1.25))
    contractability_score = round(max(0.1, 0.9 - dead_space_penalty - (0.1 if cluster.radius_km > 7 else 0.0)), 2)

    if viability_score >= 0.78 and revisit_feasible and travel_efficiency >= 0.62:
        status = "valid"
    elif viability_score >= 0.67:
        status = "valid but review recommended"
    elif viable_count < 55:
        status = "weak / merge recommended"
    elif cluster.raw_business_count > 6 and cluster.radius_km < 2.5:
        status = "oversize / split recommended"
    else:
        status = "invalid"

    return {
        "status": status,
        "viability_score": viability_score,
        "contractability_score": contractability_score,
        "active_clinic_rotation": active_rotation,
        "revisit_feasible": revisit_feasible,
        "consult_capacity": consult_capacity,
    }

