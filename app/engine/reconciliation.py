from __future__ import annotations

from collections import defaultdict

from app.core.contracts import BusinessRecord, CanonicalBusiness
from app.core.utils import normalize_text, slugify


def reconcile_businesses(records: list[BusinessRecord]) -> list[CanonicalBusiness]:
    buckets: dict[str, list[BusinessRecord]] = defaultdict(list)
    for record in records:
        key = f"{normalize_text(record.name)}|{normalize_text(record.address)}"
        buckets[key].append(record)

    canonical: list[CanonicalBusiness] = []
    for key, group in buckets.items():
        primary = max(group, key=lambda item: item.source_confidence + item.completeness)
        confidence = min(0.99, sum(item.source_confidence for item in group) / len(group) + (0.05 * (len(group) - 1)))
        canonical.append(
            CanonicalBusiness(
                canonical_id=f"cb-{slugify(primary.city_id)}-{slugify(primary.name)}",
                city_id=primary.city_id,
                country_code=primary.country_code,
                name=primary.name,
                address=primary.address,
                region=primary.region,
                city=primary.city,
                latitude=primary.latitude,
                longitude=primary.longitude,
                category=primary.category_hint,
                category_confidence=0.65,
                suitability_score=0.0,
                weighted_opportunity_score=0.0,
                quality_modifiers={},
                confidence=round(confidence - (0.08 if any(item.stale for item in group) else 0.0), 2),
                sources=group,
            )
        )
    return canonical

