from __future__ import annotations

from collections import defaultdict

from shapely.geometry import MultiPoint, mapping

from app.core.contracts import ClusterResult, CommercialScenario, TerritoryResult
from app.core.utils import slugify
from app.engine.commercial import project_territory
from app.engine.validation import validate_territory


def _territory_polygon(points: list[tuple[float, float]], buffer_factor: float) -> dict:
    multipoint = MultiPoint([(lng, lat) for lat, lng in points])
    polygon = multipoint.convex_hull.buffer(buffer_factor)
    return mapping(polygon)


def generate_territories(city: dict, clusters: list[ClusterResult], businesses_by_id: dict, profile: dict) -> list[TerritoryResult]:
    grouped: dict[str, list[ClusterResult]] = defaultdict(list)
    for cluster in clusters:
        grouped[cluster.core_id].append(cluster)

    territories: list[TerritoryResult] = []
    for core_id, core_clusters in grouped.items():
        for index, cluster in enumerate(sorted(core_clusters, key=lambda item: item.weighted_business_count, reverse=True), start=1):
            members = [businesses_by_id[business_id] for business_id in cluster.business_ids]
            points = [(item.latitude, item.longitude) for item in members]
            polygon_geojson = _territory_polygon(points, 0.02 if city["country_code"] == "US" else 0.03)
            opportunity_summary = {
                "raw_business_count": cluster.raw_business_count,
                "weighted_viable_count": round(cluster.weighted_business_count * 10.5, 1),
                "category_mix": cluster.category_mix,
                "density_score": cluster.density_score,
                "travel_efficiency": cluster.travel_efficiency,
            }
            validation = validate_territory(cluster, opportunity_summary)
            scenarios = project_territory(cluster, validation)
            territory_name = profile["naming_convention"].format(
                city=city["name"], metro=city["metro"], core=next(core["name"] for core in city["cores"] if core["id"] == core_id), index=index
            )
            territories.append(
                TerritoryResult(
                    territory_id=f"territory-{slugify(cluster.cluster_id)}",
                    territory_name=territory_name,
                    version_id=f"v{index}.0",
                    country_code=city["country_code"],
                    state_region=city["region"],
                    metro=city["metro"],
                    city=city["name"],
                    core_id=core_id,
                    polygon_geojson=polygon_geojson,
                    coordinates=[[round(coord[1], 6), round(coord[0], 6)] for coord in polygon_geojson["coordinates"][0]],
                    postal_units=[f"{city['country_code']}-{core_id[-3:].upper()}-{index:02d}", f"{city['country_code']}-{core_id[-3:].upper()}-{index+10:02d}"],
                    corridor_streets=next(core["corridors"] for core in city["cores"] if core["id"] == core_id),
                    written_boundary_description=_boundary_description(city, cluster, core_id),
                    viability_score=validation["viability_score"],
                    opportunity_summary=opportunity_summary,
                    validation_status=validation["status"],
                    contractability_score=validation["contractability_score"],
                    status="available" if validation["status"].startswith("valid") else "under_review",
                    scenarios=scenarios,
                )
            )
    return territories


def _boundary_description(city: dict, cluster: ClusterResult, core_id: str) -> str:
    core = next(core for core in city["cores"] if core["id"] == core_id)
    lat, lng = cluster.centroid
    return (
        f"{city['name']} / {core['name']} territory centered near {lat:.3f}, {lng:.3f}, "
        f"anchored by {', '.join(core['corridors'])}, extending around the validated commercial cluster footprint "
        "and excluding sparse non-commercial gap areas."
    )

