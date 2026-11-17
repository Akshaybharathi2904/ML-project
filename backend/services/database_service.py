from typing import Dict, Any, List, Optional
import copy
from backend.schemas.schemas import ItineraryResponse, ParetoSolutionSchema


class DatabaseService:
    """In-memory and persistent session cache for trips and versions."""

    def __init__(self):
        self._trips: Dict[str, ItineraryResponse] = {}
        self._versions: Dict[str, List[Dict[str, Any]]] = {}

    def save_trip(self, trip: ItineraryResponse):
        self._trips[trip.trip_id] = trip
        if trip.trip_id not in self._versions:
            self._versions[trip.trip_id] = []
        self._versions[trip.trip_id].append({
            "version_number": len(self._versions[trip.trip_id]) + 1,
            "itinerary": copy.deepcopy(trip.chosen_itinerary.model_dump()),
            "description": "Initial optimized plan",
            "feasibility": trip.feasibility_score
        })

    def get_trip(self, trip_id: str) -> Optional[ItineraryResponse]:
        return self._trips.get(trip_id)

    def get_versions(self, trip_id: str) -> List[Dict[str, Any]]:
        return self._versions.get(trip_id, [])

    def add_version(self, trip_id: str, itinerary: ParetoSolutionSchema, description: str, feasibility: float):
        if trip_id not in self._versions:
            self._versions[trip_id] = []
        self._versions[trip_id].append({
            "version_number": len(self._versions[trip_id]) + 1,
            "itinerary": copy.deepcopy(itinerary.model_dump()),
            "description": description,
            "feasibility": feasibility
        })


db_service = DatabaseService()

