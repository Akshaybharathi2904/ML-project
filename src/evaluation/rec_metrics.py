import numpy as np
import pandas as pd
from typing import Dict, List, Tuple, Any
from sklearn.metrics import mean_squared_error, mean_absolute_error


def compute_rating_error_metrics(y_true: np.ndarray, y_pred: np.ndarray) -> Dict[str, float]:
    """Compute RMSE and MAE between true and predicted ratings."""
    rmse = float(np.sqrt(mean_squared_error(y_true, y_pred)))
    mae = float(mean_absolute_error(y_true, y_pred))
    return {"RMSE": round(rmse, 4), "MAE": round(mae, 4)}


def compute_ranking_metrics_at_k(
    user_test_ratings: pd.DataFrame,
    predicted_scores_df: pd.DataFrame,
    k: int = 10,
    relevance_threshold: float = 4.0
) -> Dict[str, float]:
    """
    Compute Precision@K, Recall@K, and NDCG@K across all evaluated users.
    
    Args:
        user_test_ratings: DataFrame with 'user_id', 'place_id', 'rating'.
        predicted_scores_df: DataFrame with 'user_id', 'place_id', 'score'.
        k: Cut-off rank.
        relevance_threshold: Rating threshold to define binary relevance.
    """
    precisions = []
    recalls = []
    ndcgs = []

    # Group by user
    test_grouped = user_test_ratings.groupby("user_id")
    pred_grouped = predicted_scores_df.groupby("user_id")

    # Discount vector for DCG
    discounts = 1.0 / np.log2(np.arange(2, k + 2))

    for uid, test_group in test_grouped:
        # Ground truth relevant items
        relevant_pids = set(test_group[test_group["rating"] >= relevance_threshold]["place_id"])
        if len(relevant_pids) == 0:
            continue

        if uid not in pred_grouped.groups:
            continue

        u_preds = pred_grouped.get_group(uid).sort_values(by="score", ascending=False)
        top_k_pids = u_preds["place_id"].head(k).tolist()

        # Hits
        hits = [1 if pid in relevant_pids else 0 for pid in top_k_pids]
        num_hits = sum(hits)

        # Precision@K & Recall@K
        prec = num_hits / float(k)
        rec = num_hits / float(len(relevant_pids))

        # DCG@K
        dcg = np.sum(np.array(hits[:len(discounts)]) * discounts[:len(hits)])

        # Ideal DCG@K
        n_rel_in_k = min(k, len(relevant_pids))
        idcg = np.sum(discounts[:n_rel_in_k])
        ndcg = dcg / idcg if idcg > 0 else 0.0

        precisions.append(prec)
        recalls.append(rec)
        ndcgs.append(ndcg)

    return {
        f"Precision@{k}": round(float(np.mean(precisions)), 4) if precisions else 0.0,
        f"Recall@{k}": round(float(np.mean(recalls)), 4) if recalls else 0.0,
        f"NDCG@{k}": round(float(np.mean(ndcgs)), 4) if ndcgs else 0.0,
    }

