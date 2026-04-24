"""Business persistence store.

Provides a thin read/write layer over the ``business_cache`` and
``city_discovery_status`` SQLite tables so the adapter stack is called
exactly once per city, ever.

Usage in pipeline::

    from app.data.business_store import has_city_data, load_city_businesses, save_city_businesses

    if has_city_data(city_id):
        raw_records = load_city_businesses(city_id)
    else:
        raw_records = [r for adapter in adapter_stack() for r in adapter.discover(city_id)]
        save_city_businesses(city_id, raw_records)
"""
from __future__ import annotations

import json
from datetime import datetime, timezone

from app.core.contracts import BusinessRecord
from app.db.database import session_scope
from app.db.schema import BusinessCacheModel, CityDiscoveryStatusModel


def _utcnow() -> str:
    return datetime.now(timezone.utc).isoformat()


# ── Public API ─────────────────────────────────────────────────────────────────

def has_city_data(city_id: str) -> bool:
    """Return True if the city has already been discovered and cached."""
    with session_scope() as session:
        row = session.get(CityDiscoveryStatusModel, city_id)
        return row is not None and row.status == "discovered"


def load_city_businesses(city_id: str) -> list[BusinessRecord]:
    """Load all cached BusinessRecords for *city_id* from the database."""
    with session_scope() as session:
        rows = (
            session.query(BusinessCacheModel)
            .filter(BusinessCacheModel.city_id == city_id)
            .all()
        )
    records = []
    for row in rows:
        records.append(
            BusinessRecord(
                record_id=row.record_id,
                source=row.source,
                source_confidence=row.source_confidence,
                city_id=row.city_id,
                country_code=row.country_code,
                name=row.name,
                address=row.address,
                region=row.region,
                city=row.city,
                latitude=row.latitude,
                longitude=row.longitude,
                category_hint=row.category_hint,
                rating=row.rating,
                review_count=row.review_count,
                website_present=row.website_present,
                premium_corridor=row.premium_corridor,
                completeness=row.completeness,
                stale=row.stale,
                metadata=json.loads(row.metadata_json or "{}"),
            )
        )
    return records


def save_city_businesses(city_id: str, records: list[BusinessRecord]) -> None:
    """Persist *records* to ``business_cache`` and mark the city as discovered.

    Existing records for the city are deleted first so a re-discovery (forced
    refresh) always produces a clean snapshot.
    """
    now = _utcnow()
    with session_scope() as session:
        # Remove any stale records from a previous partial run
        session.query(BusinessCacheModel).filter(
            BusinessCacheModel.city_id == city_id
        ).delete(synchronize_session=False)

        for record in records:
            session.add(
                BusinessCacheModel(
                    record_id=record.record_id,
                    source=record.source,
                    source_confidence=record.source_confidence,
                    city_id=record.city_id,
                    country_code=record.country_code,
                    name=record.name,
                    address=record.address,
                    region=record.region,
                    city=record.city,
                    latitude=record.latitude,
                    longitude=record.longitude,
                    category_hint=record.category_hint,
                    rating=record.rating,
                    review_count=record.review_count,
                    website_present=record.website_present,
                    premium_corridor=record.premium_corridor,
                    completeness=record.completeness,
                    stale=record.stale,
                    metadata_json=json.dumps(record.metadata),
                    discovered_at=now,
                )
            )

        # Upsert the discovery status
        status_row = session.get(CityDiscoveryStatusModel, city_id)
        if status_row:
            status_row.discovered_at = now
            status_row.business_count = len(records)
            status_row.status = "discovered"
        else:
            session.add(
                CityDiscoveryStatusModel(
                    city_id=city_id,
                    discovered_at=now,
                    business_count=len(records),
                    status="discovered",
                )
            )


def invalidate_city(city_id: str) -> None:
    """Mark a city as stale so the next pipeline run re-calls Google Places."""
    with session_scope() as session:
        row = session.get(CityDiscoveryStatusModel, city_id)
        if row:
            row.status = "stale"
