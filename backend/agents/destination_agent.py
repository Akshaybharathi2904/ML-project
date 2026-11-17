from typing import Dict, Any, List
from backend.services.destination_service import destination_service
from backend.services.places_service import places_service


class DestinationIntelligenceAgent:
    """Agent 1: Resolves destination geocoding, retrieves curated attractions and geographic profiles."""

    async def execute(self, destination: str) -> Dict[str, Any]:
        dest_info = destination_service.get_destination_by_id(destination)
        if not dest_info:
            searched = await destination_service.search_destinations(destination)
            dest_info = searched[0] if searched else {
                "id": destination.lower().replace(" ", "_"),
                "name": destination,
                "state": "India",
                "lat": 24.5854,
                "lon": 73.7125,
                "best_season": "October to March",
                "approx_daily_budget_inr": 3500.0,
                "recommended_duration_days": 3,
                "overview": f"Curated destination: {destination}",
                "image_url": "https://images.unsplash.com/photo-1599661046289-e31897846e41?w=800"
            }

        places = places_service.get_places_for_destination(dest_info.get("name", destination))
        return {
            "destination_meta": dest_info,
            "places": places,
            "total_places": len(places)
        }

