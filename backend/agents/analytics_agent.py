from typing import Dict, Any, List
import numpy as np
from backend.schemas.schemas import ItineraryResponse, ParetoSolutionSchema


class AnalyticsAgent:
    """Agent 7: Synthesizes multi-dimensional trip analytics, feasibility scores, and budget utilization."""

    def execute(self, itinerary_resp: ItineraryResponse, budget_inr: float) -> Dict[str, Any]:
        sol: ParetoSolutionSchema = itinerary_resp.chosen_itinerary

        # Daily travel distance and time
        daily_stats = []
        for d in sol.days:
            daily_stats.append({
                "day_number": d.day_number,
                "stops_count": len(d.stops),
                "travel_time_min": d.total_travel_time_min,
                "estimated_distance_km": round(d.total_travel_time_min * 0.45, 1),
                "cost_inr": d.total_cost_inr,
            })

        # Category distribution
        cats: Dict[str, int] = {}
        for d in sol.days:
            for s in d.stops:
                cats[s.category] = cats.get(s.category, 0) + 1

        category_distribution = [{"category": k.capitalize(), "count": v} for k, v in cats.items()]

        # Budget utilization
        budget_util_pct = round((sol.total_cost_inr / max(1.0, budget_inr)) * 100.0, 1)
        remaining_budget = max(0.0, budget_inr - sol.total_cost_inr)

        return {
            "feasibility_score": itinerary_resp.feasibility_score,
            "feasibility_breakdown": itinerary_resp.feasibility_breakdown,
            "budget_inr": budget_inr,
            "total_estimated_cost_inr": sol.total_cost_inr,
            "budget_utilization_pct": budget_util_pct,
            "remaining_budget_inr": round(remaining_budget, 2),
            "total_places_visited": sol.total_places,
            "category_diversity_entropy": sol.category_diversity,
            "average_crowd_exposure": sol.avg_crowd_level,
            "daily_stats": daily_stats,
            "category_distribution": category_distribution,
            "pareto_solutions_count": len(itinerary_resp.pareto_solutions)
        }

