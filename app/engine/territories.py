from __future__ import annotations

from shapely.geometry import MultiPoint, mapping

from app.core.contracts import ClusterResult, CommercialScenario, TerritoryResult
from app.core.utils import haversine_km, slugify
from app.engine.commercial import project_territory, territory_tier_for_cluster


# Buffer in degrees added around the convex hull of cluster business points.
# 0.018° ≈ 2 km at most latitudes — enough to fill gaps between points without
# bleeding into adjacent territories.
_POLYGON_BUFFER = 0.018


def _territory_polygon(points: list[tuple[float, float]]) -> dict:
    """Build a buffered convex hull polygon from a list of (lat, lng) points."""
    multipoint = MultiPoint([(lng, lat) for lat, lng in points])
    polygon = multipoint.convex_hull.buffer(_POLYGON_BUFFER)
    return mapping(polygon)


def _zone_label(centroid: tuple[float, float], city_center: tuple[float, float]) -> str:
    """
    Derive a compass-direction zone label relative to the city centre.
    e.g. 'North', 'South East', 'Central'.
    """
    dlat = centroid[0] - city_center[0]
    dlng = centroid[1] - city_center[1]
    dist = haversine_km(centroid[0], centroid[1], city_center[0], city_center[1])
    if dist < 3.0:
        return "Central"
    lat_label = "North" if dlat > 0 else "South"
    lng_label = "East"  if dlng > 0 else "West"
    # Use compound label only if both axes are significant
    if abs(dlat) > abs(dlng) * 1.8:
        return lat_label
    if abs(dlng) > abs(dlat) * 1.8:
        return lng_label
    return f"{lat_label} {lng_label}"


def generate_territories(
    city: dict,
    clusters: list[ClusterResult],
    businesses_by_id: dict,
    profile: dict,
) -> list[TerritoryResult]:
    city_center = tuple(city["center"])
    territories: list[TerritoryResult] = []

    # Sort clusters by opportunity score descending so Territory 01 is the best
    sorted_clusters = sorted(clusters, key=lambda c: c.opportunity_score, reverse=True)

    for index, cluster in enumerate(sorted_clusters, start=1):
        members = [businesses_by_id[bid] for bid in cluster.business_ids if bid in businesses_by_id]
        if not members:
            continue

        points = [(m.latitude, m.longitude) for m in members]
        polygon_geojson = _territory_polygon(points)

        tier  = territory_tier_for_cluster(cluster)
        zone  = _zone_label(cluster.centroid, city_center)

        # Territory name: "{City} / {Zone} Territory {n:02d}" — no hardcoded human choices
        territory_name = f"{city['name']} / {zone} Territory {index:02d}"

        opportunity_summary = {
            "raw_business_count":    cluster.raw_business_count,
            "weighted_viable_count": float(cluster.viable_business_count),
            "opportunity_score":     cluster.opportunity_score,
            "tier":                  tier,
            "category_mix":          cluster.category_mix,
            "density_score":         cluster.density_score,
            "travel_efficiency":     cluster.travel_efficiency,
        }

        validation = _validate(cluster, opportunity_summary)
        scenarios  = project_territory(cluster, validation, profile)

        territories.append(TerritoryResult(
            territory_id=f"territory-{slugify(cluster.cluster_id)}",
            territory_name=territory_name,
            version_id=f"v{index}.0",
            country_code=city["country_code"],
            state_region=city.get("region", ""),
            metro=city.get("metro", city["name"]),
            city=city["name"],
            core_id=cluster.core_id,
            polygon_geojson=polygon_geojson,
            coordinates=[[round(c[1], 6), round(c[0], 6)] for c in polygon_geojson["coordinates"][0]],
            postal_units=[
                f"{city['country_code']}-{cluster.core_id[-4:].upper()}-{index:02d}",
                f"{city['country_code']}-{cluster.core_id[-4:].upper()}-{index + 10:02d}",
            ],
            corridor_streets=[],   # no longer hardcoded — future: reverse geocode centroid
            written_boundary_description=_boundary_description(city, cluster, zone),
            viability_score=validation["viability_score"],
            opportunity_score=cluster.opportunity_score,
            tier=tier,
            opportunity_summary=opportunity_summary,
            validation_status=validation["status"],
            contractability_score=validation["contractability_score"],
            status="available" if validation["status"].startswith("valid") else "under_review",
            scenarios=scenarios,
        ))

    return territories


def _validate(cluster: ClusterResult, opportunity_summary: dict) -> dict:
    """Inline validation — kept here to avoid circular imports."""
    from app.core.config import config
    viable_count     = opportunity_summary["weighted_viable_count"]
    travel_eff       = opportunity_summary["travel_efficiency"]
    dead_space_pen   = max(0, cluster.radius_km - 8) * 0.03   # gentler penalty for large territories
    viability_score  = round(
        min(1.0,
            ((viable_count / max(config.operating_model["viable_opportunities_min"], 1)) * 0.5)
            + (travel_eff * 0.25)
            + (cluster.confidence_score * 0.15)
            + (cluster.density_score * 0.1)
            - dead_space_pen
        ), 2,
    )
    active_rotation = round(viable_count * 0.45)
    revisit_feasible = (
        config.operating_model["active_clinic_rotation_min"]
        <= active_rotation
        <= config.operating_model["active_clinic_rotation_max"] + 12
    )
    consult_capacity = round(min(
        config.operating_model["consultations_per_month_target"] * 1.2,
        active_rotation * 1.25,
    ))
    contractability = round(max(0.1, 0.9 - dead_space_pen), 2)

    if viability_score >= 0.78 and revisit_feasible and travel_eff >= 0.55:
        status = "valid"
    elif viability_score >= 0.60:
        status = "valid but review recommended"
    elif viable_count < 30:
        status = "weak / merge recommended"
    else:
        status = "under review"

    return {
        "status": status,
        "viability_score": viability_score,
        "contractability_score": contractability,
        "active_clinic_rotation": active_rotation,
        "revisit_feasible": revisit_feasible,
        "consult_capacity": consult_capacity,
    }


def _boundary_description(city: dict, cluster: ClusterResult, zone: str) -> str:
    lat, lng = cluster.centroid
    return (
        f"{city['name']} {zone} territory centred near {lat:.3f}, {lng:.3f}. "
        f"Contains {cluster.raw_business_count} discovered businesses across "
        f"{cluster.radius_km:.1f} km radius. "
        f"Opportunity score {cluster.opportunity_score:.1f}. "
        "Boundary follows validated commercial cluster footprint."
    )
