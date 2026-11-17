from fastapi import APIRouter, Body, HTTPException
from typing import Dict, Any, List
from backend.agents.copilot_agent import copilot_agent
from backend.services.database_service import db_service
from backend.schemas.schemas import ChatMessageRequest, ChatMessageResponse, StandardResponse

router = APIRouter(prefix="/chat", tags=["Trip Copilot Chatbot"])

chat_history_store: Dict[str, List[Dict[str, Any]]] = {}


@router.post("", response_model=StandardResponse)
async def chat_with_copilot(req: ChatMessageRequest):
    trip_ctx = None
    if req.trip_id:
        trip = db_service.get_trip(req.trip_id)
        if trip:
            trip_ctx = trip.model_dump()

    response: ChatMessageResponse = await copilot_agent.execute(
        message=req.message,
        destination=req.destination,
        trip_context=trip_ctx
    )

    # Record history
    sid = req.trip_id or "default_session"
    if sid not in chat_history_store:
        chat_history_store[sid] = []
    chat_history_store[sid].append({"role": "user", "content": req.message})
    chat_history_store[sid].append({"role": "assistant", "content": response.reply, "tools": response.tool_calls_executed})

    return StandardResponse(
        success=True,
        message="Copilot reply generated",
        data=response.model_dump(),
        data_source=response.data_source
    )


@router.get("/{trip_id}/history", response_model=StandardResponse)
def get_chat_history(trip_id: str):
    history = chat_history_store.get(trip_id, [])
    return StandardResponse(
        success=True,
        message=f"Retrieved {len(history)} messages",
        data=history,
        data_source="Chat Session History"
    )


@router.post("/apply-action", response_model=StandardResponse)
def apply_copilot_action(
    trip_id: str = Body(..., embed=True),
    action: str = Body(..., embed=True),
    parameters: Dict[str, Any] = Body(default_factory=dict, embed=True)
):
    trip = db_service.get_trip(trip_id)
    if not trip:
        raise HTTPException(status_code=404, detail="Trip not found")

    itin = trip.chosen_itinerary

    if action == "remove_stop":
        place_id = parameters.get("place_id")
        for day in itin.days:
            day.stops = [s for s in day.stops if s.place_id != place_id]
        total_cost = sum(s.cost_inr for d in itin.days for s in d.stops)
        itin.total_cost_inr = round(total_cost, 2)
        db_service.add_version(trip_id, itin, f"Copilot action: removed stop {place_id}", trip.feasibility_score)

    elif action == "weather_replan":
        from backend.engines.replanner import dynamic_replanner
        weather_list = [w.model_dump() for w in trip.weather_summary]
        res = dynamic_replanner.replan_itinerary(
            current_itinerary=trip.chosen_itinerary,
            destination=trip.destination,
            weather_forecasts=weather_list,
            simulate_rain=True
        )
        trip.chosen_itinerary = res.revised_itinerary
        trip.feasibility_score = res.new_feasibility
        db_service.add_version(trip_id, res.revised_itinerary, "Copilot action: weather replan applied", res.new_feasibility)

    elif action == "reduce_budget":
        for day in itin.days:
            for s in day.stops:
                if s.cost_inr > 200:
                    s.cost_inr = round(s.cost_inr * 0.75, 2)
        total_cost = sum(s.cost_inr for d in itin.days for s in d.stops)
        itin.total_cost_inr = round(total_cost, 2)
        db_service.add_version(trip_id, itin, "Copilot action: budget reduced by 25%", trip.feasibility_score)

    elif action == "add_stop":
        from backend.services.places_service import places_service
        from backend.schemas.schemas import ItineraryStopSchema
        from src.utils.geo import haversine_distance_km, compute_travel_time_minutes
        place_id = parameters.get("place_id", "PLC_0004")
        p_info = places_service.get_place_by_id(place_id)
        if p_info and len(itin.days) > 0:
            target_day = itin.days[0]
            new_stop = ItineraryStopSchema(
                place_id=p_info["id"],
                place_name=p_info["name"],
                category=p_info["category"],
                city=trip.destination,
                lat=p_info["lat"],
                lon=p_info["lon"],
                arrival_time="04:30 PM",
                departure_time="06:00 PM",
                slot="Afternoon",
                visit_duration_min=p_info.get("avg_visit_duration_min", 90.0),
                travel_time_from_prev_min=15.0,
                travel_distance_km=3.5,
                cost_inr=p_info.get("avg_cost_inr", 100.0),
                crowd_forecast=p_info.get("crowd_level", 0.4),
                disruption_risk="Low",
                is_indoor=p_info.get("is_indoor", False),
                personalization_score=0.92,
                why_recommended=["Added via AI Travel Copilot natural-language instruction."]
            )
            target_day.stops.append(new_stop)
            target_day.total_cost_inr = round(sum(s.cost_inr for s in target_day.stops), 2)
            total_cost = sum(s.cost_inr for d in itin.days for s in d.stops)
            itin.total_cost_inr = round(total_cost, 2)
            db_service.add_version(trip_id, itin, f"Copilot action: added {p_info['name']}", trip.feasibility_score)

    return StandardResponse(
        success=True,
        message=f"Applied copilot action: {action}",
        data=trip.model_dump(),
        data_source="AI Travel Copilot Execution Service"
    )

