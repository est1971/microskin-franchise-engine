from __future__ import annotations

import csv
import json
from pathlib import Path

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

from app.core.config import EXPORT_DIR
from app.core.utils import now_iso, slugify


def export_territory(territory) -> dict[str, str]:
    folder = EXPORT_DIR / slugify(territory.territory_id)
    folder.mkdir(parents=True, exist_ok=True)

    json_path = folder / "territory.json"
    geojson_path = folder / "territory.geojson"
    csv_path = folder / "coordinates.csv"
    pdf_path = folder / "territory-pack.pdf"

    json_path.write_text(json.dumps(territory.model_dump(mode="json"), indent=2), encoding="utf-8")
    geojson_path.write_text(json.dumps(territory.polygon_geojson, indent=2), encoding="utf-8")

    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["latitude", "longitude"])
        for latitude, longitude in territory.coordinates:
            writer.writerow([latitude, longitude])

    pdf = canvas.Canvas(str(pdf_path), pagesize=letter)
    pdf.setTitle(f"{territory.territory_name} Territory Pack")
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(40, 760, territory.territory_name)
    pdf.setFont("Helvetica", 10)
    lines = [
        f"Version: {territory.version_id}",
        f"Generated: {now_iso()}",
        f"Status: {territory.status}",
        f"Country / Region: {territory.country_code} / {territory.state_region}",
        f"Metro / City: {territory.metro} / {territory.city}",
        f"Viability Score: {territory.viability_score}",
        f"Contractability Score: {territory.contractability_score}",
        f"Validation: {territory.validation_status}",
        f"Postal Units: {', '.join(territory.postal_units)}",
        f"Corridors: {', '.join(territory.corridor_streets)}",
        f"Boundary: {territory.written_boundary_description}",
    ]
    y = 730
    for line in lines:
        pdf.drawString(40, y, line[:110])
        y -= 18
    pdf.save()

    return {
        "json": str(json_path),
        "geojson": str(geojson_path),
        "csv": str(csv_path),
        "pdf": str(pdf_path),
    }

