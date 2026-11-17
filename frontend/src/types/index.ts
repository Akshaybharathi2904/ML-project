export interface Destination {
  id: string;
  name: string;
  state: string;
  lat: number;
  lon: number;
  best_season: string;
  approx_daily_budget_inr: number;
  recommended_duration_days: number;
  overview: string;
  image_url?: string;
  data_source?: string;
}

export interface Place {
  id: string;
  name: string;
  destination: string;
  state?: string;
  country_code: string;
  lat: number;
  lon: number;
  category: string;
  avg_cost_inr: number;
  avg_visit_duration_min: number;
  rating: number;
  popularity: number;
  crowd_level: number;
  open_time: string;
  close_time: string;
  is_indoor: boolean;
  best_season: string;
  tags: string;
  image_url?: string;
  data_source?: string;
}

export interface WeatherForecast {
  date: string;
  temp_min_c: number;
  temp_max_c: number;
  rain_probability_pct: number;
  condition: string;
  outdoor_suitability: string;
  suitability_score: number;
  disruption_window?: string;
  recommendation: string;
  data_source: string;
}

export interface ItineraryStop {
  place_id: string;
  place_name: string;
  category: string;
  city: string;
  lat: number;
  lon: number;
  arrival_time: string;
  departure_time: string;
  slot?: 'Morning' | 'Afternoon' | 'Evening';
  visit_duration_min: number;
  travel_time_from_prev_min: number;
  travel_distance_km: number;
  cost_inr: number;
  crowd_forecast: number;
  disruption_risk: string;
  is_indoor: boolean;
  personalization_score: number;
  why_recommended: string[];
}

export interface BudgetCategory {
  name: string;
  cost_inr: number;
  percentage: number;
  color: string;
}

export interface BudgetBreakdownData {
  trip_id: string;
  destination: string;
  num_days: number;
  user_budget_inr: number;
  total_estimated_inr: number;
  budget_remaining_inr: number;
  utilization_percentage: number;
  is_budget_exceeded: boolean;
  warnings: string[];
  categories: BudgetCategory[];
}

export interface ShapFeatureItem {
  feature: string;
  description: string;
  shap_value: number;
  direction: 'positive' | 'negative';
}

export interface ShapExplanationData {
  place_id: string;
  place_name: string;
  reasons: string[];
  base_value: number;
  feature_impact: Record<string, number>;
  features_breakdown: ShapFeatureItem[];
  model_name: string;
  data_source: string;
}

export interface UserProfile {
  user_id: string;
  username: string;
  email?: string;
  budget_level: string;
  pace_preference: string;
  preferences: Record<string, number>;
  auth_token?: string;
}

export interface UserRatingItem {
  place_id: string;
  rating: number;
  timestamp?: string;
  feedback?: string;
}

export interface SavedTripItem {
  id: string;
  trip_id: string;
  user_id?: string;
  name: string;
  destination: string;
  days_count: number;
  total_cost: number;
  feasibility: number;
  saved_at: string;
  status?: string;
}

export interface CrowdAnalyticsData {
  place_id: string;
  place_name: string;
  prediction: {
    crowd_score: number;
    category: string;
    hourly_curve: Record<number, number>;
    best_visiting_time: string;
    confidence: number;
    explanation: string;
  };
  alternatives: Array<{
    id: string;
    name: string;
    category: string;
    rating: number;
    avg_cost_inr: number;
    crowd_level: number;
    crowd_label: string;
  }>;
  evaluation_metrics: {
    algorithm: string;
    mae: number;
    rmse: number;
    r2_score: number;
  };
}

export interface ItineraryDay {
  day_number: number;
  date: string;
  stops: ItineraryStop[];
  total_travel_time_min: number;
  total_visit_time_min: number;
  total_cost_inr: number;
  feasibility: number;
}

export interface ParetoSolution {
  solution_index: number;
  total_score: number;
  total_cost_inr: number;
  total_travel_time_min: number;
  category_diversity: number;
  avg_crowd_level: number;
  total_places: number;
  is_knee_point: boolean;
  days: ItineraryDay[];
}

export interface ItineraryResponse {
  trip_id: string;
  destination: string;
  chosen_solution_index: number;
  chosen_itinerary: ParetoSolution;
  pareto_solutions: ParetoSolution[];
  feasibility_score: number;
  feasibility_breakdown: Record<string, number>;
  weather_summary: WeatherForecast[];
  solver_info: {
    algorithm: string;
    generations: number;
    population: number;
    runtime_seconds: number;
    total_pareto_front_solutions: number;
    constraint_violation_rate: string;
  };
  data_source_labels: Record<string, string>;
}

export interface EvaluationData {
  recommender_ablation: Array<Record<string, any>>;
  optimizer_benchmarks: Array<Record<string, any>>;
  end_to_end_satisfaction: Array<Record<string, any>>;
  predictor_models: Record<string, any>;
}

