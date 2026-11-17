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
                raw = json.load(f)
                # Normalize each record so both old and new field names work
                self._cached_destinations = [self._normalize(d) for d in raw]

    def _normalize(self, d: Dict[str, Any]) -> Dict[str, Any]:
        """Ensure backward-compatible aliases exist alongside extended fields."""
        # Alias: id <-> destination_id, name <-> destination_name, state <-> state_or_union_territory
        if "destination_id" in d and "id" not in d:
            d["id"] = d["destination_id"]
        elif "id" in d and "destination_id" not in d:
            d["destination_id"] = d["id"]

        if "destination_name" in d and "name" not in d:
            d["name"] = d["destination_name"]
        elif "name" in d and "destination_name" not in d:
            d["destination_name"] = d["name"]

        if "state_or_union_territory" in d and "state" not in d:
            d["state"] = d["state_or_union_territory"]
        elif "state" in d and "state_or_union_territory" not in d:
            d["state_or_union_territory"] = d["state"]

        if "overview" in d and "best_visiting_season" not in d:
            d["best_visiting_season"] = d.get("best_season", "")
        elif "best_visiting_season" in d and "best_season" not in d:
            d["best_season"] = d["best_visiting_season"]

        # Ensure required numeric fields
        d.setdefault("approx_daily_budget_inr", 3500.0)
        d.setdefault("recommended_duration_days", 3)
        d.setdefault("lat", 20.5937)
        d.setdefault("lon", 78.9629)
        d.setdefault("overview", d.get("description", "A beautiful Indian destination."))
        d.setdefault("best_season", "October to March")
        d.setdefault("destination_category", "General")

        return d

    def get_all_destinations(self) -> List[Dict[str, Any]]:
        return self._cached_destinations

    async def search_destinations(
        self,
        query: str = "",
        state: str = "",
        category: str = "",
        sort_by: str = "name_asc",
        limit: int = 500,
        offset: int = 0
    ) -> List[Dict[str, Any]]:
        """Search destinations with filtering and sorting."""
        query_norm = query.strip().lower()
        state_norm = state.strip().lower()
        category_norm = category.strip().lower()

        results = self._cached_destinations

        # Text search across name, state, overview, attractions
        if query_norm:
            def _matches(d: Dict[str, Any]) -> bool:
                if query_norm in d.get("name", "").lower():
                    return True
                if query_norm in d.get("state", "").lower():
                    return True
                if query_norm in d.get("overview", "").lower():
                    return True
                if query_norm in d.get("destination_category", "").lower():
                    return True
                attractions = d.get("popular_attractions", [])
                if any(query_norm in a.lower() for a in attractions):
                    return True
                return False
            results = [d for d in results if _matches(d)]

        # State filter
        if state_norm and state_norm != "all":
            results = [
                d for d in results
                if state_norm in d.get("state", "").lower()
                or state_norm in d.get("state_or_union_territory", "").lower()
            ]

        # Category filter
        if category_norm and category_norm != "all":
            results = [
                d for d in results
                if category_norm in d.get("destination_category", "").lower()
            ]

        # Sorting
        if sort_by == "name_asc":
            results = sorted(results, key=lambda x: x.get("name", ""))
        elif sort_by == "name_desc":
            results = sorted(results, key=lambda x: x.get("name", ""), reverse=True)
        elif sort_by == "budget_asc":
            results = sorted(results, key=lambda x: x.get("approx_daily_budget_inr", 0))
        elif sort_by == "budget_desc":
            results = sorted(results, key=lambda x: x.get("approx_daily_budget_inr", 0), reverse=True)
        elif sort_by == "duration_asc":
            results = sorted(results, key=lambda x: x.get("recommended_duration_days", 0))
        elif sort_by == "duration_desc":
            results = sorted(results, key=lambda x: x.get("recommended_duration_days", 0), reverse=True)

        total = len(results)
        paged = results[offset: offset + limit]
        return paged, total

    def get_states(self) -> List[Dict[str, Any]]:
        """Return all states/UTs with destination counts."""
        state_map: Dict[str, Dict[str, Any]] = {}
        for d in self._cached_destinations:
            state = d.get("state", "Unknown")
            is_ut = d.get("is_union_territory", False)
            if state not in state_map:
                state_map[state] = {
                    "state": state,
                    "is_union_territory": is_ut,
                    "destination_count": 0
                }
            state_map[state]["destination_count"] += 1
        return sorted(state_map.values(), key=lambda x: x["state"])

    def get_categories(self) -> List[Dict[str, Any]]:
        """Return all destination categories with counts."""
        cat_map: Dict[str, int] = {}
        for d in self._cached_destinations:
            cat = d.get("destination_category", "General")
            cat_map[cat] = cat_map.get(cat, 0) + 1
        return sorted(
            [{"category": k, "destination_count": v} for k, v in cat_map.items()],
            key=lambda x: x["destination_count"],
            reverse=True
        )

    def get_destination_by_id(self, dest_id: str) -> Optional[Dict[str, Any]]:
        dest_norm = dest_id.strip().lower()
        for d in self._cached_destinations:
            if d.get("id", "").lower() == dest_norm:
                return d
            if d.get("destination_id", "").lower() == dest_norm:
                return d
            if d.get("name", "").lower() == dest_norm:
                return d
        return None

    def get_popular_destinations(self, limit: int = 20) -> List[Dict[str, Any]]:
        """Return popular destinations (highest budget = more tourist infrastructure)."""
        return sorted(
            self._cached_destinations,
            key=lambda x: x.get("approx_daily_budget_inr", 0),
            reverse=True
        )[:limit]


destination_service = DestinationService()
