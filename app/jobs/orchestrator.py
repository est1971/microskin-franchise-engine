from __future__ import annotations

from app.core.utils import now_iso
from app.services.repository import refresh_results


def rerun_market(city_id: str) -> dict:
    refresh_results()
    return {
        "job_type": "analysis_rerun",
        "city_id": city_id,
        "status": "completed",
        "progress": 100,
        "completed_at": now_iso(),
        "steps": [
            {"name": "ingestion", "status": "completed"},
            {"name": "reconciliation", "status": "completed"},
            {"name": "clustering", "status": "completed"},
            {"name": "territory_generation", "status": "completed"},
            {"name": "exports", "status": "ready"},
        ],
    }

