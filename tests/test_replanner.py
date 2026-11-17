import pytest
from backend.engines.replanner import dynamic_replanner
from backend.schemas.schemas import ParetoSolutionSchema, ItineraryDaySchema, ItineraryStopSchema


@pytest.fixture
def sample_outdoor_itinerary():
    stop1 = ItineraryStopSchema(
        place_id="PLC_0002",
        place_name="Lake Pichola Boating",
        category="nature",
        city="Udaipur",
        lat=24.5765,
        lon=73.6805,
        arrival_time="10:00",
        departure_time="11:30",
        visit_duration_min=90,
        travel_time_from_prev_min=0,
        travel_distance_km=0.0,
        cost_inr=500.0,
        crowd_forecast=0.6,
        disruption_risk="High (Outdoor)",
        is_indoor=False,
        personalization_score=0.92,
        why_recommended=["Iconic scenic lake view"]
    )
    stop2 = ItineraryStopSchema(
        place_id="PLC_0001",
        place_name="City Palace",
        category="heritage",
        city="Udaipur",
        lat=24.5764,
        lon=73.6835,
        arrival_time="12:00",
        departure_time="14:00",
        visit_duration_min=120,
        travel_time_from_prev_min=10,
        travel_distance_km=1.2,
        cost_inr=300.0,
        crowd_forecast=0.8,
        disruption_risk="Medium",
        is_indoor=True,
        personalization_score=0.95,
        why_recommended=["Historic royal museum"]
    )

    day1 = ItineraryDaySchema(
        day_number=1,
        date="2026-11-05",
        stops=[stop1, stop2],
        total_travel_time_min=10,
        total_visit_time_min=210,
        total_cost_inr=800.0,
        feasibility=88.0
    )

    return ParetoSolutionSchema(
        solution_index=0,
        total_score=1.87,
        total_cost_inr=800.0,
        total_travel_time_min=10,
        category_diversity=0.8,
        avg_crowd_level=0.7,
        total_places=2,
        is_knee_point=True,
        days=[day1]
    )


def test_replanner_rain_shock_substitutes_outdoor(sample_outdoor_itinerary):
    forecasts = [{"date": "2026-11-05", "rain_probability_pct": 85.0}]
    
    result = dynamic_replanner.replan_itinerary(
        current_itinerary=sample_outdoor_itinerary,
        destination="Udaipur",
        weather_forecasts=forecasts,
        simulate_rain=True
    )

    assert result is not None
    assert len(result.changes) >= 1
    # Check that Lake Pichola Boating (outdoor) was replaced
    changed_original = [c.original_place for c in result.changes]
    assert "Lake Pichola Boating" in changed_original

    # Verify revised stop has is_indoor = True
    day1_stops = result.revised_itinerary.days[0].stops
    lake_stop = day1_stops[0]
    assert lake_stop.is_indoor is True
    assert lake_stop.disruption_risk.startswith("Low")
    assert result.new_feasibility >= result.old_feasibility


def test_replanner_no_rain_preserves_itinerary(sample_outdoor_itinerary):
    forecasts = [{"date": "2026-11-05", "rain_probability_pct": 10.0}]
    
    result = dynamic_replanner.replan_itinerary(
        current_itinerary=sample_outdoor_itinerary,
        destination="Udaipur",
        weather_forecasts=forecasts,
        simulate_rain=False
    )

    assert len(result.changes) == 0
    assert result.revised_itinerary.days[0].stops[0].place_name == "Lake Pichola Boating"

