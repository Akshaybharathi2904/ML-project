from fastapi import APIRouter, HTTPException
from backend.services.database_service import db_service
from backend.agents.analytics_agent import AnalyticsAgent
from backend.schemas.schemas import StandardResponse

router = APIRouter(prefix="/analytics", tags=["Analytics"])
analytics_agent = AnalyticsAgent()


@router.get("/{trip_id}", response_model=StandardResponse)
def get_trip_analytics(trip_id: str):
    trip = db_service.get_trip(trip_id)
    if not trip:
        raise HTTPException(status_code=404, detail="Trip not found")

    res = analytics_agent.execute(trip, budget_inr=trip.chosen_itinerary.total_cost_inr * 1.3)
    return StandardResponse(
        success=True,
        message="Analytics computed",
        data=res,
        data_source="Analytics Agent Multi-Factor Synthesizer"
    )

