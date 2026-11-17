from typing import Dict, Any, List, Optional
from backend.engines.recommendation_engine import recommendation_engine


class RecommendationAgent:
    """Agent 4: Computes personalization scores using Content-Based, SVD Collaborative, and LightGBM blender."""

    def execute(
        self,
        destination: str,
        user_interests: Dict[str, float],
        budget_level: str = "medium",
        pace: str = "moderate",
        seed_ratings: Optional[Dict[str, float]] = None
    ) -> Dict[str, Any]:
        scored_df, feat_mat = recommendation_engine.rank_destination_places(
            destination=destination,
            user_interests=user_interests,
            budget_level=budget_level,
            pace=pace,
            seed_ratings=seed_ratings,
            top_k=40
        )

        top_recommendations = []
        for _, r in scored_df.iterrows():
            reasons = recommendation_engine.explain_place(r["id"], scored_df, feat_mat)
            top_recommendations.append({
                "place_id": r["id"],
                "name": r["name"],
                "category": r["category"],
                "personalization_score": float(r["personalization_score"]),
                "baseline_score": float(r.get("baseline_score", 75.0)),
                "why_recommended": reasons
            })

        return {
            "top_recommendations": top_recommendations,
            "scored_places_df": scored_df,
            "feature_matrix": feat_mat,
            "count": len(top_recommendations)
        }

