from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_approve():
    r = client.post("/score", json={"amount": 100, "country": "ZA", "velocity_1h": 1})
    assert r.status_code == 200
    assert r.json()["decision"] == "APPROVE"

def test_review():
    r = client.post("/score", json={"amount": 6000, "country": "ZA", "velocity_1h": 1})
    assert r.json()["decision"] == "REVIEW"

def test_block():
    r = client.post("/score", json={"amount": 15000, "country": "US", "velocity_1h": 12})
    assert r.json()["decision"] == "BLOCK"