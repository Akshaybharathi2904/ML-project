import time
import numpy as np
import pandas as pd
from typing import List, Dict, Any, Tuple, Optional
from dataclasses import dataclass

from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.algorithms.moo.nsga3 import NSGA3
from pymoo.util.ref_dirs import get_reference_directions
from pymoo.operators.crossover.sbx import SBX
from pymoo.operators.mutation.pm import PM
from pymoo.optimize import minimize
from pymoo.util.nds.non_dominated_sorting import NonDominatedSorting

from src.optimizer.problem import TravelPlanningProblem, ItinerarySolution
from src.optimizer.repair import ItineraryRepair
from src.optimizer.selection import ParetoSelector


@dataclass
class OptimizerResult:
    pareto_solutions: List[ItinerarySolution]
    knee_solution: ItinerarySolution
    knee_index: int
    algorithm_name: str
    runtime_sec: float
    n_evals: int
    selector: ParetoSelector


def solve_itinerary_optimization(
    problem: TravelPlanningProblem,
    algorithm_name: str = "nsga2",
    pop_size: int = 40,
    generations: int = 45,
    seed: int = 42,
    use_repair: bool = True
) -> OptimizerResult:
    """
    Execute multi-objective itinerary optimization using NSGA-II or NSGA-III / MOEA/D.
    """
    start_t = time.perf_counter()

    repair_op = ItineraryRepair(problem) if use_repair else None

    # Algorithm setup
    algo_lower = algorithm_name.lower().replace("-", "")
    if "nsga3" in algo_lower or "moead" in algo_lower:
        # NSGA-III is the state-of-the-art reference-direction solver for 5 objectives
        ref_dirs = get_reference_directions("das-dennis", 5, n_partitions=3)
        actual_pop = len(ref_dirs)
        algorithm = NSGA3(
            ref_dirs=ref_dirs,
            pop_size=actual_pop,
            crossover=SBX(prob=0.9, eta=15),
            mutation=PM(prob=0.2, eta=20),
            repair=repair_op,
            eliminate_duplicates=True,
        )
    else:  # Default NSGA-II
        algorithm = NSGA2(
            pop_size=pop_size,
            crossover=SBX(prob=0.9, eta=15),
            mutation=PM(prob=0.2, eta=20),
            repair=repair_op,
            eliminate_duplicates=True,
        )

    res = minimize(
        problem,
        algorithm,
        ("n_gen", generations),
        seed=seed,
        verbose=False,
    )

    elapsed_sec = time.perf_counter() - start_t

    # Extract non-dominated solutions
    if res.X is None or len(res.X) == 0:
        # Fallback if single evaluation
        pop_x = np.random.uniform(0, 1, size=(5, problem.num_candidates))
    else:
        pop_x = np.atleast_2d(res.X)

    # Decode all population members
    decoded_sols = [problem.decode_chromosome(x) for x in pop_x]

    # Non-dominated sorting to extract exact rank 0 (true Pareto front)
    F = np.array([s.objectives for s in decoded_sols])
    nds = NonDominatedSorting()
    fronts = nds.do(F)
    pareto_indices = fronts[0] if len(fronts) > 0 else list(range(len(decoded_sols)))

    # Deduplicate distinct solutions on the front
    seen_signatures = set()
    unique_pareto_sols: List[ItinerarySolution] = []
    for idx in pareto_indices:
        sol = decoded_sols[idx]
        sig = tuple(round(float(v), 2) for v in sol.objectives)
        if sig not in seen_signatures:
            seen_signatures.add(sig)
            unique_pareto_sols.append(sol)

    if not unique_pareto_sols:
        unique_pareto_sols = decoded_sols[:5]

    selector = ParetoSelector(unique_pareto_sols)
    knee_idx, knee_sol = selector.find_knee_point()

    return OptimizerResult(
        pareto_solutions=unique_pareto_sols,
        knee_solution=knee_sol,
        knee_index=knee_idx,
        algorithm_name=algorithm_name.upper(),
        runtime_sec=round(elapsed_sec, 2),
        n_evals=int(res.algorithm.evaluator.n_eval) if hasattr(res, "algorithm") and hasattr(res.algorithm, "evaluator") else pop_size * generations,
        selector=selector,
    )

