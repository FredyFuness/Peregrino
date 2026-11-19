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
    assert len(response.json()) == 2

def test_sagrada_familia_schedule():
    churches = client.get("/api/v1/churches?search=Sagrada%20Familia").json()
    assert len(churches) == 1
    assert churches[0]["schedule_status"] == "community_reported"
    assert churches[0]["masses"][1]["times"] == ["06:00", "10:00", "18:00"]

def test_cathedral_broadcast_schedule():
    churches = client.get("/api/v1/churches?search=Catedral").json()
    assert churches[0]["schedule_status"] == "broadcast_reported"
    assert churches[0]["masses"][0]["times"] == ["07:00", "16:00"]
    assert churches[0]["masses"][1]["times"] == ["09:00"]

def test_search_validation():
    assert client.get("/api/v1/churches?search=" + "x" * 121).status_code == 422
