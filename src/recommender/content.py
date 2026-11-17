import numpy as np
import pandas as pd
from typing import Dict, List, Optional
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

CATEGORIES = [
    "heritage",
    "nature",
    "beach",
    "temple",
    "adventure",
    "food",
    "shopping",
    "museum",
    "wildlife",
    "hill_station",
]


class ContentBasedRecommender:
    """
    Content-Based Recommender utilizing TF-IDF representations of tags,
    one-hot encoded place categories, and budget-band vectors.
    """

    def __init__(self):
        self.tfidf = TfidfVectorizer(token_pattern=r"(?u)\b\w+\b", stop_words="english")
        self.places_df: Optional[pd.DataFrame] = None
        self.place_features: Optional[np.ndarray] = None
        self.place_id_to_idx: Dict[str, int] = {}
        self.idx_to_place_id: Dict[int, str] = {}
        self.is_fitted: bool = False

    def _get_cost_band(self, cost: float) -> str:
        if cost <= 100:
            return "budget_low"
        elif cost <= 450:
            return "budget_medium"
        else:
            return "budget_luxury"

    def fit(self, places_df: pd.DataFrame) -> "ContentBasedRecommender":
        """
        Fit the vectorizer on place attributes and build place feature matrices.
        """
        self.places_df = places_df.copy().reset_index(drop=True)
        self.place_id_to_idx = {pid: idx for idx, pid in enumerate(self.places_df["id"])}
        self.idx_to_place_id = {idx: pid for idx, pid in enumerate(self.places_df["id"])}

        # Combine category, tags, and cost band into textual document
        docs = []
        for _, row in self.places_df.iterrows():
            cost_band = self._get_cost_band(row.get("avg_cost_inr", 0))
            doc = f"{row['category']} {row.get('tags', '')} {cost_band} {row['category']}"
            docs.append(doc)

        # Compute TF-IDF matrix
        tfidf_mat = self.tfidf.fit_transform(docs).toarray()

        # One-hot category representation
        cat_matrix = np.zeros((len(self.places_df), len(CATEGORIES)), dtype=np.float32)
        for i, row in self.places_df.iterrows():
            cat = row["category"]
            if cat in CATEGORIES:
                cat_matrix[i, CATEGORIES.index(cat)] = 1.0

        # Normalized rating feature
        ratings = (self.places_df["rating"].to_numpy().reshape(-1, 1) - 1.0) / 4.0

        # Concatenate TF-IDF + Category weights + Quality rating
        # We give strong weight to category matching
        self.place_features = np.hstack([cat_matrix * 2.0, tfidf_mat, ratings * 0.5])
        self.is_fitted = True
        return self

    def score_for_user_profile(
        self,
        category_weights: Dict[str, float],
        budget_level: str = "medium",
        user_tags: Optional[str] = None
    ) -> pd.Series:
        """
        Compute cosine similarity scores in [0, 1] between user preference vector and places.
        """
        if not self.is_fitted or self.places_df is None:
            raise ValueError("Recommender must be fitted before scoring.")

        # Construct user query document and vector
        cat_vec = np.zeros((1, len(CATEGORIES)), dtype=np.float32)
        query_words = []

        for cat, weight in category_weights.items():
            if cat in CATEGORIES:
                cat_vec[0, CATEGORIES.index(cat)] = weight
                if weight > 0.1:
                    query_words.extend([cat] * int(max(1, weight * 4)))

        budget_token = f"budget_{budget_level.lower()}"
        query_words.append(budget_token)
        if user_tags:
            query_words.append(user_tags)

        query_text = " ".join(query_words)
        query_tfidf = self.tfidf.transform([query_text]).toarray()

        # Target rating ideal (assume user seeks top-rated places)
        query_rating = np.array([[1.0]])

        user_query_vec = np.hstack([cat_vec * 2.0, query_tfidf, query_rating * 0.5])

        # Compute cosine similarity
        sims = cosine_similarity(user_query_vec, self.place_features)[0]
        # Normalize to [0, 1]
        min_v, max_v = sims.min(), sims.max()
        if max_v > min_v:
            normalized_scores = (sims - min_v) / (max_v - min_v)
        else:
            normalized_scores = np.full_like(sims, 0.5)

        return pd.Series(normalized_scores, index=self.places_df["id"])

