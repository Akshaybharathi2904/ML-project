import json
from pathlib import Path
from typing import List, Dict, Any, Optional
import httpx
from backend.config import settings
from src.utils.geo import haversine_distance_km


class PlacesService:
    def __init__(self):
        self.mock_file = settings.MOCK_DATA_DIR / "places.json"
        self._cached_places: List[Dict[str, Any]] = []
        self._load_mock_places()

    def _load_mock_places(self):
        if self.mock_file.exists():
            with open(self.mock_file, "r", encoding="utf-8") as f:
                self._cached_places = json.load(f)

    def get_places_for_destination(self, destination: str, category: Optional[str] = None) -> List[Dict[str, Any]]:
        dest_norm = destination.strip().lower()
        matched = [
            p for p in self._cached_places
            if p["destination_id"] == dest_norm or p["destination_name"].lower() == dest_norm
        ]
        
        # If destination not found in mock, fallback to places matching closest state or default Udaipur/Jaipur
        if not matched:
            matched = [p for p in self._cached_places if p["destination_id"] == "udaipur"]

        if category:
            matched = [p for p in matched if p["category"].lower() == category.lower()]

        return matched

    def get_place_by_id(self, place_id: str) -> Optional[Dict[str, Any]]:
        for p in self._cached_places:
            if p["id"] == place_id or p["name"].lower() == place_id.lower():
                return p
        return None

    def get_nearby_places(self, lat: float, lon: float, max_radius_km: float = 25.0) -> List[Dict[str, Any]]:
        nearby = []
        for p in self._cached_places:
            d = haversine_distance_km(lat, lon, p["lat"], p["lon"])
            if d <= max_radius_km:
                item = p.copy()
                item["distance_km"] = round(d, 2)
                nearby.append(item)
        nearby.sort(key=lambda x: x["distance_km"])
        return nearby


places_service = PlacesService()

