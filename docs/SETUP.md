# Setup Instructions

## Local sandbox setup

```bash
python3 -m venv .venv
./.venv/bin/pip install fastapi uvicorn sqlalchemy alembic jinja2 pydantic shapely openpyxl pytest httpx pytest-asyncio python-multipart reportlab
cp .env.example .env
./.venv/bin/uvicorn app.main:app --reload
```

## Production path

1. Provision PostgreSQL with PostGIS.
2. Apply `app/db/migrations/001_initial_postgis.sql`.
3. Replace the default SQLite URL with a PostgreSQL URL.
4. Swap fixture adapters for real provider credentials.
5. Run validation before locking territory versions.

