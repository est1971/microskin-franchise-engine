from __future__ import annotations

import sys
from pathlib import Path

from fastapi.testclient import TestClient

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.main import app


def main() -> None:
    client = TestClient(app)
    assert client.get("/health").status_code == 200
    summary = client.get("/api/summary")
    assert summary.status_code == 200
    city = client.get("/api/cities/us-new-york")
    assert city.status_code == 200
    territory_id = city.json()["territories"][0]["territory_id"]
    territory = client.get(f"/api/territories/{territory_id}")
    assert territory.status_code == 200
    export_json = client.get(f"/api/territories/{territory_id}/export/json")
    assert export_json.status_code == 200
    print("Smoke OK:", territory_id)


if __name__ == "__main__":
    main()
