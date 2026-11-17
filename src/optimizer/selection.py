import numpy as np
import pandas as pd
from typing import List, Dict, Any, Tuple, Optional
from src.optimizer.problem import ItinerarySolution


class ParetoSelector:
    """
    Selects solutions from the multi-objective Pareto front.
    
    Implements:
      1. Nearest-to-Ideal-Point Knee Point recommendation (Compromise Programming / TOPSIS).
      2. User-weighted preference selection without collapsing the evolutionary search space.
    """

    def __init__(self, solutions: List[ItinerarySolution]):
        self.solutions = solutions
        self.num_solutions = len(solutions)

    def _extract_objective_matrix(self) -> np.ndarray:
        """
        Extract raw objectives for all solutions in standardized directions:
        Col 0: Personalization Score (Higher is better)
        Col 1: Total Cost (Lower is better)
        Col 2: Total Travel Time (Lower is better)
        Col 3: Category Diversity (Higher is better)
        Col 4: Average Crowd Level (Lower is better)
        """
        mat = np.zeros((self.num_solutions, 5), dtype=np.float32)
        for i, s in enumerate(self.solutions):
            mat[i, 0] = s.total_personalization_score
            mat[i, 1] = s.total_cost
            mat[i, 2] = s.total_travel_time
            mat[i, 3] = s.category_diversity
            mat[i, 4] = s.avg_crowd_level
        return mat

    def _compute_normalized_distance_to_ideal(
        self,
        raw_mat: np.ndarray,
        weights: Optional[np.ndarray] = None
    ) -> np.ndarray:
        """
        Normalize each objective to [0, 1] representing distance to ideal (0 is ideal).
        Apply user preference weights.
        """
        n, m = raw_mat.shape
        dist_to_ideal = np.zeros((n, m), dtype=np.float32)
        eps = 1e-6

        # Direction signs: +1 for maximize, -1 for minimize
        maximize_flags = [True, False, False, True, False]

        for j in range(m):
            col = raw_mat[:, j]
            min_val = np.min(col)
            max_val = np.max(col)
            diff = max(max_val - min_val, eps)

            if maximize_flags[j]:
                # Ideal is max_val
                dist_to_ideal[:, j] = (max_val - col) / diff
            else:
                # Ideal is min_val
                dist_to_ideal[:, j] = (col - min_val) / diff

        if weights is None:
            weights = np.ones(m, dtype=np.float32) / float(m)
        else:
            weights = weights / np.sum(weights)

        # Weighted Euclidean distance
        weighted_sq = (dist_to_ideal ** 2) * weights
        distances = np.sqrt(np.sum(weighted_sq, axis=1))
        return distances

    def find_knee_point(self) -> Tuple[int, ItinerarySolution]:
        """
        Find the balanced knee point (nearest to the ideal point with equal weights).
        """
        if self.num_solutions == 0:
            raise ValueError("No solutions available on the Pareto front.")
        if self.num_solutions == 1:
            return 0, self.solutions[0]

        raw_mat = self._extract_objective_matrix()
        distances = self._compute_normalized_distance_to_ideal(raw_mat)
        best_idx = int(np.argmin(distances))
        return best_idx, self.solutions[best_idx]

    def select_by_weights(
        self,
        weight_score: float = 1.0,
        weight_cost: float = 1.0,
        weight_time: float = 1.0,
        weight_diversity: float = 1.0,
        weight_crowd: float = 1.0
    ) -> Tuple[int, ItinerarySolution]:
        """
        Pick a solution from the Pareto front using user-customized priority weights.
        """
        if self.num_solutions == 0:
            raise ValueError("No solutions on the Pareto front.")
        if self.num_solutions == 1:
            return 0, self.solutions[0]

        w_vec = np.array([
            max(weight_score, 0.01),
            max(weight_cost, 0.01),
            max(weight_time, 0.01),
            max(weight_diversity, 0.01),
            max(weight_crowd, 0.01),
        ], dtype=np.float32)

        raw_mat = self._extract_objective_matrix()
        distances = self._compute_normalized_distance_to_ideal(raw_mat, weights=w_vec)
        best_idx = int(np.argmin(distances))
        return best_idx, self.solutions[best_idx]

    def to_dataframe(self) -> pd.DataFrame:
        """Convert all Pareto solutions into a DataFrame for Plotly tables & charts."""
        records = []
        for i, s in enumerate(self.solutions):
            records.append({
                "solution_index": i,
                "total_score": s.total_personalization_score,
                "total_cost_inr": s.total_cost,
                "total_travel_time_min": s.total_travel_time,
                "category_diversity": s.category_diversity,
                "avg_crowd_level": s.avg_crowd_level,
                "total_places": sum(len(d.stops) for d in s.days),
                "num_days": len(s.days),
            })
        return pd.DataFrame(records)

