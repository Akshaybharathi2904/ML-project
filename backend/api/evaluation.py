import json
from pathlib import Path
from fastapi import APIRouter
import pandas as pd
from backend.config import settings
from backend.schemas.schemas import StandardResponse

router = APIRouter(prefix="/evaluation", tags=["Evaluation"])


@router.get("/summary", response_model=StandardResponse)
def get_evaluation_summary():
    results_dir = settings.RESULTS_DIR
    
    # 1. Recommender Ablation
    rec_table_p = results_dir / "tables" / "recommender_ablation.csv"
    rec_data = []
    if rec_table_p.exists():
        rec_data = pd.read_csv(rec_table_p).to_dict(orient="records")

    # 2. Optimizer Benchmark
    opt_table_p = results_dir / "tables" / "optimizer_benchmark.csv"
    opt_data = []
    if opt_table_p.exists():
        opt_data = pd.read_csv(opt_table_p).to_dict(orient="records")

    # 3. End-to-End Satisfaction
    sat_table_p = results_dir / "tables" / "end_to_end_satisfaction.csv"
    sat_data = []
    if sat_table_p.exists():
        sat_data = pd.read_csv(sat_table_p).to_dict(orient="records")

    # 4. Predictors metrics
    pred_metrics_p = results_dir / "predictors_metrics.json"
    pred_data = {}
    if pred_metrics_p.exists():
        with open(pred_metrics_p, "r", encoding="utf-8") as f:
            pred_data = json.load(f)

    return StandardResponse(
        success=True,
        message="Comprehensive scientific evaluation metrics retrieved",
        data={
            "recommender_ablation": rec_data,
            "optimizer_benchmarks": opt_data,
            "end_to_end_satisfaction": sat_data,
            "predictor_models": pred_data
        },
        data_source="Offline Benchmarks (31,408 Ratings & 10 Optimization Seeds)"
    )


@router.get("/models/info", response_model=StandardResponse)
def get_models_info():
    return StandardResponse(
        success=True,
        message="Active models metadata",
        data={
            "models": [
                {
                    "name": "Hybrid LightGBM Ranker",
                    "version": "v2.0.0-blender",
                    "algorithm": "Gradient Boosted Decision Trees (GBDT)",
                    "purpose": "Personalization score prediction [0, 1] and SHAP explainability"
                },
                {
                    "name": "SVD Matrix Factorization",
                    "version": "v2.0.0-svd20",
                    "algorithm": "TruncatedSVD (20 Latent Components)",
                    "purpose": "Collaborative filtering peer interaction modeling with folding-in"
                },
                {
                    "name": "Crowd Density Regressor",
                    "version": "v2.0.0-synthetic-trained",
                    "algorithm": "LightGBM Regressor (R2: 0.950)",
                    "purpose": "Predicts attraction crowd score (0-100) and hourly profile"
                },
                {
                    "name": "Cost Regressor",
                    "version": "v2.0.0-synthetic-trained",
                    "algorithm": "GradientBoosting Regressor (R2: 0.784)",
                    "purpose": "Estimates per-person expenditure across tickets, food, transport"
                },
                {
                    "name": "Disruption Classifier",
                    "version": "v2.0.0-synthetic-trained",
                    "algorithm": "LightGBM Classifier (Accuracy: 0.994)",
                    "purpose": "Classifies weather/crowd disruption risk into Low/Medium/High"
                },
                {
                    "name": "NSGA-II Multi-Objective Optimizer",
                    "version": "v2.0.0-toptw-pymoo",
                    "algorithm": "NSGA-II with Domain Repair Operator",
                    "purpose": "Synthesizes Pareto optimal day-by-day itineraries"
                }
            ]
        },
        data_source="Trained Machine Learning Model Registry"
    )

