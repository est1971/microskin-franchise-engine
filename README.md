# Microskin Territory Intelligence Engine™

Microskin Territory Intelligence Engine is a production-oriented territory intelligence platform for opportunity-driven franchise design. It turns market fixtures or adapter-fed business records into reconciled business entities, commercial clusters, viable franchise territories, contract-ready exports, and territory-aware commercial projections.

## Stack

- FastAPI application server with typed Pydantic contracts
- SQLAlchemy schema with explicit PostGIS production migration SQL
- Leaflet-powered map UI with a premium, clinically credible presentation layer
- ReportLab PDF generation for contract packs
- Pytest coverage for engine logic, APIs, and UI contract checks

## Why this stack

The original brief preferred Next.js and TypeScript. This build uses an equivalent Python-first stack because the current environment provides Python but no Node toolchain. That keeps the deliverable deployable, testable, and runnable end to end in this sandbox while preserving a modular service boundary that can be fronted by a React client later if desired.

## Run locally

```bash
python3 -m venv .venv
./.venv/bin/pip install fastapi uvicorn sqlalchemy alembic jinja2 pydantic shapely openpyxl pytest httpx pytest-asyncio python-multipart reportlab
./.venv/bin/uvicorn app.main:app --reload
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Validate

```bash
./.venv/bin/python scripts/run_validation.py
```

## Deployment path

```bash
./.venv/bin/uvicorn app.main:app --host 0.0.0.0 --port 8000
```

Production deployment should swap the default SQLite sandbox database for PostgreSQL with PostGIS using the migration in [app/db/migrations/001_initial_postgis.sql](/Users/davidrobinson/Documents/Playground/app/db/migrations/001_initial_postgis.sql).
