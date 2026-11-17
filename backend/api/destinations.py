from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
from backend.services.destination_service import destination_service
from backend.schemas.schemas import DestinationItem, StandardResponse

router = APIRouter(prefix="/destinations", tags=["Destinations"])


@router.get("/states", response_model=StandardResponse)
async def get_states():
    """Return all states and UTs with destination counts."""
    states = destination_service.get_states()
    return StandardResponse(
        success=True,
        message=f"Found {len(states)} states and union territories",
        data=states,
        data_source="Curated Seed"
    )


@router.get("/categories", response_model=StandardResponse)
async def get_categories():
    """Return all destination categories with counts."""
    cats = destination_service.get_categories()
    return StandardResponse(
        success=True,
        message=f"Found {len(cats)} categories",
        data=cats,
        data_source="Curated Seed"
    )


@router.get("/popular", response_model=StandardResponse)
async def get_popular_destinations(limit: int = Query(20, ge=1, le=100)):
    """Return popular destinations."""
    dests = destination_service.get_popular_destinations(limit=limit)
    return StandardResponse(
        success=True,
        message=f"Found {len(dests)} popular destinations",
        data=dests,
        data_source="Curated Seed"
    )


@router.get("/search", response_model=StandardResponse)
async def search_destinations(
    q: str = Query("", description="Search by name, state, or attractions"),
    state: str = Query("", description="Filter by state or union territory"),
    category: str = Query("", description="Filter by destination category"),
    sort_by: str = Query("name_asc", description="Sort: name_asc, name_desc, budget_asc, budget_desc, duration_asc, duration_desc"),
    limit: int = Query(500, ge=1, le=1000),
    offset: int = Query(0, ge=0)
):
    """Search and filter destinations with pagination."""
    results, total = await destination_service.search_destinations(
        query=q,
        state=state,
        category=category,
        sort_by=sort_by,
        limit=limit,
        offset=offset
    )
    return StandardResponse(
        success=True,
        message=f"Found {total} destination(s)",
        data={"destinations": results, "total": total, "offset": offset, "limit": limit},
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
