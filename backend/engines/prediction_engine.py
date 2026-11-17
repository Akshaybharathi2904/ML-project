import math
from abc import ABC, abstractmethod
from typing import Dict, Any, List, Optional
import numpy as np
import pandas as pd
import joblib
from backend.config import settings
from backend.schemas.schemas import PredictionFeatures, CrowdPredictionResult, CostPredictionResult, DisruptionPredictionResult, FeasibilityScoreResult


class PredictionProvider(ABC):
    @abstractmethod
    def predict_crowd(self, features: PredictionFeatures) -> CrowdPredictionResult:
        pass

    @abstractmethod
    def predict_cost(self, features: PredictionFeatures) -> CostPredictionResult:
        pass

    @abstractmethod
    def predict_disruption(self, features: PredictionFeatures) -> DisruptionPredictionResult:
        pass


class RuleBasedPredictionProvider(PredictionProvider):
    """Fallback rule-based prediction provider ensuring 100% service uptime."""

    def predict_crowd(self, features: PredictionFeatures) -> CrowdPredictionResult:
        hour = features.hour
        # Peak hours 11:00 to 13:00 and 16:00 to 19:00
        hour_factor = math.exp(-((hour - 12) ** 2) / 10.0) * 40.0 + math.exp(-((hour - 17.5) ** 2) / 8.0) * 35.0
        weekend_boost = 18.0 if features.is_weekend else 0.0
        pop_boost = features.base_popularity * 25.0
        score = max(5.0, min(95.0, 15.0 + hour_factor + weekend_boost + pop_boost))

        if score < 35.0:
            cat = "Low"
        elif score < 65.0:
            cat = "Moderate"
        elif score < 85.0:
            cat = "High"
        else:
            cat = "Very High"

        hourly = {h: round(max(5.0, min(95.0, 15.0 + (math.exp(-((h - 12) ** 2) / 10.0) * 40.0 + math.exp(-((h - 17.5) ** 2) / 8.0) * 35.0) + weekend_boost + pop_boost)), 1) for h in range(8, 22)}

        return CrowdPredictionResult(
            crowd_score=round(score, 1),
            category=cat,
            hourly_curve=hourly,
            best_visiting_time="08:30 AM - 10:00 AM (Early Morning)" if score > 50 else "Anytime",
            confidence=0.82,
            explanation=f"Rule-based estimation based on {features.category} attraction popularity and hour {hour}:00 peak curve.",
            data_source="Rule-Based Prediction Fallback",
            model_version="v2.0.0-rule-fallback"
        )

    def predict_cost(self, features: PredictionFeatures) -> CostPredictionResult:
        base_ticket = 100.0 if features.category in ["heritage", "museum"] else (800.0 if features.category == "adventure" else 50.0)
        food_per_person = 250.0
        transport_cost = {"walking": 0.0, "public": 50.0, "mixed": 100.0, "own_vehicle": 150.0, "taxi": 300.0}.get(features.transport_mode, 150.0)
        per_person = base_ticket + food_per_person + transport_cost
        total = per_person * max(1, features.group_size)

        breakdown = {
            "tickets": round(base_ticket * features.group_size, 2),
            "food": round(food_per_person * features.group_size, 2),
            "transport": round(transport_cost, 2),
            "activities_misc": round(50.0 * features.group_size, 2),
        }

        return CostPredictionResult(
            total_cost_inr=round(total, 2),
            per_person_inr=round(per_person, 2),
            breakdown=breakdown,
            known_vs_estimated="Estimated from baseline price tiers",
            budget_utilization_pct=15.0,
            confidence=0.80,
            data_source="Rule-Based Prediction Fallback",
            model_version="v2.0.0-rule-fallback"
        )

    def predict_disruption(self, features: PredictionFeatures) -> DisruptionPredictionResult:
        if features.rain_probability > 0.6 and not features.is_indoor:
            level = "High"
            prob = 0.85
            reason = "High rain probability during scheduled outdoor activity"
            action = "Shift activity to morning slot or swap for an indoor museum/cafe alternative"
        elif features.rain_probability > 0.35 and not features.is_indoor:
            level = "Medium"
            prob = 0.50
            reason = "Moderate precipitation probability"
            action = "Carry waterproof gear and monitor real-time weather updates"
        else:
            level = "Low"
            prob = 0.15
            reason = "Clear operational window with minimal disruption indicators"
            action = "Proceed as scheduled"

        return DisruptionPredictionResult(
            risk_level=level,
            risk_score=round(prob * 100.0, 1),
            probability=round(prob, 2),
            primary_reason=reason,
            suggested_action=action,
            data_source="Rule-Based Disruption Engine",
            model_version="v2.0.0-rule-fallback"
        )


class MLModelPredictionProvider(PredictionProvider):
    """Production provider loading trained GBDT and LightGBM models."""

    def __init__(self):
        self.models_dir = settings.MODELS_DIR
        self.crowd_model = None
        self.cost_model = None
        self.disruption_model = None
        self.preprocessor = None
        self.is_loaded = False
        self.fallback = RuleBasedPredictionProvider()
        self._load_models()

    def _load_models(self):
        try:
            crowd_p = self.models_dir / "crowd_model.joblib"
            cost_p = self.models_dir / "cost_model.joblib"
            disrupt_p = self.models_dir / "disruption_model.joblib"
            prep_p = self.models_dir / "predictor_preprocessor.joblib"

            if crowd_p.exists() and cost_p.exists() and disrupt_p.exists() and prep_p.exists():
                self.crowd_model = joblib.load(crowd_p)
                self.cost_model = joblib.load(cost_p)
                self.disruption_model = joblib.load(disrupt_p)
                self.preprocessor = joblib.load(prep_p)
                self.is_loaded = True
        except Exception:
            self.is_loaded = False

    def _prepare_df(self, features: PredictionFeatures) -> pd.DataFrame:
        row = {
            "category": features.category,
            "hour": features.hour,
            "day_of_week": features.day_of_week,
            "is_weekend": 1 if features.is_weekend else 0,
            "is_holiday": 0,
            "season": "winter",
            "temp_c": features.temperature_c,
            "rain_prob": features.rain_probability,
            "is_indoor": 1 if features.is_indoor else 0,
            "base_popularity": features.base_popularity,
            "travelers": features.group_size,
            "transport_mode": features.transport_mode,
        }
        return pd.DataFrame([row])

    def predict_crowd(self, features: PredictionFeatures) -> CrowdPredictionResult:
        if not self.is_loaded or self.crowd_model is None:
            return self.fallback.predict_crowd(features)

        df = self._prepare_df(features)
        X_t = self.preprocessor.transform(df)
        pred_val = float(np.clip(self.crowd_model.predict(X_t)[0], 5.0, 98.0))

        cat = "Low" if pred_val < 35.0 else ("Moderate" if pred_val < 65.0 else ("High" if pred_val < 85.0 else "Very High"))

        # Hourly curve
        hourly = {}
        for h in range(8, 22):
            df_h = df.copy()
            df_h["hour"] = h
            X_th = self.preprocessor.transform(df_h)
            hourly[h] = round(float(np.clip(self.crowd_model.predict(X_th)[0], 5.0, 98.0)), 1)

        best_h = min(hourly.items(), key=lambda x: x[1])[0]

        return CrowdPredictionResult(
            crowd_score=round(pred_val, 1),
            category=cat,
            hourly_curve=hourly,
            best_visiting_time=f"{best_h:02d}:00 - {best_h+1:02d}:00 (Least Crowded)",
            confidence=0.91,
            explanation=f"LightGBM prediction based on {features.category} category, weekend status, and hour {features.hour}.",
            data_source="Model trained on synthetic data",
            model_version="v2.0.0-synthetic-trained"
        )

    def predict_cost(self, features: PredictionFeatures) -> CostPredictionResult:
        if not self.is_loaded or self.cost_model is None:
            return self.fallback.predict_cost(features)

        df = self._prepare_df(features)
        X_t = self.preprocessor.transform(df)
        per_person = float(max(50.0, self.cost_model.predict(X_t)[0]))
        total = per_person * max(1, features.group_size)

        breakdown = {
            "tickets": round(per_person * 0.45 * features.group_size, 2),
            "food": round(per_person * 0.30 * features.group_size, 2),
            "transport": round(per_person * 0.15 * features.group_size, 2),
            "activities_misc": round(per_person * 0.10 * features.group_size, 2),
        }

        return CostPredictionResult(
            total_cost_inr=round(total, 2),
            per_person_inr=round(per_person, 2),
            breakdown=breakdown,
            known_vs_estimated="Estimated by GradientBoosting Regressor",
            budget_utilization_pct=round((total / 12000.0) * 100.0, 1),
            confidence=0.88,
            data_source="Model trained on synthetic data",
            model_version="v2.0.0-synthetic-trained"
        )

    def predict_disruption(self, features: PredictionFeatures) -> DisruptionPredictionResult:
        if not self.is_loaded or self.disruption_model is None:
            return self.fallback.predict_disruption(features)

        df = self._prepare_df(features)
        X_t = self.preprocessor.transform(df)
        pred_class = int(self.disruption_model.predict(X_t)[0])
        probs = self.disruption_model.predict_proba(X_t)[0]

        class_map = {0: "Low", 1: "Medium", 2: "High"}
        level = class_map.get(pred_class, "Low")
        prob_val = float(probs[pred_class])

        if level == "High":
            reason = "Severe weather disruption risk predicted for outdoor scheduled stops"
            action = "Automated replanning recommended: swap for indoor alternative"
        elif level == "Medium":
            reason = "Moderate risk of crowd bottleneck or weather slowdown"
            action = "Monitor condition alerts and maintain flexible transit buffers"
        else:
            reason = "Minimal disruption indicators detected"
            action = "Proceed with scheduled itinerary"

        return DisruptionPredictionResult(
            risk_level=level,
            risk_score=round(prob_val * 100.0, 1),
            probability=round(prob_val, 2),
            primary_reason=reason,
            suggested_action=action,
            data_source="Model trained on synthetic data",
            model_version="v2.0.0-synthetic-trained"
        )


def compute_trip_feasibility_score(
    weather_suitability: float,  # 0 to 100
    crowd_comfort: float,        # 0 to 100 (100 - crowd_score)
    travel_efficiency: float,    # 0 to 100
    budget_feasibility: float,   # 0 to 100
    activity_suitability: float, # 0 to 100
    schedule_feasibility: float, # 0 to 100
    disruption_risk: float       # 0 to 100 (100 - disruption_score)
) -> FeasibilityScoreResult:
    """
    Transparent mathematical formula calculating overall itinerary feasibility:
      Score = 0.20 * Weather + 0.15 * CrowdComfort + 0.15 * TravelEfficiency +
              0.15 * BudgetFeasibility + 0.15 * ActivitySuitability +
              0.10 * ScheduleFeasibility + 0.10 * DisruptionSafety
    """
    weights = {
        "weather": 0.20,
        "crowd": 0.15,
        "travel": 0.15,
        "budget": 0.15,
        "activity": 0.15,
        "schedule": 0.10,
        "disruption": 0.10
    }

    breakdown = {
        "weather_suitability": round(weather_suitability, 1),
        "crowd_comfort": round(crowd_comfort, 1),
        "travel_efficiency": round(travel_efficiency, 1),
        "budget_feasibility": round(budget_feasibility, 1),
        "activity_suitability": round(activity_suitability, 1),
        "schedule_feasibility": round(schedule_feasibility, 1),
        "disruption_safety": round(disruption_risk, 1)
    }

    total_score = (
        weights["weather"] * weather_suitability +
        weights["crowd"] * crowd_comfort +
        weights["travel"] * travel_efficiency +
        weights["budget"] * budget_feasibility +
        weights["activity"] * activity_suitability +
        weights["schedule"] * schedule_feasibility +
        weights["disruption"] * disruption_risk
    )

    total_score = max(10.0, min(100.0, total_score))

    if total_score >= 80.0:
        status = "Highly Feasible"
        exp = "Optimal itinerary with balanced travel times, safe weather windows, and comfortable budget margin."
    elif total_score >= 60.0:
        status = "Feasible with Minor Adjustments"
        exp = "Good overall plan; minor travel overhead or moderate afternoon weather risk detected."
    else:
        status = "Critical Issues Detected"
        exp = "High risk of schedule disruption, budget overspend, or adverse weather conditions."

    return FeasibilityScoreResult(
        overall_score=round(total_score, 1),
        status=status,
        breakdown=breakdown,
        explanation=exp
    )


# Active default prediction engine
ml_prediction_provider = MLModelPredictionProvider()
rule_prediction_provider = RuleBasedPredictionProvider()

