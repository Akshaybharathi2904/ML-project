import numpy as np
from pymoo.core.repair import Repair
from src.optimizer.problem import TravelPlanningProblem


class ItineraryRepair(Repair):
    """
    Repair operator for multi-day travel planning.
    
    Adjusts priority values to reduce travel fragmentation, dampen high-cost
    candidates when budget pressure is acute, and inject geographic locality.
    """

    def __init__(self, problem: TravelPlanningProblem):
        super().__init__()
        self.problem = problem

    def _do(self, problem, X, **kwargs):
        """
        Perform domain-aware repair on population chromosome matrix X.
        """
        n_pop, n_var = X.shape
        repaired_X = X.copy()

        # Place costs and start travel times from problem
        costs = self.problem.p_costs
        scores = self.problem.p_scores
        budget_cap = self.problem.total_budget_cap

        for i in range(n_pop):
            sol = self.problem.decode_chromosome(repaired_X[i])
            
            # If total cost exceeds 85% of budget cap, slightly dampen top-cost items
            if sol.total_cost > 0.85 * budget_cap:
                high_cost_mask = costs > np.percentile(costs, 75)
                repaired_X[i, high_cost_mask] *= 0.85

            # If solution visited fewer than planned stops, boost top personalization candidates
            total_stops = sum(len(d.stops) for d in sol.days)
            target_stops = self.problem.num_days * (self.problem.max_places_per_day - 1)
            if total_stops < target_stops:
                high_score_mask = scores > np.percentile(scores, 70)
                repaired_X[i, high_score_mask] = np.clip(repaired_X[i, high_score_mask] + 0.15, 0.0, 1.0)

        return repaired_X

