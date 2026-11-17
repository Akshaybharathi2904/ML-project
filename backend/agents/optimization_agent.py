from typing import Dict, Any, Optional
from backend.engines.itinerary_engine import itinerary_engine
from backend.schemas.schemas import ItineraryGenerateRequest, ItineraryResponse


class OptimizationAgent:
    """Agent 5: Performs Team Orienteering NSGA-II Multi-Objective Optimization returning the Pareto front."""

    async def execute(self, request: ItineraryGenerateRequest) -> ItineraryResponse:
        return await itinerary_engine.generate_itinerary(request)

