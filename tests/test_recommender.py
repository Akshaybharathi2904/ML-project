import pytest
import pandas as pd
import numpy as np
from src.recommender.content import ContentBasedRecommender
from src.recommender.collaborative import CollaborativeRecommender
from src.recommender.hybrid import HybridRecommender
from src.recommender.explain import RecommendationExplainer
from data.real_data_adapter import KaggleTourismDataAdapter, OpenTripMapAdapter


@pytest.fixture(scope="module")
def sample_data():
    places = pd.read_csv("data/processed/places.csv")
    users = pd.read_csv("data/processed/users.csv")
    ratings = pd.read_csv("data/processed/ratings.csv")
    return places, users, ratings


def test_content_recommender(sample_data):
    places, _, _ = sample_data
    cbr = ContentBasedRecommender().fit(places)
    scores = cbr.score_for_user_profile(
        category_weights={"heritage": 0.9, "temple": 0.7},
        budget_level="medium"
    )
    assert len(scores) == len(places)
    assert scores.min() >= 0.0
    assert scores.max() <= 1.0


def test_collaborative_recommender(sample_data):
    _, _, ratings = sample_data
    cf = CollaborativeRecommender(n_components=10).fit(ratings)
    # Test existing user
    pred = cf.predict("U0001", "P001")
    assert 1.0 <= pred <= 5.0

    # Test completely cold-start user
    cold_pred = cf.predict("UNSEEN_USER", "P001")
    assert 1.0 <= cold_pred <= 5.0


def test_hybrid_recommender_and_explainer(sample_data):
    places, users, ratings = sample_data
    hr = HybridRecommender()
    hr.fit(places, users, ratings)

    user_profile = {
        "id": "U0001",
        "pref_heritage": 0.8,
        "pref_nature": 0.5,
        "budget_level": "medium",
        "pace": "moderate",
    }
    scores_df, feat_df = hr.predict_personalization_scores(
        user_profile=user_profile,
        start_city="Bengaluru",
        travel_season="winter"
    )

    assert len(scores_df) == len(places)
    assert "personalization_score" in scores_df.columns
    assert (scores_df["personalization_score"] >= 0.0).all()
    assert (scores_df["personalization_score"] <= 1.0).all()

    # Explainer test
    explainer = RecommendationExplainer(hr)
    first_pid = scores_df.iloc[0]["id"]
    exp = explainer.explain_place(first_pid, scores_df, feat_df)
    assert "reasons" in exp
    assert len(exp["reasons"]) <= 3
    assert len(exp["reasons"]) > 0
    assert isinstance(exp["reasons"][0], str)


def test_data_adapter_validation():
    adapter = KaggleTourismDataAdapter()
    invalid_df = pd.DataFrame({"some_col": [1, 2]})
    with pytest.raises(ValueError):
        adapter.validate_schema(invalid_df)

