from typing import Dict, Any, List
from backend.services.weather_service import weather_service


class WeatherIntelligenceAgent:
    """Agent 2: Obtains weather forecasts, rain probability, outdoor suitability, and disruption windows."""

    async def execute(self, lat: float, lon: float, num_days: int = 3) -> Dict[str, Any]:
        forecasts = await weather_service.get_forecast(lat, lon, num_days=num_days)
        overall_suitability = sum(f["suitability_score"] for f in forecasts) / float(len(forecasts)) if forecasts else 80.0
        rainy_days = [f["date"] for f in forecasts if f.get("rain_probability_pct", 0) > 40.0]

        return {
            "forecasts": forecasts,
            "average_suitability": round(overall_suitability, 1),
            "rain_alert_days": rainy_days,
            "status": "Favorable" if overall_suitability >= 75.0 else ("Moderate" if overall_suitability >= 50.0 else "Disruptive")
        }

