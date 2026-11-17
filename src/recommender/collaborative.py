import numpy as np
import pandas as pd
from typing import Dict, List, Optional, Tuple
from sklearn.decomposition import TruncatedSVD


class CollaborativeRecommender:
    """
    SVD-style Matrix Factorization collaborative filtering recommender.
    Decomposes the sparse user-item interaction matrix into latent factor representations.
    """

    def __init__(self, n_components: int = 20, random_state: int = 42):
        self.n_components = n_components
        self.random_state = random_state
        self.svd: Optional[TruncatedSVD] = None

        self.global_mean: float = 3.5
        self.user_means: Dict[str, float] = {}
        self.place_means: Dict[str, float] = {}

        self.user_to_idx: Dict[str, int] = {}
        self.place_to_idx: Dict[str, int] = {}
        self.idx_to_place: Dict[int, str] = {}
        self.idx_to_user: Dict[int, str] = {}

        self.user_factors: Optional[np.ndarray] = None
        self.place_factors: Optional[np.ndarray] = None
        self.is_fitted: bool = False

    def fit(self, ratings_df: pd.DataFrame) -> "CollaborativeRecommender":
        """
        Fit TruncatedSVD on the mean-centered rating matrix.
        """
        self.global_mean = float(ratings_df["rating"].mean())

        # Compute user and place means
        self.user_means = ratings_df.groupby("user_id")["rating"].mean().to_dict()
        self.place_means = ratings_df.groupby("place_id")["rating"].mean().to_dict()

        unique_users = sorted(ratings_df["user_id"].unique())
        unique_places = sorted(ratings_df["place_id"].unique())

        self.user_to_idx = {uid: i for i, uid in enumerate(unique_users)}
        self.place_to_idx = {pid: i for i, pid in enumerate(unique_places)}
        self.idx_to_user = {i: uid for uid, i in self.user_to_idx.items()}
        self.idx_to_place = {i: pid for pid, i in self.place_to_idx.items()}

        n_users = len(unique_users)
        n_places = len(unique_places)

        # Construct sparse user-place matrix centered by user mean
        matrix = np.zeros((n_users, n_places), dtype=np.float32)
        for _, row in ratings_df.iterrows():
            u_idx = self.user_to_idx[row["user_id"]]
            p_idx = self.place_to_idx[row["place_id"]]
            u_mean = self.user_means[row["user_id"]]
            matrix[u_idx, p_idx] = float(row["rating"] - u_mean)

        actual_components = min(self.n_components, n_places - 1, n_users - 1)
        self.svd = TruncatedSVD(n_components=actual_components, random_state=self.random_state)
        self.user_factors = self.svd.fit_transform(matrix)  # Shape (n_users, n_components)
        self.place_factors = self.svd.components_.T          # Shape (n_places, n_components)

        self.is_fitted = True
        return self

    def predict(self, user_id: str, place_id: str) -> float:
        """Predict rating for a specific user and place."""
        if not self.is_fitted:
            raise ValueError("Collaborative model has not been fitted.")

        has_user = user_id in self.user_to_idx
        has_place = place_id in self.place_to_idx

        if not has_user and not has_place:
            return self.global_mean
        elif not has_user:
            return self.place_means.get(place_id, self.global_mean)
        elif not has_place:
            return self.user_means.get(user_id, self.global_mean)

        u_idx = self.user_to_idx[user_id]
        p_idx = self.place_to_idx[place_id]

        interaction = float(np.dot(self.user_factors[u_idx], self.place_factors[p_idx]))
        pred = self.user_means[user_id] + interaction
        return float(np.clip(pred, 1.0, 5.0))

    def predict_all_places(
        self,
        user_id: Optional[str] = None,
        places_df: Optional[pd.DataFrame] = None,
        user_ratings: Optional[Dict[str, float]] = None
    ) -> pd.Series:
        """
        Predict ratings for all places.
        If user_ratings dict is supplied (e.g. from UI interactive ratings), folds in user latent vector.
        """
        if not self.is_fitted or self.svd is None:
            raise ValueError("Collaborative model is not fitted.")

        place_ids = places_df["id"].tolist() if places_df is not None else list(self.place_to_idx.keys())
        preds = np.zeros(len(place_ids), dtype=np.float32)

        # Case 1: Active user with seed ratings supplied interactively (folding in)
        if user_ratings and len(user_ratings) > 0:
            user_mean = np.mean(list(user_ratings.values()))
            user_vec = np.zeros((1, len(self.place_to_idx)), dtype=np.float32)
            for pid, r in user_ratings.items():
                if pid in self.place_to_idx:
                    user_vec[0, self.place_to_idx[pid]] = float(r - user_mean)
            # Project into latent space using V^T
            folded_factors = self.svd.transform(user_vec)[0]  # (n_components,)

            for i, pid in enumerate(place_ids):
                if pid in self.place_to_idx:
                    p_idx = self.place_to_idx[pid]
                    inter = np.dot(folded_factors, self.place_factors[p_idx])
                    preds[i] = float(np.clip(user_mean + inter, 1.0, 5.0))
                else:
                    preds[i] = self.place_means.get(pid, self.global_mean)

        # Case 2: Existing user in training matrix
        elif user_id and user_id in self.user_to_idx:
            u_idx = self.user_to_idx[user_id]
            u_factors = self.user_factors[u_idx]
            u_mean = self.user_means[user_id]
            for i, pid in enumerate(place_ids):
                if pid in self.place_to_idx:
                    p_idx = self.place_to_idx[pid]
                    inter = np.dot(u_factors, self.place_factors[p_idx])
                    preds[i] = float(np.clip(u_mean + inter, 1.0, 5.0))
                else:
                    preds[i] = self.place_means.get(pid, self.global_mean)

        # Case 3: Completely cold-start user without any ratings
        else:
            for i, pid in enumerate(place_ids):
                preds[i] = self.place_means.get(pid, self.global_mean)

        # Normalize predicted ratings (1 to 5) to [0, 1] personalization score
        norm_scores = (preds - 1.0) / 4.0
        return pd.Series(norm_scores, index=place_ids)

