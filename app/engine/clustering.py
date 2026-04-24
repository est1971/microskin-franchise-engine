from __future__ import annotations

"""
Data-driven DBSCAN clustering.

No hardcoded cores.  No demographic assumptions.  Wherever viable businesses
exist in the metro, this algorithm finds them and creates a cluster.  Each
cluster becomes one territory.

A large sparse cluster = a large territory.  That's a feature, not a bug.
Franchise buyers see more opportunity, not less.

Overlap fix: DBSCAN assigns each business to exactly one cluster by design.
The old visited-set bug cannot occur here.
"""

from collections import Counter

from app.core.contracts import CanonicalBusiness, ClusterResult
from app.core.utils import centroid, haversine_km, slugify
from app.core.config import config


# ── DBSCAN parameters ──────────────────────────────────────────────────────────
# eps_km: two businesses are "neighbours" if within this distance.
# min_samples: minimum neighbours for a point to be a core point.
# Noise points (isolated single businesses far from any cluster) are assigned
# to their nearest cluster rather than discarded — no business is left behind.
DBSCAN_EPS_KM    = 2.8
DBSCAN_MIN_SAMP  = 3


def _get_neighbours(idx: int, businesses: list[CanonicalBusiness], eps_km: float) -> list[int]:
    b = businesses[idx]
    return [
        j for j in range(len(businesses))
        if haversine_km(b.latitude, b.longitude,
                        businesses[j].latitude, businesses[j].longitude) <= eps_km
    ]


def _dbscan(
    businesses: list[CanonicalBusiness],
    eps_km: float = DBSCAN_EPS_KM,
    min_samples: int = DBSCAN_MIN_SAMP,
) -> list[int]:
    """
    Pure-Python DBSCAN.  Returns list of cluster labels, one per business.
    Label -1 = noise (will be assigned to nearest cluster in a second pass).
    Labels 0..n-1 = cluster indices.
    """
    n = len(businesses)
    labels = [-2] * n   # -2 = unvisited
    cluster_id = -1

    for i in range(n):
        if labels[i] != -2:
            continue
        neighbours = _get_neighbours(i, businesses, eps_km)
        if len(neighbours) < min_samples:
            labels[i] = -1   # noise for now
            continue
        cluster_id += 1
        labels[i] = cluster_id
        seed_set = [j for j in neighbours if j != i]
        ptr = 0
        while ptr < len(seed_set):
            q = seed_set[ptr]
            ptr += 1
            if labels[q] == -1:
                labels[q] = cluster_id   # border point → promote to cluster
            if labels[q] != -2:
                continue
            labels[q] = cluster_id
            q_neighbours = _get_neighbours(q, businesses, eps_km)
            if len(q_neighbours) >= min_samples:
                seed_set.extend(j for j in q_neighbours if labels[j] == -2)

    # ── Assign noise to nearest cluster ───────────────────────────────────────
    # We never discard a business.  Isolated locations (e.g. a lone hospital
    # in a suburban area) get pulled into the nearest cluster so they
    # contribute to territory opportunity scores.
    if cluster_id >= 0:
        cluster_centroids: list[tuple[float, float]] = []
        for cid in range(cluster_id + 1):
            pts = [
                (businesses[i].latitude, businesses[i].longitude)
                for i in range(n) if labels[i] == cid
            ]
            if pts:
                lat_c = sum(p[0] for p in pts) / len(pts)
                lng_c = sum(p[1] for p in pts) / len(pts)
                cluster_centroids.append((lat_c, lng_c))
            else:
                cluster_centroids.append((0.0, 0.0))

        for i in range(n):
            if labels[i] == -1:
                nearest = min(
                    range(len(cluster_centroids)),
                    key=lambda cid: haversine_km(
                        businesses[i].latitude, businesses[i].longitude,
                        cluster_centroids[cid][0], cluster_centroids[cid][1],
                    ),
                )
                labels[i] = nearest

    return labels


def detect_clusters(
    city_id: str,
    businesses: list[CanonicalBusiness],
) -> list[ClusterResult]:
    """
    Run DBSCAN over all businesses in the metro and return one ClusterResult
    per cluster.  Works for any city in any country — no manual core input.
    """
    if not businesses:
        return []

    labels = _dbscan(businesses)
    num_clusters = max(labels) + 1

    if num_clusters <= 0:
        # All noise, single territory
        labels = [0] * len(businesses)
        num_clusters = 1

    cluster_map: dict[int, list[CanonicalBusiness]] = {i: [] for i in range(num_clusters)}
    for biz, label in zip(businesses, labels):
        if label >= 0:
            cluster_map[label].append(biz)

    results: list[ClusterResult] = []
    for cid, members in cluster_map.items():
        if not members:
            continue

        points    = [(m.latitude, m.longitude) for m in members]
        center    = centroid(points)
        distances = [haversine_km(center[0], center[1], p[0], p[1]) for p in points]
        max_dist  = max(distances, default=0.5)

        category_mix  = Counter(m.category for m in members)
        viable_count  = sum(1 for m in members if m.weighted_opportunity_score >= 4.0)
        cluster_weight = sum(m.weighted_opportunity_score for m in members) / 10

        # Opportunity score: sum of (category_weight × suitability) per business
        opp_score = round(sum(
            config.category_weights.get(m.category, 0.5) * m.suitability_score
            for m in members
        ), 2)

        density_score   = round(min(1.0, cluster_weight / max(max_dist, 1)), 2)
        travel_eff      = round(max(0.25, 1 - (max_dist / 15)), 2)
        confidence_avg  = round(min(0.98, sum(m.confidence for m in members) / len(members)), 2)

        results.append(ClusterResult(
            cluster_id=f"cluster-{slugify(city_id)}-{cid + 1:02d}",
            city_id=city_id,
            core_id=f"auto-core-{cid + 1:02d}",   # auto-generated, not handpicked
            business_ids=[m.canonical_id for m in members],
            raw_business_count=len(members),
            weighted_business_count=round(cluster_weight, 2),
            viable_business_count=viable_count,
            opportunity_score=opp_score,
            category_mix=dict(category_mix),
            density_score=density_score,
            radius_km=round(max_dist + 0.5, 2),
            travel_efficiency=travel_eff,
            confidence_score=confidence_avg,
            centroid=center,
        ))

    return results
