import json
import joblib
import numpy as np
import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score, accuracy_score, f1_score, confusion_matrix
from sklearn.ensemble import GradientBoostingRegressor
import lightgbm as lgb

from ml.data.generate_training_data import generate_predictor_training_data

MODEL_VERSION = "v2.0.0-synthetic-trained"


def train_and_save_predictors():
    models_dir = Path("models")
    results_dir = Path("results")
    models_dir.mkdir(parents=True, exist_ok=True)
    results_dir.mkdir(parents=True, exist_ok=True)

    print("Generating synthetic predictor training dataset (N=15,000)...")
    df = generate_predictor_training_data(15000)

    features = [
        "category", "hour", "day_of_week", "is_weekend", "is_holiday",
        "season", "temp_c", "rain_prob", "is_indoor", "base_popularity",
        "travelers", "transport_mode"
    ]
    categorical_features = ["category", "season", "transport_mode"]
    numerical_features = [f for f in features if f not in categorical_features]

    X = df[features]
    y_crowd = df["target_crowd_score"]
    y_cost = df["target_per_person_cost"]
    y_disruption = df["target_disruption_risk"]

    # Preprocessor
    preprocessor = ColumnTransformer(
        transformers=[
            ("cat", OneHotEncoder(handle_unknown="ignore", sparse_output=False), categorical_features),
            ("num", "passthrough", numerical_features)
        ]
    )

    X_transformed = preprocessor.fit_transform(X)

    # 1. TRAIN CROWD REGRESSOR (LightGBM)
    print("\nTraining Crowd Density Regressor (LightGBM)...")
    X_tr, X_te, y_tr, y_te = train_test_split(X_transformed, y_crowd, test_size=0.2, random_state=42)
    crowd_model = lgb.LGBMRegressor(
        n_estimators=100, learning_rate=0.08, num_leaves=31, random_state=42, verbose=-1
    )
    crowd_model.fit(X_tr, y_tr)
    preds_crowd = crowd_model.predict(X_te)
    mae_crowd = float(mean_absolute_error(y_te, preds_crowd))
    rmse_crowd = float(np.sqrt(mean_squared_error(y_te, preds_crowd)))
    r2_crowd = float(r2_score(y_te, preds_crowd))
    print(f" Crowd Model -> MAE: {mae_crowd:.3f}, RMSE: {rmse_crowd:.3f}, R2: {r2_crowd:.3f}")

    # 2. TRAIN COST REGRESSOR (Gradient Boosting)
    print("\nTraining Cost Regressor (Gradient Boosting)...")
    X_tr_c, X_te_c, y_tr_c, y_te_c = train_test_split(X_transformed, y_cost, test_size=0.2, random_state=42)
    cost_model = GradientBoostingRegressor(
        n_estimators=80, learning_rate=0.1, max_depth=5, random_state=42
    )
    cost_model.fit(X_tr_c, y_tr_c)
    preds_cost = cost_model.predict(X_te_c)
    mae_cost = float(mean_absolute_error(y_te_c, preds_cost))
    rmse_cost = float(np.sqrt(mean_squared_error(y_te_c, preds_cost)))
    r2_cost = float(r2_score(y_te_c, preds_cost))
    print(f" Cost Model -> MAE: {mae_cost:.2f} INR, RMSE: {rmse_cost:.2f} INR, R2: {r2_cost:.3f}")

    # 3. TRAIN DISRUPTION CLASSIFIER (LightGBM)
    print("\nTraining Disruption Classifier (LightGBM)...")
    label_map = {"Low": 0, "Medium": 1, "High": 2}
    inv_label_map = {0: "Low", 1: "Medium", 2: "High"}
    y_disrupt_enc = y_disruption.map(label_map)

    X_tr_d, X_te_d, y_tr_d, y_te_d = train_test_split(X_transformed, y_disrupt_enc, test_size=0.2, random_state=42)
    disruption_model = lgb.LGBMClassifier(
        n_estimators=80, learning_rate=0.08, num_leaves=25, random_state=42, verbose=-1
    )
    disruption_model.fit(X_tr_d, y_tr_d)
    preds_d = disruption_model.predict(X_te_d)
    acc_d = float(accuracy_score(y_te_d, preds_d))
    f1_d = float(f1_score(y_te_d, preds_d, average="macro"))
    cm = confusion_matrix(y_te_d, preds_d).tolist()
    print(f" Disruption Classifier -> Accuracy: {acc_d:.4f}, Macro-F1: {f1_d:.4f}")

    # Save artifacts
    print("\nPersisting trained model artifacts to models/...")
    joblib.dump(crowd_model, models_dir / "crowd_model.joblib")
    joblib.dump(cost_model, models_dir / "cost_model.joblib")
    joblib.dump(disruption_model, models_dir / "disruption_model.joblib")
    joblib.dump(preprocessor, models_dir / "predictor_preprocessor.joblib")

    # Save metrics JSON
    metrics_report = {
        "model_version": MODEL_VERSION,
        "data_source": "Model trained on synthetic data",
        "training_samples": len(df),
        "crowd_regressor": {
            "algorithm": "LightGBM Regressor",
            "MAE": round(mae_crowd, 4),
            "RMSE": round(rmse_crowd, 4),
            "R2": round(r2_crowd, 4)
        },
        "cost_regressor": {
            "algorithm": "GradientBoosting Regressor",
            "MAE": round(mae_cost, 4),
            "RMSE": round(rmse_cost, 4),
            "R2": round(r2_cost, 4)
        },
        "disruption_classifier": {
            "algorithm": "LightGBM Classifier",
            "accuracy": round(acc_d, 4),
            "macro_f1": round(f1_d, 4),
            "confusion_matrix": cm,
            "classes": ["Low", "Medium", "High"]
        }
    }

    metrics_path = results_dir / "predictors_metrics.json"
    with open(metrics_path, "w", encoding="utf-8") as f:
        json.dump(metrics_report, f, indent=2)
    print(f" Saved predictors evaluation report to {metrics_path}")


if __name__ == "__main__":
    train_and_save_predictors()

