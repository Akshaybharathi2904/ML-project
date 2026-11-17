from typing import Dict, Any, List
from backend.engines.prediction_engine import ml_prediction_provider
from backend.schemas.schemas import PredictionFeatures


class PredictionAgent:
    """Agent 3: Predicts crowd levels, cost forecasts, and disruption probabilities using trained ML models."""

    def execute(self, destination: str, places: List[Dict[str, Any]], weather_info: Dict[str, Any]) -> Dict[str, Any]:
        forecasts = weather_info.get("forecasts", [])
        avg_rain = forecasts[0].get("rain_probability_pct", 15.0) / 100.0 if forecasts else 0.15
        avg_temp = forecasts[0].get("temp_max_c", 26.0) if forecasts else 26.0

        predictions_by_place = {}
        for p in places[:25]:
            feats = PredictionFeatures(
                destination=destination,
                category=p.get("category", "heritage"),
                hour=11,
                day_of_week=5,
                is_weekend=True,
                rain_probability=avg_rain,
                temperature_c=avg_temp,
                is_indoor=p.get("is_indoor", False),
                base_popularity=p.get("popularity", 0.7),
                group_size=2,
                transport_mode="taxi"
            )

            crowd = ml_prediction_provider.predict_crowd(feats)
            cost = ml_prediction_provider.predict_cost(feats)
            disrupt = ml_prediction_provider.predict_disruption(feats)

            predictions_by_place[p["id"]] = {
                "crowd": crowd.model_dump(),
                "cost": cost.model_dump(),
                "disruption": disrupt.model_dump(),
            }

        return {
            "place_predictions": predictions_by_place,
            "provider": "MLModelPredictionProvider (LightGBM & GBDT)",
            "data_source": "Model trained on synthetic data"
        }

