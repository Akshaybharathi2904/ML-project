import pytest
import pandas as pd
import numpy as np
from src.optimizer.problem import TravelPlanningProblem, parse_time_str_to_min
from src.optimizer.solve import solve_itinerary_optimization


@pytest.fixture(scope="module")
def setup_problem():
    places = pd.read_csv("data/processed/places.csv")
    time_mat = pd.read_csv("data/processed/travel_time_matrix.csv", index_col=0)
    
    # Take top 40 places sorted by rating and popularity
    places["personalization_score"] = (places["rating"] / 5.0) * places["popularity"]
    subset = places.head(45).copy().reset_index(drop=True)

    prob = TravelPlanningProblem(
        candidate_places=subset,
        travel_time_matrix=time_mat,
        num_days=3,
        daily_time_budget_min=600.0,
        total_budget_cap=8000.0,
        max_places_per_day=4,
        start_lat=12.9716,
        start_lon=77.5946,
        start_city="Bengaluru",
        day_start_time_str="08:30"
    )
    return prob


def test_no_repeated_places(setup_problem):
    prob = setup_problem
    random_vec = np.random.uniform(0, 1, size=prob.num_candidates)
    sol = prob.decode_chromosome(random_vec)

    visited_places = []
    for day in sol.days:
        for stop in day.stops:
            visited_places.append(stop.place_id)

    assert len(visited_places) == len(set(visited_places)), "Constraint violation: Duplicate places found in itinerary!"


def test_daily_time_budget(setup_problem):
    prob = setup_problem
    random_vec = np.random.uniform(0, 1, size=prob.num_candidates)
    sol = prob.decode_chromosome(random_vec)

    for day in sol.days:
        total_day_time = day.total_travel_time_min + day.total_visit_time_min
        # Must be within the configured daily time budget
        assert total_day_time <= prob.daily_time_budget_min + 1.0, (
            f"Constraint violation: Day {day.day_number} time {total_day_time} exceeded budget {prob.daily_time_budget_min}"
        )


def test_budget_cap(setup_problem):
    prob = setup_problem
    random_vec = np.random.uniform(0, 1, size=prob.num_candidates)
    sol = prob.decode_chromosome(random_vec)

    assert sol.total_cost <= prob.total_budget_cap + 0.01, (
        f"Constraint violation: Total cost {sol.total_cost} exceeded cap {prob.total_budget_cap}"
    )


def test_max_places_per_day(setup_problem):
    prob = setup_problem
    random_vec = np.random.uniform(0, 1, size=prob.num_candidates)
    sol = prob.decode_chromosome(random_vec)

    for day in sol.days:
        assert len(day.stops) <= prob.max_places_per_day, (
            f"Constraint violation: Day {day.day_number} has {len(day.stops)} stops, exceeds max {prob.max_places_per_day}"
        )


def test_opening_hours(setup_problem):
    prob = setup_problem
    np.random.seed(42)
    random_vec = np.random.uniform(0, 1, size=prob.num_candidates)
    sol = prob.decode_chromosome(random_vec)

    p_dict = {r["id"]: r for _, r in prob.candidate_places.iterrows()}
    for day in sol.days:
        for stop in day.stops:
            p_meta = p_dict[stop.place_id]
            close_min = parse_time_str_to_min(p_meta["close_time"])
            assert stop.departure_time_min <= close_min + 30.0, (
                f"Constraint violation: Stop {stop.place_name} departure {stop.departure_time_min} exceeds closing {close_min}"
            )


def test_pareto_front_constraint_satisfaction(setup_problem):
    """Verify that EVERY solution returned on the Pareto front satisfies all constraints."""
    prob = setup_problem
    result = solve_itinerary_optimization(prob, algorithm_name="nsga2", pop_size=30, generations=25, seed=42)
    assert len(result.pareto_solutions) > 0

    for sol in result.pareto_solutions:
        # Check duplicates
        pids = [s.place_id for d in sol.days for s in d.stops]
        assert len(pids) == len(set(pids))
        # Check budget
        assert sol.total_cost <= prob.total_budget_cap + 0.01
        # Check daily time
        for d in sol.days:
            assert d.total_travel_time_min + d.total_visit_time_min <= prob.daily_time_budget_min + 1.0
            assert len(d.stops) <= prob.max_places_per_day

