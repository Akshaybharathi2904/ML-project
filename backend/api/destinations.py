from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
from backend.services.destination_service import destination_service
from backend.schemas.schemas import DestinationItem, StandardResponse

router = APIRouter(prefix="/destinations", tags=["Destinations"])


@router.get("/search", response_model=StandardResponse)
async def search_destinations(q: str = Query("", description="Destination or state search query")):
    results = await destination_service.search_destinations(q)
    return StandardResponse(
        success=True,
        message=f"Found {len(results)} destination(s)",
        data=results,
        data_source="Curated Seed & Nominatim Geocoding"
    )


@router.get("/{destination_id}", response_model=StandardResponse)
def get_destination_details(destination_id: str):
    dest = destination_service.get_destination_by_id(destination_id)
    if not dest:
        raise HTTPException(status_code=404, detail="Destination not found")
    return StandardResponse(
        success=True,
        message="Destination details retrieved",
        data=dest,
        data_source="Curated Seed"
    )

