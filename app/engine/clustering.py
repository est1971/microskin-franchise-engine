from __future__ import annotations

from collections import Counter

from app.core.contracts import CanonicalBusiness, ClusterResult
from app.core.utils import centroid, haversine_km, slugify


def _city_radius(country_code: str) -> float:
    return 3.8 if country_code == "US" else 4.2


def detect_clusters(city_id: str, core_id: str, businesses: list[CanonicalBusiness], core_center: tuple[float, float]) -> list[ClusterResult]:
    radius = _city_radius(businesses[0].country_code if businesses else "IN")
    candidate = [business for business in businesses if haversine_km(core_center[0], core_center[1], business.latitude, business.longitude) <= 18]
    visited: set[str] = set()
    clusters: list[ClusterResult] = []

    for business in candidate:
        if business.canonical_id in visited:
            continue
        neighborhood = [
            item for item in candidate
            if haversine_km(business.latitude, business.longitude, item.latitude, item.longitude) <= radius
        ]
        cluster_weight = sum(item.weighted_opportunity_score for item in neighborhood) / 10
        if len(neighborhood) < 2 and cluster_weight < 5:
            continue
        ids = []
        points = []
        for member in neighborhood:
            visited.add(member.canonical_id)
            ids.append(member.canonical_id)
            points.append((member.latitude, member.longitude))
        center = centroid(points)
        distances = [haversine_km(center[0], center[1], pt[0], pt[1]) for pt in points]
        category_mix = Counter(member.category for member in neighborhood)
        # viable = businesses that cleared a minimum quality bar (score ≥ 4.0 means
        # at least suitability ~0.5 with a mid-weight category — excludes junk data)
        viable_count = sum(1 for m in neighborhood if m.weighted_opportunity_score >= 4.0)
        clusters.append(
            ClusterResult(
                cluster_id=f"cluster-{slugify(city_id)}-{slugify(core_id)}-{len(clusters)+1}",
                city_id=city_id,
                core_id=core_id,
                business_ids=ids,
                raw_business_count=len(neighborhood),
                weighted_business_count=round(cluster_weight, 2),
                viable_business_count=viable_count,
                category_mix=dict(category_mix),
                density_score=round(min(1.0, cluster_weight / max(max(distances, default=1), 1)), 2),
                radius_km=round(max(distances, default=0.5) + 0.6, 2),
                travel_efficiency=round(max(0.3, 1 - (max(distances, default=0.5) / 10)), 2),
                confidence_score=round(min(0.98, sum(member.confidence for member in neighborhood) / len(neighborhood)), 2),
                centroid=center,
            )
        )
    return clusters

