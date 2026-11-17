import pytest
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "TRAVELMATE" in data["service"].upper()


def test_destinations_search():
    response = client.get("/api/destinations/search?q=Udaipur")
    assert response.status_code == 200
    res = response.json()
    assert res["success"] is True
    # New API returns { destinations: [...], total: N, ... }
    data = res["data"]
    destinations = data["destinations"] if isinstance(data, dict) else data
    dest_names = [d["name"] for d in destinations]
    assert "Udaipur" in dest_names


def test_places_retrieval():
    response = client.get("/api/places?destination=Udaipur")
    assert response.status_code == 200
    res = response.json()
    assert res["success"] is True
    assert len(res["data"]) > 0
    assert any("Palace" in p["name"] or "Lake" in p["name"] for p in res["data"])


def test_crowd_prediction():
    payload = {
        "destination": "Udaipur",
        "category": "heritage",
        "day_of_week": 6,
        "is_weekend": True,
        "hour": 15,
        "month": 11,
        "base_popularity": 0.85
    }
    response = client.post("/api/predictions/crowd", json=payload)
    assert response.status_code == 200
    res = response.json()
    assert res["success"] is True
    assert "crowd_score" in res["data"]
    assert 0 <= res["data"]["crowd_score"] <= 100


def test_hybrid_recommendation():
    payload = {
        "user_id": "USR_TEST",
        "destination": "Udaipur",
        "interests": {"heritage": 0.9, "nature": 0.8},
        "budget_level": "medium",
        "pace": "moderate",
        "num_candidates": 5
    }
    response = client.post("/api/recommend", json=payload)
    assert response.status_code == 200
    res = response.json()
    assert res["success"] is True
    assert len(res["data"]) > 0
    top_rec = res["data"][0]
    assert "personalization_score" in top_rec
    assert "why_recommended" in top_rec
    assert len(top_rec["why_recommended"]) > 0


def test_chat_copilot():
    payload = {
        "destination": "Udaipur",
        "message": "What is the expected weather and crowd in Udaipur?"
    }
    response = client.post("/api/chat", json=payload)
    assert response.status_code == 200
    res = response.json()
    assert res["success"] is True
    assert "reply" in res["data"]
    assert len(res["data"]["reply"]) > 10


def test_evaluation_summary():
    response = client.get("/api/evaluation/summary")
    assert response.status_code == 200
    res = response.json()
    assert res["success"] is True
    assert "recommender_ablation" in res["data"]
    assert "optimizer_benchmarks" in res["data"]
