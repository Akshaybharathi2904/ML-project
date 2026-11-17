import numpy as np
import pandas as pd
from typing import List, Dict, Any, Tuple, Optional
from dataclasses import dataclass
from pymoo.core.problem import Problem
from src.utils.geo import haversine_distance_km, compute_travel_time_minutes


@dataclass
class ItineraryStop:
    place_id: str
    place_name: str
    category: str
    city: str
    lat: float
    lon: float
    arrival_time_min: float  # e.g., minutes from 08:00 AM (0 = 08:00)
    departure_time_min: float
    visit_duration_min: float
    travel_time_from_prev_min: float
    cost_inr: float
    crowd_level: float
    personalization_score: float


@dataclass
class ItineraryDay:
    day_number: int
    stops: List[ItineraryStop]
    total_travel_time_min: float
    total_visit_time_min: float
    total_cost_inr: float
    day_score: float


@dataclass
class ItinerarySolution:
    days: List[ItineraryDay]
    total_personalization_score: float
    total_cost: float
    total_travel_time: float
    category_diversity: float
    avg_crowd_level: float
    objectives: np.ndarray  # [-f1, f2, f3, -f4, f5] for pymoo minimization


def parse_time_str_to_min(time_str: str) -> float:
    """Convert HH:MM 24-hr string to minutes since midnight."""
    try:
        parts = time_str.split(":")
        return float(int(parts[0]) * 60 + int(parts[1]))
    except Exception:
        return 540.0  # Default 09:00 AM


class TravelPlanningProblem(Problem):
    """
    Multi-Objective Team Orienteering Problem with Time Windows (TOPTW).
    
    Objectives:
      f1 = Maximize Personalization Score (minimize -f1)
      f2 = Minimize Total Cost (INR)
      f3 = Minimize Total Travel Time (minutes)
      f4 = Maximize Category Diversity (entropy, minimize -f4)
      f5 = Minimize Average Crowd Level [0, 1]
    """

    def __init__(
        self,
        candidate_places: pd.DataFrame,
        travel_time_matrix: pd.DataFrame,
        num_days: int = 3,
        daily_time_budget_min: float = 600.0,
        total_budget_cap: float = 15000.0,
        max_places_per_day: int = 4,
        start_lat: float = 12.9716,
        start_lon: float = 77.5946,
        start_city: str = "Bengaluru",
        day_start_time_str: str = "08:30"
    ):
        self.candidate_places = candidate_places.copy().reset_index(drop=True)
        self.num_candidates = len(self.candidate_places)
        self.time_mat = travel_time_matrix
        self.num_days = num_days
        self.daily_time_budget_min = daily_time_budget_min
        self.total_budget_cap = total_budget_cap
        self.max_places_per_day = max_places_per_day
        self.start_lat = start_lat
        self.start_lon = start_lon
        self.start_city = start_city
        self.day_start_min = parse_time_str_to_min(day_start_time_str)

        # Precompute lookups for ultra-fast chromosome decoding
        self.p_ids = self.candidate_places["id"].tolist()
        self.p_names = self.candidate_places["name"].tolist()
        self.p_cats = self.candidate_places["category"].tolist()
        if "city" in self.candidate_places.columns:
            self.p_cities = self.candidate_places["city"].tolist()
        elif "destination_name" in self.candidate_places.columns:
            self.p_cities = self.candidate_places["destination_name"].tolist()
        elif "destination" in self.candidate_places.columns:
            self.p_cities = self.candidate_places["destination"].tolist()
        else:
            self.p_cities = [start_city] * self.num_candidates
        self.p_lats = self.candidate_places["lat"].to_numpy()
        self.p_lons = self.candidate_places["lon"].to_numpy()
        self.p_costs = self.candidate_places["avg_cost_inr"].to_numpy()
        self.p_durs = self.candidate_places["avg_visit_duration_min"].to_numpy()
        self.p_crowds = self.candidate_places["crowd_level"].to_numpy()
        self.p_scores = self.candidate_places["personalization_score"].to_numpy()
        
        self.p_open_mins = np.array([parse_time_str_to_min(t) for t in self.candidate_places["open_time"]])
        self.p_close_mins = np.array([parse_time_str_to_min(t) for t in self.candidate_places["close_time"]])

        # Precompute initial travel times from start location
        self.start_travel_times = np.zeros(self.num_candidates, dtype=np.float32)
        for i in range(self.num_candidates):
            d = haversine_distance_km(self.start_lat, self.start_lon, self.p_lats[i], self.p_lons[i])
            self.start_travel_times[i] = compute_travel_time_minutes(d)

        # Pre-extract pairwise travel times as numpy array
        self.pairwise_time = np.zeros((self.num_candidates, self.num_candidates), dtype=np.float32)
        for i in range(self.num_candidates):
            pid_i = self.p_ids[i]
            for j in range(self.num_candidates):
                pid_j = self.p_ids[j]
                if pid_i in self.time_mat.index and pid_j in self.time_mat.columns:
                    self.pairwise_time[i, j] = float(self.time_mat.loc[pid_i, pid_j])
                else:
                    d = haversine_distance_km(self.p_lats[i], self.p_lons[i], self.p_lats[j], self.p_lons[j])
                    self.pairwise_time[i, j] = compute_travel_time_minutes(d)

        super().__init__(
            n_var=self.num_candidates,
            n_obj=5,
            n_constr=0,
            xl=0.0,
            xu=1.0,
        )

    def decode_chromosome(self, priority_vec: np.ndarray) -> ItinerarySolution:
        """
        Decode a real-valued priority vector into an exact, constraint-satisfying
        day-by-day itinerary schedule.
        """
        # Order candidates by priority (descending)
        order = np.argsort(-priority_vec)

        visited = np.zeros(self.num_candidates, dtype=bool)
        days: List[ItineraryDay] = []
        cumulative_cost = 0.0

        cand_ptr = 0
        curr_lat = self.start_lat
        curr_lon = self.start_lon
        curr_place_idx = -1

        for day_idx in range(1, self.num_days + 1):
            day_stops: List[ItineraryStop] = []
            day_clock_min = self.day_start_min  # e.g., 510.0 (08:30 AM)
            day_travel_time = 0.0
            day_visit_time = 0.0
            day_cost = 0.0
            day_score = 0.0

            # For subsequent days, optionally restart from current city cluster
            for _ in range(self.num_candidates):
                if len(day_stops) >= self.max_places_per_day:
                    break
                if cand_ptr >= self.num_candidates:
                    break

                idx = order[cand_ptr]
                cand_ptr += 1

                if visited[idx]:
                    continue

                # Check budget
                p_cost = self.p_costs[idx]
                if cumulative_cost + day_cost + p_cost > self.total_budget_cap:
                    continue

                # Calculate travel time from previous location
                if curr_place_idx == -1:
                    t_travel = self.start_travel_times[idx]
                else:
                    t_travel = self.pairwise_time[curr_place_idx, idx]

                p_dur = self.p_durs[idx]
                arr_clock_min = day_clock_min + t_travel
                
                # Check opening / closing window
                open_m = self.p_open_mins[idx]
                close_m = self.p_close_mins[idx]

                # If arriving before open, wait until opening
                service_start = max(arr_clock_min, open_m)
                dept_clock_min = service_start + p_dur

                # Check if departure exceeds closing time or daily time limit
                if service_start > close_m - 30.0:  # Must have at least 30 min before closing
                    continue

                added_day_time = (dept_clock_min - self.day_start_min)
                if added_day_time > self.daily_time_budget_min:
                    continue

                # Place fits all constraints!
                visited[idx] = True
                curr_place_idx = idx
                curr_lat = self.p_lats[idx]
                curr_lon = self.p_lons[idx]
                day_clock_min = dept_clock_min
                day_travel_time += t_travel
                day_visit_time += p_dur
                day_cost += p_cost
                day_score += self.p_scores[idx]

                stop = ItineraryStop(
                    place_id=self.p_ids[idx],
                    place_name=self.p_names[idx],
                    category=self.p_cats[idx],
                    city=self.p_cities[idx],
                    lat=float(curr_lat),
                    lon=float(curr_lon),
                    arrival_time_min=round(float(arr_clock_min), 1),
                    departure_time_min=round(float(dept_clock_min), 1),
                    visit_duration_min=float(p_dur),
                    travel_time_from_prev_min=round(float(t_travel), 1),
                    cost_inr=float(p_cost),
                    crowd_level=float(self.p_crowds[idx]),
                    personalization_score=round(float(self.p_scores[idx]), 4),
                )
                day_stops.append(stop)

            cumulative_cost += day_cost
            days.append(
                ItineraryDay(
                    day_number=day_idx,
                    stops=day_stops,
                    total_travel_time_min=round(day_travel_time, 1),
                    total_visit_time_min=round(day_visit_time, 1),
                    total_cost_inr=round(day_cost, 2),
                    day_score=round(day_score, 4),
                )
            )

        # Compute aggregate 5 objectives
        all_stops = [s for d in days for s in d.stops]
        n_stops = len(all_stops)

        if n_stops == 0:
            # Fallback penalty for empty solution
            f1_score = 0.01
            f2_cost = self.total_budget_cap
            f3_travel = self.daily_time_budget_min * self.num_days
            f4_diversity = 0.0
            f5_crowd = 1.0
        else:
            f1_score = sum(s.personalization_score for s in all_stops)
            f2_cost = sum(s.cost_inr for s in all_stops)
            f3_travel = sum(d.total_travel_time_min for d in days)
            
            # Shannon Entropy for category diversity
            cat_counts: Dict[str, int] = {}
            for s in all_stops:
                cat_counts[s.category] = cat_counts.get(s.category, 0) + 1
            probs = np.array(list(cat_counts.values()), dtype=np.float32) / n_stops
            f4_diversity = float(-np.sum(probs * np.log(probs + 1e-9)))

            f5_crowd = float(np.mean([s.crowd_level for s in all_stops]))

        objectives = np.array([
            -f1_score,      # Maximize personalization score
            f2_cost,       # Minimize total cost
            f3_travel,     # Minimize travel time
            -f4_diversity, # Maximize category entropy
            f5_crowd,      # Minimize average crowd level
        ], dtype=np.float32)

        return ItinerarySolution(
            days=days,
            total_personalization_score=round(float(f1_score), 4),
            total_cost=round(float(f2_cost), 2),
            total_travel_time=round(float(f3_travel), 1),
            category_diversity=round(float(f4_diversity), 4),
            avg_crowd_level=round(float(f5_crowd), 3),
            objectives=objectives,
        )

    def _evaluate(self, X: np.ndarray, out: Dict[str, Any], *args, **kwargs):
        """Pymoo batch evaluation hook."""
        pop_size = X.shape[0]
        F = np.zeros((pop_size, 5), dtype=np.float32)
        for i in range(pop_size):
            sol = self.decode_chromosome(X[i])
            F[i, :] = sol.objectives
        out["F"] = F

