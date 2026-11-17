import pytest
from fastapi.testclient import TestClient
from backend.main import app
from backend.schemas.schemas import ItineraryGenerateRequest
from backend.services.database_service import db_service

client = TestClient(app)


def test_shap_explanation_endpoint():
    """Test Feature 4: SHAP feature attribution endpoint."""
    res = client.get("/api/recommend/explain/PLC_0001?destination=Udaipur")
    assert res.status_code == 200
    json_data = res.json()
    assert json_data["success"] is True
    data = json_data["data"]
    assert "features_breakdown" in data
    assert "feature_impact" in data
    assert len(data["features_breakdown"]) > 0
    # Verify positive and negative directions
    directions = [f["direction"] for f in data["features_breakdown"]]
    assert "positive" in directions


def test_budget_breakdown_endpoint():
    """Test Feature 3: Category-wise budget breakdown."""
    # First generate an itinerary
    req_payload = {
        "destination": "Udaipur",
        "start_date": "2026-11-05",
        "num_days": 3,
        "budget_inr": 18000,
        "pace": "moderate",
        "transport": "taxi",
        "travelers_count": 2,
        "interests": {"heritage": 0.9, "nature": 0.8}
    }
    gen_res = client.post("/api/itinerary/generate", json=req_payload)
    assert gen_res.status_code == 200
    trip_id = gen_res.json()["data"]["trip_id"]

    # Now get budget breakdown
    b_res = client.get(f"/api/itinerary/{trip_id}/budget-breakdown?budget_cap=18000")
    assert b_res.status_code == 200
    b_data = b_res.json()["data"]
    assert "categories" in b_data
    assert len(b_data["categories"]) == 5
    cat_names = [c["name"] for c in b_data["categories"]]
    assert any("Accommodation" in n for n in cat_names)
    assert any("Food" in n for n in cat_names)
    assert any("Transportation" in n for n in cat_names)
    assert any("Attraction" in n for n in cat_names)
    assert any("Shopping" in n for n in cat_names)
    assert b_data["total_estimated_inr"] > 0


def test_route_optimization_endpoint():
    """Test Feature 2: Route optimization and reordering."""
    req_payload = {
        "destination": "Udaipur",
        "start_date": "2026-11-05",
        "num_days": 2,
        "budget_inr": 15000,
        "pace": "moderate",
        "interests": {"heritage": 0.9}
    }
    gen_res = client.post("/api/itinerary/generate", json=req_payload)
    trip_id = gen_res.json()["data"]["trip_id"]

    opt_res = client.post("/api/itinerary/optimize-route", json={"trip_id": trip_id, "day_number": 1})
    assert opt_res.status_code == 200
    assert opt_res.json()["success"] is True
    assert "Optimized visiting route" in opt_res.json()["message"]


def test_crowd_prediction_with_alternatives():
    """Test Feature 9: Crowd prediction with serene alternatives."""
    res = client.get("/api/predictions/crowd/place/PLC_0001?destination=Udaipur&hour=14")
    assert res.status_code == 200
    data = res.json()["data"]
    assert "prediction" in data
    assert "category" in data["prediction"]
    assert "alternatives" in data
    assert "evaluation_metrics" in data
    assert data["evaluation_metrics"]["r2_score"] == 0.950


def test_user_profile_and_ratings():
    """Test Feature 10: User profile, ratings, and travel history."""
    # Login/register
    login_res = client.post("/api/users/auth/login", json={"username": "Priya_Traveler"})
    assert login_res.status_code == 200
    user_data = login_res.json()["data"]
    user_id = user_data["user_id"]
    assert user_id.startswith("USR_")

    # Update preferences
    pref_res = client.put(f"/api/users/profile/{user_id}", json={
        "budget_level": "luxury",
        "pace_preference": "relaxed",
        "preferences": {"nature": 0.95, "wildlife": 0.85}
    })
    assert pref_res.status_code == 200
    assert pref_res.json()["data"]["budget_level"] == "luxury"

    # Submit rating for cold-start collaborative filtering
    rate_res = client.post("/api/users/ratings", json={
        "user_id": user_id,
        "place_id": "PLC_0001",
        "rating": 5.0,
        "feedback": "Magnificent palace architecture!"
    })
    assert rate_res.status_code == 200
    assert rate_res.json()["success"] is True

    # Retrieve ratings
    get_rates = client.get(f"/api/users/ratings/{user_id}")
    assert get_rates.status_code == 200
    assert len(get_rates.json()["data"]) >= 1


def test_copilot_natural_language_actions():
    """Test Feature 8: AI Copilot natural language itinerary modifications."""
    chat_res = client.post("/api/chat", json={
        "destination": "Udaipur",
        "message": "Can you remove an attraction from my plan?"
    })
    assert chat_res.status_code == 200
    resp_data = chat_res.json()["data"]
    assert resp_data["proposed_changes"] is not None
    assert any(c["action"] == "remove_stop" for c in resp_data["proposed_changes"])
