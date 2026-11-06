from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"

def test_score_approve():
    payload = {
        "transaction_id": "TX-1", "user_id": "U-1", "amount": 100,
        "merchant_category": "general", "country": "ZA", "device_type": "mobile",
        "hour_of_day": 12, "is_weekend": 0, "velocity_1h": 1,
        "velocity_24h": 2, "amount_vs_avg": 1.0
    }
    r = client.post("/score", json=payload)
    assert r.status_code == 200
    assert r.json()["decision"] in ["APPROVE", "REVIEW", "BLOCK"]