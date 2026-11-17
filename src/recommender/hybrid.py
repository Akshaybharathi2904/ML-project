import numpy as np
import pandas as pd
import lightgbm as lgb
from typing import Dict, List, Optional, Tuple, Any
from src.recommender.content import ContentBasedRecommender, CATEGORIES
from src.recommender.collaborative import CollaborativeRecommender
from src.utils.geo import haversine_distance_km

BUDGET_MAP = {"low": 0, "medium": 1, "luxury": 2}
PACE_MAP = {"relaxed": 0, "moderate": 1, "packed": 2}

FEATURE_COLUMNS = [
    "content_score",
    "collab_score",
    "place_rating",
    "popularity",
    "crowd_level",
    "cost_match",
    "distance_from_start",
    "season_match",
    "user_budget_tier",
    "user_pace_tier",
    "category_match",
]


class HybridRecommender:
    """
    Hybrid Recommender System using LightGBM Gradient Boosted Decision Trees
    to combine Content-Based similarity, SVD Collaborative Filtering, and
    contextual trip constraints (budget, distance, season, pace).
    """

    def __init__(self, lgb_params: Optional[Dict[str, Any]] = None):
        self.lgb_params = lgb_params or {
            "objective": "regression",
            "metric": "rmse",
            "boosting_type": "gbdt",
            "n_estimators": 100,
            "learning_rate": 0.05,
            "num_leaves": 31,
            "random_state": 42,
            "verbose": -1,
        }
        self.content_model = ContentBasedRecommender()
        self.collab_model = CollaborativeRecommender(n_components=20)
        self.model: Optional[lgb.LGBMRegressor] = None

        self.places_df: Optional[pd.DataFrame] = None
        self.users_df: Optional[pd.DataFrame] = None
        self.city_coords: Dict[str, Tuple[float, float]] = {}
        self.is_fitted: bool = False

    def _compute_cost_match(self, place_cost: float, budget_level: str) -> float:
        """Score how appropriately a place cost aligns with the user budget level."""
        b = budget_level.lower()
        if b == "low":
            return 1.0 if place_cost <= 100 else max(0.0, 1.0 - (place_cost - 100) / 400.0)
        elif b == "medium":
            if place_cost <= 450:
                return 1.0
            else:
                return max(0.0, 1.0 - (place_cost - 450) / 800.0)
        else:  # luxury
            return 1.0

    def _compute_season_match(self, best_season: str, travel_season: str) -> float:
        """Compute match score between place best season and trip season."""
        if best_season == "all" or travel_season == "all":
            return 1.0
        return 1.0 if best_season.lower() == travel_season.lower() else 0.4

    def build_feature_vector(
        self,
        place: pd.Series,
        content_score: float,
        collab_score: float,
        user_profile: Dict[str, Any],
        start_lat: float,
        start_lon: float,
        travel_season: str = "winter"
    ) -> Dict[str, float]:
        """Build feature dictionary for a single user-place pair."""
        cat = place["category"]
        cat_match = float(user_profile.get(f"pref_{cat}", 0.1))
        cost_match = self._compute_cost_match(float(place["avg_cost_inr"]), user_profile.get("budget_level", "medium"))
        season_match = self._compute_season_match(place.get("best_season", "all"), travel_season)
        dist = haversine_distance_km(start_lat, start_lon, float(place["lat"]), float(place["lon"]))

        b_tier = BUDGET_MAP.get(str(user_profile.get("budget_level", "medium")).lower(), 1)
        p_tier = PACE_MAP.get(str(user_profile.get("pace", "moderate")).lower(), 1)

        return {
            "content_score": float(content_score),
            "collab_score": float(collab_score),
            "place_rating": float(place["rating"]),
            "popularity": float(place["popularity"]),
            "crowd_level": float(place["crowd_level"]),
            "cost_match": float(cost_match),
            "distance_from_start": float(dist),
            "season_match": float(season_match),
            "user_budget_tier": float(b_tier),
            "user_pace_tier": float(p_tier),
            "category_match": float(cat_match),
        }

    def fit(
        self,
        places_df: pd.DataFrame,
        users_df: pd.DataFrame,
        ratings_df: pd.DataFrame
    ) -> "HybridRecommender":
        """
        Train Content-Based, Collaborative, and LightGBM Hybrid ensemble.
        """
        self.places_df = places_df.copy().reset_index(drop=True)
        self.users_df = users_df.copy().reset_index(drop=True)

        # 1. Fit sub-models
        self.content_model.fit(self.places_df)
        self.collab_model.fit(ratings_df)

        # Precompute city centers
        city_groups = self.places_df.groupby("city")[["lat", "lon"]].mean()
        self.city_coords = {c: (r["lat"], r["lon"]) for c, r in city_groups.iterrows()}

        # 2. Build training tabular dataset
        places_dict = {r["id"]: r for _, r in self.places_df.iterrows()}
        users_dict = {r["id"]: r.to_dict() for _, r in self.users_df.iterrows()}

        # Precompute content scores for all unique users
        print("Precomputing sub-model scores for training tabular dataset...")
        user_content_scores: Dict[str, pd.Series] = {}
        for uid, udata in users_dict.items():
            cat_weights = {cat: float(udata.get(f"pref_{cat}", 0.1)) for cat in CATEGORIES}
            user_content_scores[uid] = self.content_model.score_for_user_profile(
                category_weights=cat_weights,
                budget_level=udata.get("budget_level", "medium")
            )

        X_rows = []
        y_targets = []

        # Subsample if ratings are very large to train quickly and reliably
        sample_ratings = ratings_df if len(ratings_df) <= 40000 else ratings_df.sample(40000, random_state=42)

        # Vectorized lookup for high-speed training feature construction
        uids = sample_ratings["user_id"].to_numpy()
        pids = sample_ratings["place_id"].to_numpy()
        targets = sample_ratings["rating"].to_numpy()

        for uid, pid, target in zip(uids, pids, targets):
            if uid not in users_dict or pid not in places_dict:
                continue

            place = places_dict[pid]
            user = users_dict[uid]

            cb_score = float(user_content_scores[uid].get(pid, 0.5))
            cf_pred = self.collab_model.predict(uid, pid)
            cf_score = (cf_pred - 1.0) / 4.0

            start_coord = self.city_coords.get(place["city"], (place["lat"], place["lon"]))

            feats = self.build_feature_vector(
                place=place,
                content_score=cb_score,
                collab_score=cf_score,
                user_profile=user,
                start_lat=start_coord[0],
                start_lon=start_coord[1],
                travel_season="winter"
            )
            X_rows.append(feats)
            y_targets.append(float(target))

        X_train = pd.DataFrame(X_rows)[FEATURE_COLUMNS]
        y_train = np.array(y_targets)

        print(f"Training LightGBM regressor on {len(X_train)} interactions...")
        self.model = lgb.LGBMRegressor(**self.lgb_params)
        self.model.fit(X_train, y_train)

        self.is_fitted = True
        return self

    def predict_personalization_scores(
        self,
        user_profile: Dict[str, Any],
        start_city: str = "Bengaluru",
        travel_season: str = "winter",
        user_seed_ratings: Optional[Dict[str, float]] = None
    ) -> Tuple[pd.DataFrame, pd.DataFrame]:
        """
        Predict personalization scores in [0, 1] for all places.
        
        Returns:
            scores_df: DataFrame with place id, name, category, and predicted 'personalization_score'
            feature_matrix_df: Exact feature inputs used by LightGBM (useful for SHAP explainability)
        """
        if not self.is_fitted or self.model is None or self.places_df is None:
            raise ValueError("Hybrid recommender has not been fitted.")

        # 1. Content scores
        cat_weights = {cat: float(user_profile.get(f"pref_{cat}", 0.1)) for cat in CATEGORIES}
        cb_scores = self.content_model.score_for_user_profile(
            category_weights=cat_weights,
            budget_level=user_profile.get("budget_level", "medium")
        )

        # 2. Collaborative scores with cold-start blending
        num_seed_ratings = len(user_seed_ratings) if user_seed_ratings else 0
        cf_scores = self.collab_model.predict_all_places(
            user_id=user_profile.get("id"),
            places_df=self.places_df,
            user_ratings=user_seed_ratings
        )

        # Dynamic blend weight: shifts toward collaborative as ratings increase
        cf_weight = min(1.0, num_seed_ratings / 5.0) if num_seed_ratings > 0 else 0.0

        # Start coordinates
        if start_city in self.city_coords:
            start_lat, start_lon = self.city_coords[start_city]
        else:
            start_lat = float(self.places_df["lat"].mean())
            start_lon = float(self.places_df["lon"].mean())

        # 3. Construct feature matrix for all places
        rows = []
        for _, place in self.places_df.iterrows():
            pid = place["id"]
            cb_val = float(cb_scores.get(pid, 0.5))
            cf_val = float(cf_scores.get(pid, 0.5))

            # Blend collaborative signal based on user rating history density
            blended_cf = (1.0 - cf_weight) * cb_val + cf_weight * cf_val

            feats = self.build_feature_vector(
                place=place,
                content_score=cb_val,
                collab_score=blended_cf,
                user_profile=user_profile,
                start_lat=start_lat,
                start_lon=start_lon,
                travel_season=travel_season
            )
            feats["place_id"] = pid
            rows.append(feats)

        feat_df = pd.DataFrame(rows)
        X_eval = feat_df[FEATURE_COLUMNS]

        # 4. Predict ratings with LightGBM
        raw_preds = self.model.predict(X_eval)

        # Normalize predicted ratings (typically ~2.0 - 5.0) to [0.0, 1.0] personalization score
        min_p, max_p = 1.0, 5.0
        norm_scores = np.clip((raw_preds - min_p) / (max_p - min_p), 0.0, 1.0)

        # Assemble output
        result_df = self.places_df.copy()
        result_df["content_score"] = feat_df["content_score"]
        result_df["collab_score"] = feat_df["collab_score"]
        result_df["predicted_rating"] = np.round(raw_preds, 2)
        result_df["personalization_score"] = np.round(norm_scores, 4)

        return result_df, X_eval
