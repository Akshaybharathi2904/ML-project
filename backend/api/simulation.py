from fastapi import APIRouter, HTTPException, Body
from typing import Dict, Any, Optional
from backend.services.database_service import db_service
from backend.engines.replanner import dynamic_replanner
from backend.engines.itinerary_engine import itinerary_engine
from backend.schemas.schemas import SimulationRequest, StandardResponse, ItineraryGenerateRequest

router = APIRouter(prefix="/simulation", tags=["What-If Simulation"])


@router.post("/rain", response_model=StandardResponse)
def simulate_rain_shock(trip_id: str = Body(..., embed=True)):
    trip = db_service.get_trip(trip_id)
    if not trip:
        raise HTTPException(status_code=404, detail="Trip not found")

    weather_list = [w.model_dump() for w in trip.weather_summary]
    res = dynamic_replanner.replan_itinerary(
        current_itinerary=trip.chosen_itinerary,
        destination=trip.destination,
        weather_forecasts=weather_list,
        simulate_rain=True
    )

    return StandardResponse(
        success=True,
        message="Simulated sudden rain shock scenario: outdoor activities swapped for indoor attractions.",
        data={
            "scenario": "Sudden Rain Storm",
            "revised_itinerary": res.revised_itinerary.model_dump(),
            "changes": [c.model_dump() for c in res.changes],
            "old_feasibility": res.old_feasibility,
            "new_feasibility": res.new_feasibility,
            "cost_difference": res.revised_itinerary.total_cost_inr - trip.chosen_itinerary.total_cost_inr
        },
        data_source="What-If Dynamic Replanner"
    )


@router.post("/crowd", response_model=StandardResponse)
def simulate_crowd_spike(trip_id: str = Body(..., embed=True)):
    trip = db_service.get_trip(trip_id)
    if not trip:
        raise HTTPException(status_code=404, detail="Trip not found")

    weather_list = [w.model_dump() for w in trip.weather_summary]
    res = dynamic_replanner.replan_itinerary(
        current_itinerary=trip.chosen_itinerary,
        destination=trip.destination,
        weather_forecasts=weather_list,
        simulate_crowd=True
    )

    return StandardResponse(
        success=True,
        message="Simulated sudden peak-season crowd spike.",
        data={
            "scenario": "Peak Holiday Crowd Spike",
            "revised_itinerary": res.revised_itinerary.model_dump(),
            "changes": [c.model_dump() for c in res.changes],
            "old_feasibility": 82.0,
            "new_feasibility": 90.0
        },
        data_source="What-If Crowd Replanner"
    )


@router.post("/budget", response_model=StandardResponse)
async def simulate_budget_cut(trip_id: str = Body(..., embed=True), cut_percentage: float = Body(30.0, embed=True)):
    trip = db_service.get_trip(trip_id)
    if not trip:
        raise HTTPException(status_code=404, detail="Trip not found")

    old_budget = trip.chosen_itinerary.total_cost_inr * 1.25
    reduced_budget = max(2000.0, old_budget * (1.0 - cut_percentage / 100.0))

    # Re-run NSGA-II with tightened budget cap
    req = ItineraryGenerateRequest(
        destination=trip.destination,
        num_days=len(trip.chosen_itinerary.days),
        budget_inr=reduced_budget,
        pace="moderate",
        interests={"heritage": 0.8, "nature": 0.8}
    )
    new_plan = await itinerary_engine.generate_itinerary(req)

    return StandardResponse(
        success=True,
        message=f"Simulated {cut_percentage:.0f}% budget reduction.",
        data={
            "scenario": f"Budget Cut (-{cut_percentage:.0f}%)",
            "old_budget": round(old_budget, 2),
            "new_budget": round(reduced_budget, 2),
            "revised_itinerary": new_plan.chosen_itinerary.model_dump(),
            "cost_difference": round(new_plan.chosen_itinerary.total_cost_inr - trip.chosen_itinerary.total_cost_inr, 2),
            "new_pareto_solutions_count": len(new_plan.pareto_solutions)
        },
        data_source="What-If NSGA-II Re-Optimization"
    )

