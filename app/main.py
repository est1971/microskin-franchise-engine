from __future__ import annotations

from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

from app.core.config import BASE_DIR, config
from app.core.utils import now_iso
from app.db.database import Base, engine
from app.data.business_store import invalidate_city
from app.jobs.orchestrator import rerun_market
from app.services.exporter import export_territory
from app.services.repository import city_detail, country_detail, get_summary, list_countries, territory_detail


app = FastAPI(title=config.app_name, version="1.0.0")
templates = Jinja2Templates(directory=str(BASE_DIR / "app" / "templates"))
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "app" / "static")), name="static")
Base.metadata.create_all(bind=engine)


@app.get("/", response_class=HTMLResponse)
async def index(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"title": config.app_name, "generated": now_iso()},
    )


@app.get("/health")
async def health() -> dict:
    return {"ok": True, "app": config.app_name, "generated": now_iso()}


@app.get("/api/summary")
async def summary() -> dict:
    return get_summary()


@app.get("/api/countries")
async def countries() -> list[dict]:
    return list_countries()


@app.get("/api/countries/{country_code}")
def country(country_code: str) -> dict:
    return country_detail(country_code)


@app.get("/api/cities/{city_id}")
def city(city_id: str) -> dict:
    # Synchronous endpoint — FastAPI runs this in a threadpool so the long-running
    # Google Places grid search does not block the async event loop.
    # Other endpoints (summary, countries) remain responsive during discovery.
    try:
        return city_detail(city_id)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"City pipeline error: {exc}") from exc


@app.get("/api/territories/{territory_id}")
async def territory(territory_id: str) -> dict:
    try:
        return territory_detail(territory_id).model_dump(mode="json")
    except KeyError as error:
        raise HTTPException(status_code=404, detail="Territory not found") from error


@app.post("/api/admin/rerun/{city_id}")
async def admin_rerun(city_id: str) -> dict:
    return rerun_market(city_id)


@app.post("/api/admin/invalidate/{city_id}")
async def admin_invalidate(city_id: str) -> dict:
    """Mark a city's business cache as stale so the next pipeline run re-calls Google Places."""
    invalidate_city(city_id)
    return {"ok": True, "city_id": city_id, "message": "City cache invalidated — next load will re-discover via Google Places"}


@app.get("/api/territories/{territory_id}/export/{fmt}")
async def territory_export(territory_id: str, fmt: str):
    territory_model = territory_detail(territory_id)
    exports = export_territory(territory_model)
    if fmt not in exports:
        raise HTTPException(status_code=404, detail="Unsupported export format")
    return FileResponse(Path(exports[fmt]))

