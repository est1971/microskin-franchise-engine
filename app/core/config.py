from __future__ import annotations

from dataclasses import dataclass, field
import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[2]
INSTANCE_DIR = BASE_DIR / "instance"
EXPORT_DIR = BASE_DIR / "exports"


@dataclass(slots=True)
class AppConfig:
    app_name: str = os.getenv("MICROSKIN_APP_NAME", "Microskin Territory Intelligence Engine™")
    # On Railway, mount a persistent volume at /data and set DATABASE_URL to
    # sqlite:////data/microskin.db so the DB survives redeployments.
    # Locally the default sqlite in instance/ is used.
    database_url: str = os.getenv(
        "MICROSKIN_DATABASE_URL",
        os.getenv("DATABASE_URL", f"sqlite:///{(INSTANCE_DIR / 'microskin.db').as_posix()}")
    )
    data_confidence_threshold: float = float(os.getenv("MICROSKIN_DATA_CONFIDENCE_THRESHOLD", "0.62"))
    contractability_threshold: float = float(os.getenv("MICROSKIN_CONTRACTABILITY_THRESHOLD", "0.70"))
    refresh_days_soft_limit: int = 90
    operating_model: dict = field(
        default_factory=lambda: {
            "clinic_days_per_week": 4,
            "admin_days_per_week": 1,
            "clinic_days_per_month_min": 16,
            "clinic_days_per_month_max": 20,
            "consultations_per_month_target": 60,
            "revisit_days_min": 60,
            "revisit_days_max": 90,
            "active_clinic_rotation_min": 40,
            "active_clinic_rotation_max": 60,
            "viable_opportunities_min": 80,
            "viable_opportunities_max": 120,
        }
    )
    category_weights: dict = field(
        default_factory=lambda: {
            "dermatologist": 1.2,
            "aesthetic_clinic": 1.0,
            "med_spa": 0.9,
            "hospital_dermatology_department": 0.8,
            "pmu_artist": 0.7,
            "premium_salon": 0.5,
        }
    )
    scenario_multipliers: dict = field(
        default_factory=lambda: {
            "conservative": 0.82,
            "expected": 1.0,
            "high_performance": 1.22,
        }
    )


config = AppConfig()
INSTANCE_DIR.mkdir(exist_ok=True)
EXPORT_DIR.mkdir(exist_ok=True)
