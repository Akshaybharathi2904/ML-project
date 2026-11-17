import numpy as np
import pandas as pd
import shap
from typing import Dict, List, Any, Optional, Tuple
import plotly.graph_objects as go
from src.recommender.hybrid import HybridRecommender, FEATURE_COLUMNS


FEATURE_DESCRIPTIONS = {
    "content_score": "Content-Based Interest Match",
    "collab_score": "Collaborative Traveler Peer Rating",
    "place_rating": "Place Historic Review Score",
    "popularity": "Overall Landmark Popularity",
    "crowd_level": "Serenity & Low Crowd Factor",
    "cost_match": "Budget Compatibility",
    "distance_from_start": "Proximity to Start City",
    "season_match": "Seasonal Alignment",
    "user_budget_tier": "Traveler Budget Band",
    "user_pace_tier": "Itinerary Travel Pace",
    "category_match": "Specific Category Affinity",
}


class RecommendationExplainer:
    """
    SHAP TreeExplainer wrapper providing local and global feature attribution
    and generating plain English 'Why this place?' reasons.
    """

    def __init__(self, hybrid_recommender: HybridRecommender):
        self.hybrid = hybrid_recommender
        if self.hybrid.model is None:
            raise ValueError("Hybrid recommender must be fitted before creating explainer.")
        
        # Initialize TreeExplainer
        self.explainer = shap.TreeExplainer(self.hybrid.model)

    def explain_place(
        self,
        place_id: str,
        places_df: pd.DataFrame,
        feature_df: pd.DataFrame
    ) -> Dict[str, Any]:
        """
        Compute SHAP values and top-3 plain English reasons for a given recommended place.
        """
        match_indices = places_df.index[places_df["id"] == place_id].tolist()
        if not match_indices:
            return {
                "place_id": place_id,
                "reasons": ["Top recommended attraction matching regional highlights."],
                "shap_values": {},
            }

        idx = match_indices[0]
        row_features = feature_df.iloc[[idx]][FEATURE_COLUMNS]
        place_meta = places_df.iloc[idx]

        # Calculate SHAP values
        raw_shap = self.explainer.shap_values(row_features)
        if isinstance(raw_shap, list):
            shap_vals = raw_shap[0][0]
        elif len(raw_shap.shape) == 2:
            shap_vals = raw_shap[0]
        else:
            shap_vals = raw_shap

        feature_impact = {col: float(shap_vals[i]) for i, col in enumerate(FEATURE_COLUMNS)}

        # Sort features by highest positive impact on the rating prediction
        sorted_pos = sorted(feature_impact.items(), key=lambda x: x[1], reverse=True)

        # Generate human-readable narrative reasons
        reasons: List[str] = []
        for feat, imp in sorted_pos:
            if len(reasons) >= 3:
                break

            cat_name = str(place_meta.get("category", "sightseeing")).capitalize()

            if feat == "category_match":
                reasons.append(f"Strongly matches your selected affinity for {cat_name} experiences.")
            elif feat == "content_score":
                reasons.append(f"Tags and thematic profile align closely with your travel interests.")
            elif feat == "place_rating":
                reasons.append(f"Exceptional visitor rating of {place_meta.get('rating', 4.5):.1f}/5.0 stars.")
            elif feat == "cost_match":
                reasons.append(f"Admission cost (INR {place_meta.get('avg_cost_inr', 0):.0f}) fits your budget.")
            elif feat == "popularity":
                reasons.append(f"Celebrated regional landmark with high visitor acclaim.")
            elif feat == "distance_from_start":
                reasons.append(f"Geographically accessible relative to your travel route.")
            elif feat == "collab_score":
                reasons.append(f"Highly favored by travelers with similar visit histories.")
            elif feat == "season_match":
                reasons.append(f"Optimal seasonal weather conditions for sightseeing.")
            elif feat == "crowd_level":
                reasons.append(f"Favorable crowd density offering a pleasant experience.")

        if not reasons:
            reasons.append("Balanced blend of scenic appeal, high quality, and budget alignment.")

        return {
            "place_id": place_id,
            "place_name": place_meta.get("name", place_id),
            "reasons": reasons,
            "feature_impact": feature_impact,
            "base_value": float(self.explainer.expected_value if not isinstance(self.explainer.expected_value, np.ndarray) else self.explainer.expected_value[0]),
        }

    def generate_shap_waterfall_fig(
        self,
        place_id: str,
        places_df: pd.DataFrame,
        feature_df: pd.DataFrame
    ) -> go.Figure:
        """
        Create an interactive Plotly horizontal bar chart showing SHAP contributions.
        """
        explanation = self.explain_place(place_id, places_df, feature_df)
        impacts = explanation["feature_impact"]

        # Sort by absolute impact
        sorted_items = sorted(impacts.items(), key=lambda x: abs(x[1]), reverse=False)
        labels = [FEATURE_DESCRIPTIONS.get(k, k) for k, _ in sorted_items]
        values = [v for _, v in sorted_items]
        colors = ["#2ecc71" if v >= 0 else "#e74c3c" for v in values]

        fig = go.Figure(
            go.Bar(
                x=values,
                y=labels,
                orientation="h",
                marker_color=colors,
                text=[f"{v:+.3f}" for v in values],
                textposition="auto",
            )
        )
        place_name = explanation["place_name"]
        fig.update_layout(
            title=f"SHAP Feature Attribution: {place_name}",
            xaxis_title="Impact on Personalization Score (SHAP value)",
            yaxis_title="Feature",
            margin=dict(l=20, r=20, t=40, b=20),
            height=380,
            template="plotly_white",
        )
        return fig

