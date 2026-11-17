import pytest
import pandas as pd
import numpy as np
from src.optimizer.problem import TravelPlanningProblem
from src.optimizer.solve import solve_itinerary_optimization
from src.optimizer.baselines import BaselineSolvers
from src.optimizer.selection import ParetoSelector


@pytest.fixture(scope="module")
def setup_optimizer_problem():
    places = pd.read_csv("data/processed/places.csv")
    time_mat = pd.read_csv("data/processed/travel_time_matrix.csv", index_col=0)
    places["personalization_score"] = (places["rating"] / 5.0) * places["popularity"]
    subset = places.head(40).copy().reset_index(drop=True)

    prob = TravelPlanningProblem(
        candidate_places=subset,
        travel_time_matrix=time_mat,
        num_days=2,
        daily_time_budget_min=500.0,
        total_budget_cap=5000.0,
        max_places_per_day=3,
        start_lat=12.9716,
        start_lon=77.5946,
        start_city="Bengaluru"
    )
    return prob


def test_nsga2_solver(setup_optimizer_problem):
    prob = setup_optimizer_problem
    res = solve_itinerary_optimization(prob, algorithm_name="nsga2", pop_size=25, generations=15, seed=42)
    assert len(res.pareto_solutions) >= 1
    assert res.knee_solution is not None
    assert res.runtime_sec < 10.0


def test_nsga3_solver(setup_optimizer_problem):
    prob = setup_optimizer_problem
    res = solve_itinerary_optimization(prob, algorithm_name="nsga3", pop_size=25, generations=15, seed=42)
    assert len(res.pareto_solutions) >= 1
    assert res.knee_solution is not None


def test_baselines(setup_optimizer_problem):
    prob = setup_optimizer_problem
    solvers = BaselineSolvers(prob)

    rand_sols = solvers.solve_random(num_samples=10)
    assert len(rand_sols) == 10

    greedy_score = solvers.solve_greedy_score()
    assert greedy_score.total_personalization_score > 0.0

    greedy_ratio = solvers.solve_greedy_score_cost()
    assert greedy_ratio.total_personalization_score > 0.0

    ga_sol = solvers.solve_weighted_sum_ga(pop_size=20, generations=10, seed=42)
    assert ga_sol.total_personalization_score > 0.0


def test_pareto_selector(setup_optimizer_problem):
    prob = setup_optimizer_problem
    res = solve_itinerary_optimization(prob, algorithm_name="nsga2", pop_size=25, generations=15, seed=42)
    selector = ParetoSelector(res.pareto_solutions)

    knee_idx, knee_sol = selector.find_knee_point()
    assert 0 <= knee_idx < len(res.pareto_solutions)

    # Test weight customization
    idx_budget, sol_budget = selector.select_by_weights(weight_score=0.1, weight_cost=5.0)
    assert 0 <= idx_budget < len(res.pareto_solutions)

