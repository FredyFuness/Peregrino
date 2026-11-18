from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_empty_directory():
    response = client.get("/api/v1/churches?search=San%20Miguel")
    assert response.status_code == 200
    assert response.json() == []

def test_search_validation():
    assert client.get("/api/v1/churches?search=" + "x" * 121).status_code == 422
