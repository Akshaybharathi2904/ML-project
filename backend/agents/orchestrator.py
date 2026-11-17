from dataclasses import dataclass, field
from typing import Dict, Any, List, Optional
from datetime import datetime

from backend.agents.destination_agent import DestinationIntelligenceAgent
from backend.agents.weather_agent import WeatherIntelligenceAgent
from backend.agents.prediction_agent import PredictionAgent
from backend.agents.recommendation_agent import RecommendationAgent
from backend.agents.optimization_agent import OptimizationAgent
from backend.agents.analytics_agent import AnalyticsAgent
from backend.schemas.schemas import ItineraryGenerateRequest, ItineraryResponse


@dataclass
class TripContext:
    trip_id: str
    destination: str
    num_days: int
    budget: float
    pace: str
    transport: str
    interests: Dict[str, float]
    destination_meta: Dict[str, Any] = field(default_factory=dict)
    places: List[Dict[str, Any]] = field(default_factory=list)
    weather: Dict[str, Any] = field(default_factory=dict)
    predictions: Dict[str, Any] = field(default_factory=dict)
    recommendations: Dict[str, Any] = field(default_factory=dict)
    itinerary_response: Optional[ItineraryResponse] = None
    analytics: Dict[str, Any] = field(default_factory=dict)
    execution_logs: List[str] = field(default_factory=list)


class TripOrchestrator:
    """
    Lightweight Multi-Agent Orchestrator executing the 7-agent pipeline in sequence:
      1. Destination Intelligence Agent
      2. Weather Intelligence Agent
      3. Prediction Agent
      4. Recommendation Agent
      5. Optimization Agent
      6. Analytics Agent
    """

    def __init__(self):
        self.dest_agent = DestinationIntelligenceAgent()
        self.weather_agent = WeatherIntelligenceAgent()
        self.pred_agent = PredictionAgent()
        self.rec_agent = RecommendationAgent()
        self.opt_agent = OptimizationAgent()
        self.analytics_agent = AnalyticsAgent()

    async def run_pipeline(self, request: ItineraryGenerateRequest) -> TripContext:
        ctx = TripContext(
            trip_id=f"TRIP_{int(datetime.utcnow().timestamp())}_{request.destination.lower()[:4]}",
            destination=request.destination,
            num_days=request.num_days,
            budget=request.budget_inr,
            pace=request.pace,
            transport=request.transport,
            interests=request.interests
        )
        ctx.execution_logs.append(f"[{datetime.utcnow().strftime('%H:%M:%S')}] Orchestrator initialized for {request.destination} ({request.num_days} days).")

        # Step 1: Destination Intelligence
        dest_res = await self.dest_agent.execute(request.destination)
        ctx.destination_meta = dest_res["destination_meta"]
        ctx.places = dest_res["places"]
        ctx.execution_logs.append(f"[{datetime.utcnow().strftime('%H:%M:%S')}] Agent 1 (Destination Intelligence): Loaded {dest_res['total_places']} candidate places.")

        # Step 2: Weather Intelligence
        lat = ctx.destination_meta.get("lat", 24.5854)
        lon = ctx.destination_meta.get("lon", 73.7125)
        weather_res = await self.weather_agent.execute(lat, lon, num_days=request.num_days)
        ctx.weather = weather_res
        ctx.execution_logs.append(f"[{datetime.utcnow().strftime('%H:%M:%S')}] Agent 2 (Weather Intelligence): Forecast status: {weather_res['status']} (Suitability: {weather_res['average_suitability']}/100).")

        # Step 3: Prediction Agent
        pred_res = self.pred_agent.execute(request.destination, ctx.places, weather_res)
        ctx.predictions = pred_res
        ctx.execution_logs.append(f"[{datetime.utcnow().strftime('%H:%M:%S')}] Agent 3 (Prediction Agent): Generated crowd, cost, and disruption estimates.")

        # Step 4: Recommendation Agent
        rec_res = self.rec_agent.execute(
            destination=request.destination,
            user_interests=request.interests,
            budget_level="medium" if request.budget_inr <= 20000 else "luxury",
            pace=request.pace,
            seed_ratings=request.seed_ratings
        )
        ctx.recommendations = rec_res
        ctx.execution_logs.append(f"[{datetime.utcnow().strftime('%H:%M:%S')}] Agent 4 (Recommendation Agent): Scored {rec_res['count']} attractions via LightGBM hybrid model.")

        # Step 5: Optimization Agent
        itin_res = await self.opt_agent.execute(request)
        ctx.itinerary_response = itin_res
        ctx.execution_logs.append(f"[{datetime.utcnow().strftime('%H:%M:%S')}] Agent 5 (Optimization Agent): NSGA-II discovered {len(itin_res.pareto_solutions)} non-dominated Pareto plans in {itin_res.solver_info['runtime_seconds']}s.")

        # Step 6: Analytics Agent
        analytics_res = self.analytics_agent.execute(itin_res, request.budget_inr)
        ctx.analytics = analytics_res
        ctx.execution_logs.append(f"[{datetime.utcnow().strftime('%H:%M:%S')}] Agent 6 (Analytics Agent): Feasibility score {itin_res.feasibility_score}/100, Budget utilization {analytics_res['budget_utilization_pct']}%.")

        return ctx


orchestrator = TripOrchestrator()

