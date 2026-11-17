from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field


class StandardResponse(BaseModel):
    success: bool = True
    message: str = "Success"
    data: Optional[Any] = None
    data_source: str = "local"


class DestinationItem(BaseModel):
    # Core fields (backward compatible)
    id: str
    name: str
    state: str
    lat: float
    lon: float
    best_season: str
    approx_daily_budget_inr: float
    recommended_duration_days: int
    overview: str
    image_url: Optional[str] = None
    # Extended fields for 314-destination dataset
    destination_id: Optional[str] = None
    destination_name: Optional[str] = None
    state_or_union_territory: Optional[str] = None
    is_union_territory: Optional[bool] = None
    destination_category: Optional[str] = None
    popular_attractions: Optional[List[str]] = None
    nearby_places: Optional[List[str]] = None
    recommended_activities: Optional[List[str]] = None
    best_visiting_season: Optional[str] = None
    image_source: Optional[str] = None
    photographer_name: Optional[str] = None
    photographer_profile_url: Optional[str] = None
    image_license: Optional[str] = None
    image_source_page: Optional[str] = None
    data_source: Optional[str] = None


class StateItem(BaseModel):
    state: str
    is_union_territory: bool = False
    destination_count: int


class CategoryItem(BaseModel):
    category: str
    destination_count: int


class PlaceItem(BaseModel):
    id: str
    name: str
    destination: str
    state: Optional[str] = None
    country_code: str = "IN"
    lat: float
    lon: float
    category: str
    avg_cost_inr: float = 0.0
    avg_visit_duration_min: float = 60.0
    rating: float = 4.0
    popularity: float = 0.5
    crowd_level: float = 0.5
    open_time: str = "09:00"
    close_time: str = "18:00"
    is_indoor: bool = False
    best_season: str = "all"
    tags: str = ""
    image_url: Optional[str] = None
    data_source: str = "curated_seed"


class WeatherForecastItem(BaseModel):
    date: str
    temp_min_c: float
    temp_max_c: float
    rain_probability_pct: float
    condition: str
    outdoor_suitability: str  # Suitable, Moderate, Poor
    suitability_score: float  # 0 to 100
    disruption_window: Optional[str] = None
    recommendation: str
    data_source: str = "Open-Meteo"


class PredictionFeatures(BaseModel):
    destination: str
    category: str = "nature"
    day_of_week: int = 2  # 0-6
    is_weekend: bool = False
    hour: int = 11
    month: int = 10
    rain_probability: float = 0.1
    temperature_c: float = 24.0
    is_indoor: bool = False
    base_popularity: float = 0.7
    group_size: int = 1
    transport_mode: str = "taxi"


class CrowdPredictionResult(BaseModel):
    crowd_score: float  # 0-100
    category: str  # Low, Moderate, High, Very High
    hourly_curve: Dict[int, float]
    best_visiting_time: str
    confidence: float
    explanation: str
    data_source: str
    model_version: str


class CostPredictionResult(BaseModel):
    total_cost_inr: float
    per_person_inr: float
    breakdown: Dict[str, float]  # tickets, food, transport, activities, misc
    known_vs_estimated: str
    budget_utilization_pct: float
    confidence: float
    data_source: str
    model_version: str


class DisruptionPredictionResult(BaseModel):
    risk_level: str  # Low, Medium, High
    risk_score: float  # 0-100
    probability: float
    primary_reason: str
    suggested_action: str
    data_source: str
    model_version: str


class FeasibilityScoreResult(BaseModel):
    overall_score: float  # 0-100
    status: str  # Highly Feasible, Feasible with Adjustments, Critical Issues
    breakdown: Dict[str, float]  # weather, crowd, travel, budget, activity, schedule, disruption
    explanation: str


class RecommendationRequest(BaseModel):
    destination: str
    budget_level: str = "medium"  # low, medium, luxury
    pace: str = "moderate"  # relaxed, moderate, packed
    season: str = "winter"
    interests: Dict[str, float] = Field(default_factory=dict)
    seed_ratings: Optional[Dict[str, float]] = None
    num_candidates: int = 30


class ScoredPlaceItem(PlaceItem):
    personalization_score: float  # 0 to 100
    content_score: float
    collab_score: float
    ranking: int
    why_recommended: List[str]


class ItineraryGenerateRequest(BaseModel):
    destination: str
    start_date: str = "2026-11-01"
    num_days: int = 3
    budget_inr: float = 15000.0
    pace: str = "moderate"
    transport: str = "taxi"
    travelers_count: int = 1
    interests: Dict[str, float] = Field(default_factory=dict)
    seed_ratings: Optional[Dict[str, float]] = None
    user_id: Optional[str] = None


class ItineraryStopSchema(BaseModel):
    place_id: str
    place_name: str
    category: str
    city: str
    lat: float
    lon: float
    arrival_time: str
    departure_time: str
    slot: str = "Morning"  # Morning, Afternoon, Evening
    visit_duration_min: float
    travel_time_from_prev_min: float
    travel_distance_km: float
    cost_inr: float
    crowd_forecast: float
    disruption_risk: str
    is_indoor: bool
    personalization_score: float
    why_recommended: List[str]


class ItineraryDaySchema(BaseModel):
    day_number: int
    date: str
    stops: List[ItineraryStopSchema]
    total_travel_time_min: float
    total_visit_time_min: float
    total_cost_inr: float
    feasibility: float


class ParetoSolutionSchema(BaseModel):
    solution_index: int
    total_score: float
    total_cost_inr: float
    total_travel_time_min: float
    category_diversity: float
    avg_crowd_level: float
    total_places: int
    is_knee_point: bool = False
    days: List[ItineraryDaySchema]


class ItineraryResponse(BaseModel):
    trip_id: str
    destination: str
    chosen_solution_index: int
    chosen_itinerary: ParetoSolutionSchema
    pareto_solutions: List[ParetoSolutionSchema]
    feasibility_score: float
    feasibility_breakdown: Dict[str, float]
    weather_summary: List[WeatherForecastItem]
    solver_info: Dict[str, Any]
    data_source_labels: Dict[str, str]


class ItineraryReplanRequest(BaseModel):
    trip_id: str
    destination: str
    simulate_rain: bool = False
    simulate_crowd: bool = False
    new_budget: Optional[float] = None
    new_pace: Optional[str] = None


class ItineraryChangeRecord(BaseModel):
    original_place: str
    replacement_place: str
    reason: str
    weather_condition: Optional[str] = None
    old_cost: float
    new_cost: float
    auto_adjusted: bool = True


class ReplanResponse(BaseModel):
    revised_itinerary: ParetoSolutionSchema
    changes: List[ItineraryChangeRecord]
    old_feasibility: float
    new_feasibility: float
    message: str


class ChatMessageRequest(BaseModel):
    trip_id: Optional[str] = None
    destination: str = "Udaipur"
    date: Optional[str] = None
    message: str
    auto_replan: bool = False


class ChatMessageResponse(BaseModel):
    reply: str
    tool_calls_executed: List[str]
    proposed_changes: Optional[List[Dict[str, Any]]] = None
    data_source: str = "Copilot"


class SimulationRequest(BaseModel):
    trip_id: str
    scenario_type: str  # rain_shock, crowd_spike, budget_cut, relaxed_pace, transport_change, date_change
    parameters: Dict[str, Any] = Field(default_factory=dict)

