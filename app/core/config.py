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
    # ── Category weights ─────────────────────────────────────────────────────
    # Weights reflect how likely Microskin treatments can be placed in each
    # business type.  No demographic or location assumptions — pure category
    # relevance.  The same weights apply to every country.
    category_weights: dict = field(
        default_factory=lambda: {
            "hospital":                         1.5,
            "dermatologist":                    1.4,
            "aesthetic_clinic":                 1.3,
            "plastic_surgery":                  1.2,
            "med_spa":                          1.1,
            "hospital_dermatology_department":  1.1,  # legacy alias
            "general_practice":                 0.6,
            "pharmacy":                         0.7,
            "beauty_spa":                       0.8,
            "pmu_artist":                       0.7,
            "premium_salon":                    0.5,
        }
    )
    # ── Territory tier thresholds (opportunity score) ─────────────────────
    # Opportunity score = Σ(category_weight × suitability_score) per territory
    territory_tiers: dict = field(
        default_factory=lambda: {
            "Platinum": 120,
            "Gold":      70,
            "Silver":    35,
            "Standard":   0,
        }
    )
    # ── Payback years per tier (drives franchise fee) ─────────────────────
    tier_payback_years: dict = field(
        default_factory=lambda: {
            "Platinum": 2.5,
            "Gold":     2.0,
            "Silver":   1.5,
            "Standard": 1.2,
        }
    )
    # ── Market maturity multiplier per maturity label ──────────────────────
    # Adjusts franchise fee for market development stage.
    # GDP per capita is NOT a primary valuation driver — it is only used as
    # a floor check (capped at 12% influence) so no market is undervalued.
    market_maturity_multipliers: dict = field(
        default_factory=lambda: {
            "established":  1.05,
            "mature":       1.00,
            "developing":   0.88,
            "emerging":     0.75,
            "nascent":      0.65,
        }
    )
    scenario_multipliers: dict = field(
        default_factory=lambda: {
            "conservative":      0.82,
            "expected":          1.00,
            "high_performance":  1.22,
        }
    )


config = AppConfig()
INSTANCE_DIR.mkdir(exist_ok=True)
EXPORT_DIR.mkdir(exist_ok=True)
