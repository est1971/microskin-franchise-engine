from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["ok"] is True


def test_country_and_city_endpoints():
    countries = client.get("/api/countries")
    assert countries.status_code == 200
    assert any(item["code"] == "IN" for item in countries.json())

    city = client.get("/api/cities/us-new-york")
    assert city.status_code == 200
    payload = city.json()
    assert payload["analysis"]["suggested_economic_cores"] >= 3
    assert len(payload["territories"]) >= 2


def test_export_endpoint():
    city = client.get("/api/cities/in-delhi-ncr").json()
    territory_id = city["territories"][0]["territory_id"]
    response = client.get(f"/api/territories/{territory_id}/export/json")
    assert response.status_code == 200

