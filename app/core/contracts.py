from __future__ import annotations

from typing import Any, Literal

from pydantic import BaseModel, Field


TerritoryStatus = Literal["available", "reserved", "sold", "under_review"]


class CountryProfile(BaseModel):
    code: str
    name: str
    postal_system_type: str
    admin_hierarchy: list[str]
    preferred_geometry_snap_hierarchy: list[str]
    normalization: dict[str, Any]
    market_defaults: dict[str, Any]
    category_mapping_adjustments: dict[str, float]
    naming_convention: str
    export_convention: dict[str, Any]


class BusinessRecord(BaseModel):
    record_id: str
    source: str
    source_confidence: float
    city_id: str
    country_code: str
    name: str
    address: str
    region: str
    city: str
    latitude: float
    longitude: float
    category_hint: str
    rating: float = 0.0
    review_count: int = 0
    website_present: bool = False
    premium_corridor: bool = False
    completeness: float = 0.5
    stale: bool = False
    metadata: dict[str, Any] = Field(default_factory=dict)


class CanonicalBusiness(BaseModel):
    canonical_id: str
    city_id: str
    country_code: str
    name: str
    address: str
    region: str
    city: str
    latitude: float
    longitude: float
    category: str
    category_confidence: float
    suitability_score: float
    weighted_opportunity_score: float
    quality_modifiers: dict[str, float]
    confidence: float
    sources: list[BusinessRecord]


class ClusterResult(BaseModel):
    cluster_id: str
    city_id: str
    core_id: str
    business_ids: list[str]
    raw_business_count: int
    weighted_business_count: float
    viable_business_count: int = 0   # businesses with weighted_opportunity_score >= 4.0
    opportunity_score: float = 0.0   # Σ(category_weight × suitability_score) — primary valuation driver
    category_mix: dict[str, int]
    density_score: float
    radius_km: float
    travel_efficiency: float
    confidence_score: float
    centroid: tuple[float, float]


class CommercialScenario(BaseModel):
    name: str
    monthly_clinic_days: int
    consults_per_day: float
    monthly_consults: float
    annual_product_revenue: float
    annual_consultation_revenue: float
    gross_profit: float
    royalties: float
    marketing_contribution: float
    platform_fee: float
    net_franchisee_income: float
    recommended_franchise_price_low: float
    recommended_franchise_price_high: float


class TerritoryResult(BaseModel):
    territory_id: str
    territory_name: str
    version_id: str
    country_code: str
    state_region: str
    metro: str
    city: str
    core_id: str
    polygon_geojson: dict[str, Any]
    coordinates: list[list[float]]
    postal_units: list[str]
    corridor_streets: list[str]
    written_boundary_description: str
    viability_score: float
    opportunity_score: float = 0.0   # drives tier and franchise fee
    tier: str = "Standard"           # Platinum / Gold / Silver / Standard
    opportunity_summary: dict[str, Any]
    validation_status: str
    contractability_score: float
    status: TerritoryStatus
    scenarios: list[CommercialScenario]

