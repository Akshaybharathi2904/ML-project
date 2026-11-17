from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from backend.services.places_service import places_service
from backend.schemas.schemas import StandardResponse

router = APIRouter(prefix="/places", tags=["Places"])


@router.get("", response_model=StandardResponse)
def get_places(
    destination: str = Query("Udaipur", description="Destination name"),
    category: Optional[str] = Query(None, description="Category filter")
):
    places = places_service.get_places_for_destination(destination, category=category)
    return StandardResponse(
        success=True,
        message=f"Retrieved {len(places)} places",
        data=places,
        data_source="Curated Mock & Seed POIs"
    )


@router.get("/nearby", response_model=StandardResponse)
def get_nearby_places(
    lat: float = Query(..., description="Latitude"),
    lon: float = Query(..., description="Longitude"),
    radius_km: float = Query(25.0, description="Search radius in km")
):
    nearby = places_service.get_nearby_places(lat, lon, max_radius_km=radius_km)
    return StandardResponse(
        success=True,
        message=f"Found {len(nearby)} nearby places within {radius_km} km",
        data=nearby,
        data_source="Haversine Spatial Graph"
    )


@router.get("/{place_id}", response_model=StandardResponse)
def get_place(place_id: str):
    place = places_service.get_place_by_id(place_id)
    if not place:
        raise HTTPException(status_code=404, detail="Place not found")
    return StandardResponse(
        success=True,
        message="Place details retrieved",
        data=place,
        data_source=place.get("data_source", "curated_seed")
    )

