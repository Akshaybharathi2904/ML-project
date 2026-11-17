from datetime import datetime, timedelta
from typing import List, Dict, Any, Optional
import httpx
from backend.config import settings


class WeatherService:
    def __init__(self):
        self.base_url = "https://api.open-meteo.com/v1/forecast"

    def compute_suitability(self, temp_max: float, rain_prob_pct: float) -> Dict[str, Any]:
        """
        Deterministic formula for outdoor weather suitability (0-100 score).
        Penalizes heavy rain probability and extreme heat/cold.
        """
        # Rain penalty: 0% rain -> 0 penalty, 100% rain -> 65 point penalty
        rain_penalty = (rain_prob_pct / 100.0) * 65.0

        # Temperature comfort penalty (ideal is 21-28 C)
        temp_penalty = 0.0
        if temp_max > 28.0:
            temp_penalty = min(35.0, (temp_max - 28.0) * 3.5)
        elif temp_max < 18.0:
            temp_penalty = min(30.0, (18.0 - temp_max) * 3.0)

        score = max(5.0, min(100.0, 100.0 - rain_penalty - temp_penalty))

        if score >= 75.0:
            category = "Suitable"
            rec = "Pleasant weather conditions. Ideal for outdoor sightseeing and open-air activities."
            window = None
        elif score >= 50.0:
            category = "Moderate"
            rec = "Fair conditions with mild weather variance. Keep an umbrella or sun protection handy."
            window = "Possible midday or late afternoon rain"
        else:
            category = "Poor"
            rec = "Adverse conditions (heavy rain/excessive heat). Recommend prioritizing indoor museums, galleries, and cafes."
            window = "Rain disruption expected between 12:00 PM and 17:00 PM"

        return {
            "suitability_score": round(score, 1),
            "outdoor_suitability": category,
            "disruption_window": window,
            "recommendation": rec
        }

    async def get_forecast(self, lat: float, lon: float, num_days: int = 5) -> List[Dict[str, Any]]:
        """Fetch real-time weather from Open-Meteo with fallback to simulated data."""
        if not settings.MOCK_MODE:
            try:
                async with httpx.AsyncClient(timeout=4.0) as client:
                    resp = await client.get(
                        self.base_url,
                        params={
                            "latitude": lat,
                            "longitude": lon,
                            "daily": ["temperature_2m_max", "temperature_2m_min", "precipitation_probability_max", "weather_code"],
                            "timezone": "auto",
                            "forecast_days": min(num_days, 7)
                        }
                    )
                    if resp.status_code == 200:
                        data = resp.json().get("daily", {})
                        dates = data.get("time", [])
                        t_maxs = data.get("temperature_2m_max", [])
                        t_mins = data.get("temperature_2m_min", [])
                        rain_probs = data.get("precipitation_probability_max", [])

                        forecasts = []
                        for i in range(len(dates)):
                            t_max = float(t_maxs[i]) if i < len(t_maxs) else 26.0
                            t_min = float(t_mins[i]) if i < len(t_mins) else 18.0
                            r_prob = float(rain_probs[i]) if i < len(rain_probs) else 15.0

                            cond = "Sunny" if r_prob < 25.0 else ("Partly Cloudy" if r_prob < 50.0 else "Rain Showers")
                            eval_res = self.compute_suitability(t_max, r_prob)

                            forecasts.append({
                                "date": dates[i],
                                "temp_min_c": round(t_min, 1),
                                "temp_max_c": round(t_max, 1),
                                "rain_probability_pct": round(r_prob, 1),
                                "condition": cond,
                                "outdoor_suitability": eval_res["outdoor_suitability"],
                                "suitability_score": eval_res["suitability_score"],
                                "disruption_window": eval_res["disruption_window"],
                                "recommendation": eval_res["recommendation"],
                                "data_source": "Open-Meteo Live API"
                            })
                        if forecasts:
                            return forecasts
            except Exception:
                pass

        # Deterministic mock fallback (reproducible simulated weather)
        today = datetime.now()
        mock_forecasts = []
        for i in range(num_days):
            d_str = (today + timedelta(days=i)).strftime("%Y-%m-%d")
            # Deterministic variation
            r_prob = 15.0 if i != 1 else 68.0  # Day 2 has moderate rain for replanning test scenarios
            t_max = 28.0 - i * 0.5
            t_min = 18.0 - i * 0.3
            cond = "Scattered Showers" if r_prob > 50 else ("Clear Sky" if i % 2 == 0 else "Partly Cloudy")
            eval_res = self.compute_suitability(t_max, r_prob)

            mock_forecasts.append({
                "date": d_str,
                "temp_min_c": round(t_min, 1),
                "temp_max_c": round(t_max, 1),
                "rain_probability_pct": round(r_prob, 1),
                "condition": cond,
                "outdoor_suitability": eval_res["outdoor_suitability"],
                "suitability_score": eval_res["suitability_score"],
                "disruption_window": eval_res["disruption_window"],
                "recommendation": eval_res["recommendation"],
                "data_source": "Simulated Weather (Seeded)"
            })
        return mock_forecasts


weather_service = WeatherService()

