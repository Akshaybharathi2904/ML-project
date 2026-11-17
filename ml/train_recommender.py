import joblib
import pandas as pd
from pathlib import Path
from src.recommender.hybrid import HybridRecommender

MODEL_PATH = Path("models/hybrid_recommender.joblib")


def train_and_persist_recommender():
    models_dir = Path("models")
    models_dir.mkdir(parents=True, exist_ok=True)

    print("Loading processed dataset for Hybrid Recommender training...")
    places = pd.read_csv("data/processed/places.csv")
    users = pd.read_csv("data/processed/users.csv")
    ratings = pd.read_csv("data/processed/ratings.csv")

    print(f"Training Hybrid Recommender on {len(ratings)} interactions...")
    hybrid = HybridRecommender()
    hybrid.fit(places, users, ratings)

    joblib.dump(hybrid, MODEL_PATH)
    print(f" Saved Hybrid Recommender artifact to {MODEL_PATH}")


if __name__ == "__main__":
    train_and_persist_recommender()

