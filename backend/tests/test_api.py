from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_san_miguel_directory():
    response = client.get("/api/v1/churches?search=San%20Miguel")
    assert response.status_code == 200
    assert len(response.json()) == 22

def test_sagrada_familia_schedule():
    churches = client.get("/api/v1/churches?search=Sagrada%20Familia").json()
    assert len(churches) == 1
    assert churches[0]["schedule_status"] == "community_reported"
    assert churches[0]["masses"][1]["times"] == ["06:00", "10:00", "18:00"]

def test_cathedral_reported_schedule():
    churches = client.get("/api/v1/churches?search=Catedral").json()
    assert churches[0]["schedule_status"] == "community_reported"
    assert churches[0]["masses"][0]["times"] == ["05:30"]
    assert churches[0]["masses"][1]["times"] == ["05:30", "08:30", "17:00"]
    assert "16:00" in churches[0]["unconfirmed_masses"][0]["times"]
    assert len(churches[0]["opening_hours"]) == 6

def test_search_validation():
    assert client.get("/api/v1/churches?search=" + "x" * 121).status_code == 422
