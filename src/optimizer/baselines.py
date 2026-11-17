import numpy as np
import pandas as pd
from typing import List, Dict, Any, Tuple
from pymoo.algorithms.soo.nonconvex.ga import GA
from pymoo.core.problem import Problem
from pymoo.optimize import minimize
from pymoo.operators.crossover.sbx import SBX
from pymoo.operators.mutation.pm import PM
from src.optimizer.problem import TravelPlanningProblem, ItinerarySolution


class BaselineSolvers:
    """
    Comparison Baselines for Itinerary Optimization:
      1. Random valid itineraries
      2. Greedy by personalization score
      3. Greedy by personalization score / cost ratio
      4. Single-objective Weighted-Sum GA
    """

    def __init__(self, problem: TravelPlanningProblem):
        self.problem = problem

    def solve_random(self, num_samples: int = 100) -> List[ItinerarySolution]:
        """Generate random valid itineraries and return solutions."""
        solutions = []
        for _ in range(num_samples):
            vec = np.random.uniform(0.0, 1.0, size=self.problem.num_candidates)
            sol = self.problem.decode_chromosome(vec)
            solutions.append(sol)
        return solutions

    def solve_greedy_score(self) -> ItinerarySolution:
        """Greedy heuristic: prioritize candidate places strictly by predicted personalization score."""
        vec = self.problem.p_scores.copy()
        return self.problem.decode_chromosome(vec)

    def solve_greedy_score_cost(self) -> ItinerarySolution:
        """Greedy heuristic: prioritize candidate places by personalization score / cost ratio."""
        safe_costs = np.maximum(self.problem.p_costs, 20.0)
        ratios = self.problem.p_scores / safe_costs
        # Normalize to [0, 1]
        norm_ratios = (ratios - ratios.min()) / (ratios.max() - ratios.min() + 1e-6)
        return self.problem.decode_chromosome(norm_ratios)

    def solve_weighted_sum_ga(
        self,
        pop_size: int = 40,
        generations: int = 40,
        weights: Tuple[float, float, float, float, float] = (0.35, 0.2, 0.15, 0.15, 0.15),
        seed: int = 42
    ) -> ItinerarySolution:
        """
        Single-objective Weighted-Sum Genetic Algorithm.
        Collapses all 5 objectives into a single scalar fitness function.
        """
        prob = self.problem

        class SingleObjectiveScalarizedProblem(Problem):
            def __init__(self):
                super().__init__(
                    n_var=prob.num_candidates,
                    n_obj=1,
                    n_constr=0,
                    xl=0.0,
                    xu=1.0,
                )

            def _evaluate(self, X, out, *args, **kwargs):
                n = X.shape[0]
                F = np.zeros((n, 1), dtype=np.float32)
                w1, w2, w3, w4, w5 = weights
                for i in range(n):
                    sol = prob.decode_chromosome(X[i])
                    # Scalar penalty objective to minimize:
                    # -w1*score + w2*cost/1000 + w3*time/60 - w4*diversity + w5*crowd
                    scalar_val = (
                        - w1 * (sol.total_personalization_score * 2.0)
                        + w2 * (sol.total_cost / max(prob.total_budget_cap, 1.0))
                        + w3 * (sol.total_travel_time / (prob.daily_time_budget_min * prob.num_days))
                        - w4 * sol.category_diversity
                        + w5 * sol.avg_crowd_level
                    )
                    F[i, 0] = scalar_val
                out["F"] = F

        single_prob = SingleObjectiveScalarizedProblem()
        algorithm = GA(
            pop_size=pop_size,
            crossover=SBX(prob=0.9, eta=15),
            mutation=PM(prob=0.2, eta=20),
            eliminate_duplicates=True,
        )

        res = minimize(
            single_prob,
            algorithm,
            ("n_gen", generations),
            seed=seed,
            verbose=False,
        )

        best_x = res.X if res.X is not None else np.random.uniform(0, 1, size=prob.num_candidates)
        return prob.decode_chromosome(best_x)

