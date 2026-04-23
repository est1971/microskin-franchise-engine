# Architecture Overview

Microskin Territory Intelligence Engine is organized as a configurable, opportunity-driven market analysis platform rather than a static territory calculator.

## Modules

- `app/engine/country_profiles.py`: pluggable country rules for postal systems, admin hierarchy, naming, and export conventions.
- `app/engine/city_discovery.py`: city-level viability classification, launch-phase recommendation, and a visible check that population-only logic can mislead.
- `app/engine/adapters.py`: provider adapter boundary for Google Places, Overture, Mapbox, and future country-specific sources.
- `app/engine/reconciliation.py`: source normalization and deduplication into canonical businesses with provenance.
- `app/engine/scoring.py`: suitability and weighted opportunity scoring using configurable category weights and quality modifiers.
- `app/engine/clustering.py`: weighted density clustering around metro cores.
- `app/engine/territories.py`: cluster-to-territory generation with non-radial polygon creation and written boundaries.
- `app/engine/validation.py`: territory viability, travel, revisit cadence, and contractability checks.
- `app/engine/commercial.py`: conservative, expected, and high-performance commercial projections tied to territory capacity.
- `app/services/exporter.py`: JSON, GeoJSON, CSV, and PDF contract-pack generation.

## Runtime Shape

- FastAPI serves both API and browser UI.
- SQLAlchemy defines the persistent schema.
- The sandbox runtime uses SQLite for portability.
- Production migration SQL for PostgreSQL + PostGIS lives in `app/db/migrations`.
- Seed fixtures demonstrate India, USA, and a blank-profile Singapore baseline without pretending to be live sourced data.

