from fastapi import APIRouter, HTTPException, Body, Query
from typing import Dict, Any, Optional, List
from backend.engines.itinerary_engine import itinerary_engine
from backend.engines.replanner import dynamic_replanner, format_clock_min
from backend.services.database_service import db_service
from backend.services.places_service import places_service
from src.utils.geo import haversine_distance_km, compute_travel_time_minutes
from backend.schemas.schemas import (
    ItineraryGenerateRequest, ItineraryResponse, ParetoSolutionSchema,
    ItineraryReplanRequest, ReplanResponse, StandardResponse
)

router = APIRouter(prefix="/itinerary", tags=["Itinerary"])


@router.post("/generate", response_model=StandardResponse)
async def generate_itinerary(req: ItineraryGenerateRequest):
    res = await itinerary_engine.generate_itinerary(req)
    db_service.save_trip(res)
    return StandardResponse(
        success=True,
        message=f"Synthesized {len(res.pareto_solutions)} non-dominated Pareto plans via NSGA-II",
        data=res.model_dump(),
        data_source="NSGA-II Multi-Objective Itinerary Engine"
    )


@router.post("/select-solution", response_model=StandardResponse)
def select_pareto_solution(trip_id: str = Body(..., embed=True), solution_index: int = Body(..., embed=True)):
    trip = db_service.get_trip(trip_id)
    if not trip:
        raise HTTPException(status_code=404, detail="Trip not found")
    if solution_index < 0 or solution_index >= len(trip.pareto_solutions):
        raise HTTPException(status_code=400, detail="Invalid solution index")

    selected = trip.pareto_solutions[solution_index]
    trip.chosen_solution_index = solution_index
    trip.chosen_itinerary = selected
    db_service.add_version(trip_id, selected, f"Selected Pareto plan #{solution_index+1}", trip.feasibility_score)

    return StandardResponse(
        success=True,
        message=f"Selected Pareto plan #{solution_index + 1}",
        data=trip.model_dump(),
        data_source="Pareto Front Selector"
    )


@router.post("/replan", response_model=StandardResponse)
def replan_itinerary(req: ItineraryReplanRequest):
    trip = db_service.get_trip(req.trip_id)
    if not trip:
        raise HTTPException(status_code=404, detail="Trip not found")

    weather_list = [w.model_dump() for w in trip.weather_summary]
    replan_res = dynamic_replanner.replan_itinerary(
        current_itinerary=trip.chosen_itinerary,
        destination=req.destination or trip.destination,
        weather_forecasts=weather_list,
        simulate_rain=req.simulate_rain,
        simulate_crowd=req.simulate_crowd,
        new_budget=req.new_budget
    )

    # Save version
    trip.chosen_itinerary = replan_res.revised_itinerary
    trip.feasibility_score = replan_res.new_feasibility
    db_service.add_version(
        req.trip_id,
        replan_res.revised_itinerary,
        f"Dynamic replan ({len(replan_res.changes)} activities swapped)",
        replan_res.new_feasibility
    )

    return StandardResponse(
        success=True,
        message=replan_res.message,
        data=replan_res.model_dump(),
        data_source="Weather-Aware Dynamic Replanner"
    )


@router.post("/swap", response_model=StandardResponse)
def swap_activity(
    trip_id: str = Body(..., embed=True),
    day_number: int = Body(..., embed=True),
    old_place_id: str = Body(..., embed=True),
    new_place_id: str = Body(..., embed=True)
):
    trip = db_service.get_trip(trip_id)
    if not trip:
        raise HTTPException(status_code=404, detail="Trip not found")

    new_place = places_service.get_place_by_id(new_place_id)
    if not new_place:
        raise HTTPException(status_code=404, detail="Replacement place not found")

    itin = trip.chosen_itinerary
    swapped = False
    for day in itin.days:
        if day.day_number == day_number:
            for stop in day.stops:
                if stop.place_id == old_place_id:
                    stop.place_id = new_place["id"]
                    stop.place_name = new_place["name"]
                    stop.category = new_place["category"]
                    stop.cost_inr = new_place.get("avg_cost_inr", 100.0)
                    stop.is_indoor = new_place.get("is_indoor", False)
                    stop.why_recommended = ["Manually swapped by user."]
                    swapped = True
                    break

    if not swapped:
        raise HTTPException(status_code=400, detail="Place not found in specified day")

    db_service.add_version(trip_id, itin, f"Swapped activity for {new_place['name']}", trip.feasibility_score)

    return StandardResponse(
        success=True,
        message=f"Swapped activity for {new_place['name']}",
        data=trip.model_dump(),
        data_source="User Custom Activity Swap"
    )


@router.post("/optimize-route", response_model=StandardResponse)
def optimize_route(trip_id: str = Body(..., embed=True), day_number: int = Body(..., embed=True)):
    trip = db_service.get_trip(trip_id)
    if not trip:
        raise HTTPException(status_code=404, detail="Trip not found")

    itin = trip.chosen_itinerary
    target_day = None
    for day in itin.days:
        if day.day_number == day_number:
            target_day = day
            break

    if not target_day:
        raise HTTPException(status_code=404, detail=f"Day {day_number} not found in itinerary")

    stops = target_day.stops
    if len(stops) > 2:
        # Nearest neighbor TSP on attraction geo-coordinates
        unvisited = list(range(1, len(stops)))
        ordered_indices = [0]
        curr = 0
        while unvisited:
            best_idx = None
            best_dist = float('inf')
            for cand in unvisited:
                d = haversine_distance_km(stops[curr].lat, stops[curr].lon, stops[cand].lat, stops[cand].lon)
                if d < best_dist:
                    best_dist = d
                    best_idx = cand
            ordered_indices.append(best_idx)
            unvisited.remove(best_idx)
            curr = best_idx

        target_day.stops = [stops[i] for i in ordered_indices]

    # Recalculate transit times, distances, arrival and departure times
    current_clock = 540.0  # 09:00 AM start
    for idx, stop in enumerate(target_day.stops):
        if idx == 0:
            stop.travel_time_from_prev_min = 0.0
            stop.travel_distance_km = 0.0
        else:
            prev = target_day.stops[idx - 1]
            dist = haversine_distance_km(prev.lat, prev.lon, stop.lat, stop.lon)
            transit_min = compute_travel_time_minutes(dist)
            stop.travel_distance_km = round(dist, 1)
            stop.travel_time_from_prev_min = round(transit_min, 1)
            current_clock += transit_min

        stop.arrival_time = format_clock_min(current_clock)
        dur = stop.visit_duration_min or 90.0
        current_clock += dur
        stop.departure_time = format_clock_min(current_clock)

        # Assign slot
        if current_clock < 720:
            stop.slot = "Morning"
        elif current_clock < 1020:
            stop.slot = "Afternoon"
        else:
            stop.slot = "Evening"

    target_day.total_travel_time_min = round(sum(s.travel_time_from_prev_min for s in target_day.stops), 1)
    itin.total_travel_time_min = round(sum(d.total_travel_time_min for d in itin.days), 1)

    db_service.add_version(trip_id, itin, f"Route order optimized for Day {day_number}", trip.feasibility_score)

    return StandardResponse(
        success=True,
        message=f"Optimized visiting route order for Day {day_number}. Total transit time reduced to {target_day.total_travel_time_min} mins.",
        data=trip.model_dump(),
        data_source="TSP Nearest-Neighbor Route Optimizer"
    )


@router.post("/remove-stop", response_model=StandardResponse)
def remove_stop_from_itinerary(
    trip_id: str = Body(..., embed=True),
    day_number: int = Body(..., embed=True),
    place_id: str = Body(..., embed=True)
):
    trip = db_service.get_trip(trip_id)
    if not trip:
        raise HTTPException(status_code=404, detail="Trip not found")

    itin = trip.chosen_itinerary
    removed_name = ""
    for day in itin.days:
        if day.day_number == day_number:
            new_stops = []
            for s in day.stops:
                if s.place_id == place_id:
                    removed_name = s.place_name
                else:
                    new_stops.append(s)
            day.stops = new_stops

            # Recalculate day times
            current_clock = 540.0
            for idx, stop in enumerate(day.stops):
                if idx == 0:
                    stop.travel_time_from_prev_min = 0.0
                    stop.travel_distance_km = 0.0
                else:
                    prev = day.stops[idx - 1]
                    dist = haversine_distance_km(prev.lat, prev.lon, stop.lat, stop.lon)
                    transit_min = compute_travel_time_minutes(dist)
                    stop.travel_distance_km = round(dist, 1)
                    stop.travel_time_from_prev_min = round(transit_min, 1)
                    current_clock += transit_min

                stop.arrival_time = format_clock_min(current_clock)
                dur = stop.visit_duration_min or 90.0
                current_clock += dur
                stop.departure_time = format_clock_min(current_clock)

            day.total_travel_time_min = round(sum(s.travel_time_from_prev_min for s in day.stops), 1)
            day.total_cost_inr = round(sum(s.cost_inr for s in day.stops), 2)
            break

    total_cost = sum(s.cost_inr for d in itin.days for s in d.stops)
    itin.total_cost_inr = round(total_cost, 2)
    itin.total_travel_time_min = round(sum(d.total_travel_time_min for d in itin.days), 1)

    db_service.add_version(trip_id, itin, f"Removed stop: {removed_name}", trip.feasibility_score)

    return StandardResponse(
        success=True,
        message=f"Removed {removed_name or place_id} from Day {day_number}",
        data=trip.model_dump(),
        data_source="Itinerary Customizer"
    )


@router.get("/{trip_id}/budget-breakdown", response_model=StandardResponse)
def get_budget_breakdown(trip_id: str, budget_cap: Optional[float] = Query(None)):
    trip = db_service.get_trip(trip_id)
    if not trip:
        raise HTTPException(status_code=404, detail="Trip not found")

    itin = trip.chosen_itinerary
    num_days = max(1, len(itin.days))
    tickets_cost = round(sum(s.cost_inr for d in itin.days for s in d.stops), 2)

    # Transit estimate: sum of km * ₹15/km + ₹250 daily base
    total_km = sum(s.travel_distance_km for d in itin.days for s in d.stops)
    transit_cost = round(total_km * 15.0 + (num_days * 250.0), 2)

    # Accommodation estimate: ₹2200 per night
    accommodation_cost = round(max(1, num_days - 1) * 2200.0, 2)

    # Food estimate: ₹700 per day
    food_cost = round(num_days * 700.0, 2)

    # Shopping and misc allowance
    shopping_cost = 1200.0

    total_est = round(tickets_cost + transit_cost + accommodation_cost + food_cost + shopping_cost, 2)
    user_budget = budget_cap if budget_cap is not None else 15000.0

    is_exceeded = total_est > user_budget
    utilization_pct = round((total_est / max(1.0, user_budget)) * 100.0, 1)

    warnings = []
    if is_exceeded:
        diff = round(total_est - user_budget, 2)
        warnings.append(f"Budget Exceeded by ₹{diff:,}! Consider selecting economy stays or switching taxi transfers to public transit.")
    elif utilization_pct > 88.0:
        warnings.append(f"High Budget Utilization ({utilization_pct}%). You have only ₹{round(user_budget - total_est, 2):,} remaining contingency buffer.")

    categories = [
        {"name": "Accommodation (Stays)", "cost_inr": accommodation_cost, "percentage": round((accommodation_cost / total_est) * 100, 1), "color": "#38bdf8"},
        {"name": "Food & Dining", "cost_inr": food_cost, "percentage": round((food_cost / total_est) * 100, 1), "color": "#f59e0b"},
        {"name": "Transportation & Transit", "cost_inr": transit_cost, "percentage": round((transit_cost / total_est) * 100, 1), "color": "#14b8a6"},
        {"name": "Attraction Tickets & Fees", "cost_inr": tickets_cost, "percentage": round((tickets_cost / total_est) * 100, 1), "color": "#10b981"},
        {"name": "Shopping & Souvenirs", "cost_inr": shopping_cost, "percentage": round((shopping_cost / total_est) * 100, 1), "color": "#a855f7"},
    ]

    return StandardResponse(
        success=True,
        message="Comprehensive budget breakdown synthesized",
        data={
            "trip_id": trip_id,
            "destination": trip.destination,
            "num_days": num_days,
            "user_budget_inr": user_budget,
            "total_estimated_inr": total_est,
            "budget_remaining_inr": round(user_budget - total_est, 2),
            "utilization_percentage": utilization_pct,
            "is_budget_exceeded": is_exceeded,
            "warnings": warnings,
            "categories": categories
        },
        data_source="Predictive Budget Optimization Service"
    )


@router.get("/{trip_id}", response_model=StandardResponse)
def get_itinerary(trip_id: str):
    trip = db_service.get_trip(trip_id)
    if not trip:
        raise HTTPException(status_code=404, detail="Trip not found")
    return StandardResponse(
        success=True,
        message="Itinerary retrieved",
        data=trip.model_dump(),
        data_source="Database Session Store"
    )


@router.get("/{trip_id}/versions", response_model=StandardResponse)
def get_versions(trip_id: str):
    versions = db_service.get_versions(trip_id)
    return StandardResponse(
        success=True,
        message=f"Retrieved {len(versions)} itinerary versions",
        data=versions,
        data_source="Itinerary Version History"
    )

