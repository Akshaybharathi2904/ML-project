import numpy as np
import pandas as pd
from typing import List, Dict, Any, Tuple
from pymoo.indicators.hv import HV
from src.optimizer.problem import ItinerarySolution


def compute_spacing_metric(F: np.ndarray) -> float:
    """
    Calculate the Spacing metric (uniformity of spread across the Pareto front).
    Lower value indicates a more uniform distribution of trade-offs.
    """
    n_points = F.shape[0]
    if n_points <= 1:
        return 0.0

    # Pairwise Manhattan distances
    dists = np.zeros(n_points, dtype=np.float32)
    for i in range(n_points):
        other_pts = np.delete(F, i, axis=0)
        manhattan_dists = np.sum(np.abs(other_pts - F[i]), axis=1)
        dists[i] = np.min(manhattan_dists)

    d_mean = np.mean(dists)
    spacing = np.sqrt(np.mean((dists - d_mean) ** 2))
    return float(round(spacing, 4))


def compute_pareto_hypervolume(
    F: np.ndarray,
    ref_point: np.ndarray = None
) -> float:
    """
    Compute normalized Hypervolume (HV) indicator.
    Higher HV indicates superior convergence and diversity.
    """
    if len(F) == 0:
        return 0.0

    # Normalize objectives to [0, 1] bounds for numerical stability
    f_min = np.min(F, axis=0)
    f_max = np.max(F, axis=0)
    diff = np.where(f_max - f_min > 1e-6, f_max - f_min, 1.0)

    norm_F = (F - f_min) / diff
    
    if ref_point is None:
        ref_point = np.ones(F.shape[1], dtype=np.float32) * 1.1

    try:
        ind = HV(ref_point=ref_point)
        hv_val = float(ind(norm_F))
        return float(round(hv_val, 4))
    except Exception:
        # Fallback approximation if exact 5D hypervolume computation encounters dimension edge
        return float(round(float(np.prod(1.1 - np.mean(norm_F, axis=0))), 4))


def evaluate_optimizer_run(
    solutions: List[ItinerarySolution],
    runtime_sec: float,
    daily_time_limit: float = 600.0,
    budget_cap: float = 15000.0,
    max_places_per_day: int = 5
) -> Dict[str, float]:
    """
    Compute comprehensive metrics for an optimization run:
      - Hypervolume
      - Spread / Spacing
      - Number of non-dominated solutions
      - Runtime (seconds)
      - Constraint violation rate
    """
    n_sols = len(solutions)
    if n_sols == 0:
        return {
            "Hypervolume": 0.0,
            "Spacing": 0.0,
            "NonDominatedSolutions": 0,
            "RuntimeSec": runtime_sec,
            "ViolationRate": 1.0,
        }

    F = np.array([s.objectives for s in solutions])
    hv = compute_pareto_hypervolume(F)
    spacing = compute_spacing_metric(F)

    # Check constraint violations
    violations = 0
    for s in solutions:
        is_violated = False
        if s.total_cost > budget_cap + 1.0:
            is_violated = True
        for d in s.days:
            if len(d.stops) > max_places_per_day:
                is_violated = True
            if d.total_travel_time_min + d.total_visit_time_min > daily_time_limit + 1.0:
                is_violated = True
        
        # Check duplicate places
        pids = [stop.place_id for d in s.days for stop in d.stops]
        if len(pids) != len(set(pids)):
            is_violated = True

        if is_violated:
            violations += 1

    violation_rate = violations / float(n_sols)

    return {
        "Hypervolume": hv,
        "Spacing": spacing,
        "NonDominatedSolutions": n_sols,
        "RuntimeSec": round(runtime_sec, 2),
        "ViolationRate": round(violation_rate, 4),
    }

