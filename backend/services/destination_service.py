import json
from pathlib import Path
from typing import List, Dict, Any, Optional
import httpx
from backend.config import settings


class DestinationService:
    def __init__(self):
        self.mock_file = settings.MOCK_DATA_DIR / "destinations.json"
        self._cached_destinations: List[Dict[str, Any]] = []
        self._load_mock_data()

    def _load_mock_data(self):
        if self.mock_file.exists():
            with open(self.mock_file, "r", encoding="utf-8") as f:
                self._cached_destinations = json.load(f)

    async def search_destinations(self, query: str = "") -> List[Dict[str, Any]]:
        """Search destinations matching query, supporting mock and geocoding."""
        query_norm = query.strip().lower()
        if not query_norm:
            return self._cached_destinations

        # Match from local curated seed
        matched = [
            d for d in self._cached_destinations
            if query_norm in d["name"].lower() or query_norm in d["state"].lower()
        ]
        if matched:
            return matched

        # If not mock-only, attempt Nominatim geocoding for any arbitrary Indian place
        if not settings.MOCK_MODE:
            try:
                async with httpx.AsyncClient(timeout=4.0) as client:
                    resp = await client.get(
                        "https://nominatim.openstreetmap.org/search",
                        params={"q": f"{query}, India", "format": "json", "limit": 1},
                        headers={"User-Agent": settings.USER_AGENT}
                    )
                    if resp.status_code == 200:
                        data = resp.json()
                        if data:
                            item = data[0]
                            return [{
                                "id": query_norm.replace(" ", "_"),
                                "name": item.get("display_name", query).split(",")[0],
                                "state": "India",
                                "lat": float(item["lat"]),
                                "lon": float(item["lon"]),
                                "best_season": "October to March",
                                "approx_daily_budget_inr": 3500.0,
                                "recommended_duration_days": 3,
                                "overview": f"Scenic destination in India ({item.get('display_name')})",
                                "image_url": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?w=800",
                                "data_source": "Nominatim Live Geocoding"
                            }]
            except Exception:
                pass

        # Fallback: return default destinations
        return self._cached_destinations[:6]

    def get_destination_by_id(self, dest_id: str) -> Optional[Dict[str, Any]]:
        dest_norm = dest_id.strip().lower()
        for d in self._cached_destinations:
            if d["id"] == dest_norm or d["name"].lower() == dest_norm:
                return d
        return None


destination_service = DestinationService()

