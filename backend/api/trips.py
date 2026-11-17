from fastapi import APIRouter, HTTPException, Body
from typing import Dict, Any, List
from backend.services.database_service import db_service
from backend.schemas.schemas import StandardResponse

router = APIRouter(prefix="/trips", tags=["Trips"])

saved_user_trips: Dict[str, Dict[str, Any]] = {}


@router.post("", response_model=StandardResponse)
def save_trip_bookmark(trip_id: str = Body(..., embed=True), name: str = Body("My Dream Vacation", embed=True)):
    trip = db_service.get_trip(trip_id)
    if not trip:
        raise HTTPException(status_code=404, detail="Trip not found")

    saved_user_trips[trip_id] = {
        "trip_id": trip_id,
        "name": name,
        "destination": trip.destination,
        "days": len(trip.chosen_itinerary.days),
        "total_cost": trip.chosen_itinerary.total_cost_inr,
        "feasibility": trip.feasibility_score,
        "itinerary": trip.chosen_itinerary.model_dump()
    }

    return StandardResponse(
        success=True,
        message=f"Trip '{name}' saved successfully",
        data=saved_user_trips[trip_id],
        data_source="Saved Trips Database"
    )


@router.get("", response_model=StandardResponse)
def list_saved_trips():
    return StandardResponse(
        success=True,
        message=f"Retrieved {len(saved_user_trips)} saved trip(s)",
        data=list(saved_user_trips.values()),
        data_source="Saved Trips Database"
    )


@router.get("/{trip_id}", response_model=StandardResponse)
def get_saved_trip(trip_id: str):
    item = saved_user_trips.get(trip_id)
    if not item:
        raise HTTPException(status_code=404, detail="Saved trip not found")
    return StandardResponse(
        success=True,
        message="Saved trip retrieved",
        data=item,
        data_source="Saved Trips Database"
    )


@router.delete("/{trip_id}", response_model=StandardResponse)
def delete_saved_trip(trip_id: str):
    if trip_id in saved_user_trips:
        del saved_user_trips[trip_id]
    return StandardResponse(
        success=True,
        message="Trip removed from saved list",
        data={"trip_id": trip_id},
        data_source="Saved Trips Database"
    )

