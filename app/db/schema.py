from __future__ import annotations

from sqlalchemy import Boolean, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.db.database import Base


class Country(Base):
    __tablename__ = "countries"
    id: Mapped[str] = mapped_column(String, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    iso3: Mapped[str] = mapped_column(String, nullable=False)
    region: Mapped[str] = mapped_column(String, default="")
    supported: Mapped[bool] = mapped_column(Boolean, default=True)


class CountryProfileModel(Base):
    __tablename__ = "country_profiles"
    country_id: Mapped[str] = mapped_column(ForeignKey("countries.id"), primary_key=True)
    profile_json: Mapped[str] = mapped_column(Text, nullable=False)


class City(Base):
    __tablename__ = "cities"
    id: Mapped[str] = mapped_column(String, primary_key=True)
    country_id: Mapped[str] = mapped_column(ForeignKey("countries.id"), nullable=False)
    name: Mapped[str] = mapped_column(String, nullable=False)
    region: Mapped[str] = mapped_column(String, default="")
    metro_name: Mapped[str] = mapped_column(String, default="")
    population_context: Mapped[int] = mapped_column(Integer, default=0)
    maturity_level: Mapped[str] = mapped_column(String, default="")
    center_lat: Mapped[float] = mapped_column(Float, default=0)
    center_lng: Mapped[float] = mapped_column(Float, default=0)
    discovery_json: Mapped[str] = mapped_column(Text, default="{}")


class MetroCore(Base):
    __tablename__ = "metro_cores"
    id: Mapped[str] = mapped_column(String, primary_key=True)
    city_id: Mapped[str] = mapped_column(ForeignKey("cities.id"), nullable=False)
    name: Mapped[str] = mapped_column(String, nullable=False)
    center_lat: Mapped[float] = mapped_column(Float, default=0)
    center_lng: Mapped[float] = mapped_column(Float, default=0)
    notes: Mapped[str] = mapped_column(Text, default="")


class SourceRecordModel(Base):
    __tablename__ = "source_records"
    id: Mapped[str] = mapped_column(String, primary_key=True)
    city_id: Mapped[str] = mapped_column(ForeignKey("cities.id"), nullable=False)
    source_name: Mapped[str] = mapped_column(String, nullable=False)
    source_record_id: Mapped[str] = mapped_column(String, nullable=False)
    confidence: Mapped[float] = mapped_column(Float, default=0.0)
    raw_payload: Mapped[str] = mapped_column(Text, default="{}")


class CanonicalBusinessModel(Base):
    __tablename__ = "canonical_businesses"
    id: Mapped[str] = mapped_column(String, primary_key=True)
    city_id: Mapped[str] = mapped_column(ForeignKey("cities.id"), nullable=False)
    name: Mapped[str] = mapped_column(String, nullable=False)
    address: Mapped[str] = mapped_column(String, default="")
    category: Mapped[str] = mapped_column(String, default="")
    latitude: Mapped[float] = mapped_column(Float, default=0)
    longitude: Mapped[float] = mapped_column(Float, default=0)
    confidence: Mapped[float] = mapped_column(Float, default=0.0)
    geometry_geojson: Mapped[str] = mapped_column(Text, default="{}")
    provenance_json: Mapped[str] = mapped_column(Text, default="[]")


class BusinessCategoryModel(Base):
    __tablename__ = "business_categories"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    business_id: Mapped[str] = mapped_column(ForeignKey("canonical_businesses.id"), nullable=False)
    category: Mapped[str] = mapped_column(String, nullable=False)
    confidence: Mapped[float] = mapped_column(Float, default=0.0)


class BusinessScoreModel(Base):
    __tablename__ = "business_scores"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    business_id: Mapped[str] = mapped_column(ForeignKey("canonical_businesses.id"), nullable=False)
    suitability_score: Mapped[float] = mapped_column(Float, default=0.0)
    weighted_opportunity_score: Mapped[float] = mapped_column(Float, default=0.0)
    explanation_json: Mapped[str] = mapped_column(Text, default="{}")


class ClusterModel(Base):
    __tablename__ = "clusters"
    id: Mapped[str] = mapped_column(String, primary_key=True)
    city_id: Mapped[str] = mapped_column(ForeignKey("cities.id"), nullable=False)
    core_id: Mapped[str] = mapped_column(ForeignKey("metro_cores.id"), nullable=False)
    summary_json: Mapped[str] = mapped_column(Text, default="{}")
    geometry_geojson: Mapped[str] = mapped_column(Text, default="{}")


class ClusterMemberModel(Base):
    __tablename__ = "cluster_members"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    cluster_id: Mapped[str] = mapped_column(ForeignKey("clusters.id"), nullable=False)
    business_id: Mapped[str] = mapped_column(ForeignKey("canonical_businesses.id"), nullable=False)


class TerritoryModel(Base):
    __tablename__ = "territories"
    id: Mapped[str] = mapped_column(String, primary_key=True)
    city_id: Mapped[str] = mapped_column(ForeignKey("cities.id"), nullable=False)
    core_id: Mapped[str] = mapped_column(ForeignKey("metro_cores.id"), nullable=False)
    name: Mapped[str] = mapped_column(String, nullable=False)
    status: Mapped[str] = mapped_column(String, default="under_review")
    current_version_id: Mapped[str] = mapped_column(String, default="")


class TerritoryVersionModel(Base):
    __tablename__ = "territory_versions"
    id: Mapped[str] = mapped_column(String, primary_key=True)
    territory_id: Mapped[str] = mapped_column(ForeignKey("territories.id"), nullable=False)
    version_number: Mapped[str] = mapped_column(String, nullable=False)
    geometry_geojson: Mapped[str] = mapped_column(Text, default="{}")
    coordinate_csv: Mapped[str] = mapped_column(Text, default="")
    boundary_description: Mapped[str] = mapped_column(Text, default="")
    locked: Mapped[bool] = mapped_column(Boolean, default=False)


class TerritoryScoreModel(Base):
    __tablename__ = "territory_scores"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    territory_version_id: Mapped[str] = mapped_column(ForeignKey("territory_versions.id"), nullable=False)
    viability_score: Mapped[float] = mapped_column(Float, default=0.0)
    contractability_score: Mapped[float] = mapped_column(Float, default=0.0)
    validation_status: Mapped[str] = mapped_column(String, default="")
    score_json: Mapped[str] = mapped_column(Text, default="{}")


class TerritoryPostalUnitModel(Base):
    __tablename__ = "territory_postal_units"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    territory_version_id: Mapped[str] = mapped_column(ForeignKey("territory_versions.id"), nullable=False)
    postal_unit: Mapped[str] = mapped_column(String, nullable=False)


class TerritoryCorridorModel(Base):
    __tablename__ = "territory_corridors"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    territory_version_id: Mapped[str] = mapped_column(ForeignKey("territory_versions.id"), nullable=False)
    corridor_name: Mapped[str] = mapped_column(String, nullable=False)


class TerritoryStatusHistoryModel(Base):
    __tablename__ = "territory_status_history"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    territory_id: Mapped[str] = mapped_column(ForeignKey("territories.id"), nullable=False)
    status: Mapped[str] = mapped_column(String, nullable=False)
    note: Mapped[str] = mapped_column(Text, default="")
    created_at: Mapped[str] = mapped_column(String, nullable=False)


class CommercialModel(Base):
    __tablename__ = "commercial_models"
    id: Mapped[str] = mapped_column(String, primary_key=True)
    territory_version_id: Mapped[str] = mapped_column(ForeignKey("territory_versions.id"), nullable=False)
    assumptions_json: Mapped[str] = mapped_column(Text, default="{}")


class CommercialScenarioModel(Base):
    __tablename__ = "commercial_scenarios"
    id: Mapped[str] = mapped_column(String, primary_key=True)
    commercial_model_id: Mapped[str] = mapped_column(ForeignKey("commercial_models.id"), nullable=False)
    name: Mapped[str] = mapped_column(String, nullable=False)
    scenario_json: Mapped[str] = mapped_column(Text, default="{}")


class ExportModel(Base):
    __tablename__ = "exports"
    id: Mapped[str] = mapped_column(String, primary_key=True)
    territory_version_id: Mapped[str] = mapped_column(ForeignKey("territory_versions.id"), nullable=False)
    export_type: Mapped[str] = mapped_column(String, nullable=False)
    file_path: Mapped[str] = mapped_column(String, nullable=False)
    generated_at: Mapped[str] = mapped_column(String, nullable=False)


class AdminReviewModel(Base):
    __tablename__ = "admin_reviews"
    id: Mapped[str] = mapped_column(String, primary_key=True)
    territory_version_id: Mapped[str] = mapped_column(ForeignKey("territory_versions.id"), nullable=False)
    state: Mapped[str] = mapped_column(String, nullable=False)
    reviewer: Mapped[str] = mapped_column(String, default="system")
    notes: Mapped[str] = mapped_column(Text, default="")


class IngestionRunModel(Base):
    __tablename__ = "ingestion_runs"
    id: Mapped[str] = mapped_column(String, primary_key=True)
    city_id: Mapped[str] = mapped_column(ForeignKey("cities.id"), nullable=False)
    status: Mapped[str] = mapped_column(String, nullable=False)
    summary_json: Mapped[str] = mapped_column(Text, default="{}")


class AnalysisRunModel(Base):
    __tablename__ = "analysis_runs"
    id: Mapped[str] = mapped_column(String, primary_key=True)
    city_id: Mapped[str] = mapped_column(ForeignKey("cities.id"), nullable=False)
    status: Mapped[str] = mapped_column(String, nullable=False)
    summary_json: Mapped[str] = mapped_column(Text, default="{}")


class AuditLogModel(Base):
    __tablename__ = "audit_logs"
    id: Mapped[str] = mapped_column(String, primary_key=True)
    entity_type: Mapped[str] = mapped_column(String, nullable=False)
    entity_id: Mapped[str] = mapped_column(String, nullable=False)
    action: Mapped[str] = mapped_column(String, nullable=False)
    details_json: Mapped[str] = mapped_column(Text, default="{}")
    created_at: Mapped[str] = mapped_column(String, nullable=False)

