import numpy as np
import pandas as pd
from pathlib import Path

# Deterministic seed for scientific reproducibility
RANDOM_SEED = 42
np.random.seed(RANDOM_SEED)

CATEGORIES = ["heritage", "nature", "beach", "temple", "adventure", "food", "shopping", "museum", "wildlife", "spiritual"]
TRANSPORT_MODES = ["own_vehicle", "taxi", "public", "walking", "mixed"]
SEASONS = ["winter", "monsoon", "summer"]


def generate_predictor_training_data(n_samples: int = 15000) -> pd.DataFrame:
    """
    Generative process for travel conditions across India.
    Generates realistic features and labels for crowd density, cost breakdown, and disruption risk.
    """
    rows = []

    for i in range(n_samples):
        cat = np.random.choice(CATEGORIES)
        hour = np.random.randint(6, 22)  # 06:00 to 22:00
        day_of_week = np.random.randint(0, 7)  # 0: Monday, 6: Sunday
        is_weekend = 1 if day_of_week in [5, 6] else 0
        is_holiday = 1 if np.random.rand() < 0.08 else 0
        season = np.random.choice(SEASONS, p=[0.5, 0.2, 0.3])
        temp_c = np.random.uniform(12.0, 38.0)
        rain_prob = np.random.uniform(0.0, 1.0)
        is_indoor = 1 if cat in ["museum", "food", "shopping"] or (cat == "heritage" and np.random.rand() < 0.4) else 0
        base_pop = np.random.uniform(0.2, 1.0)
        travelers = np.random.choice([1, 2, 3, 4, 6], p=[0.25, 0.4, 0.15, 0.15, 0.05])
        transport = np.random.choice(TRANSPORT_MODES, p=[0.3, 0.35, 0.15, 0.05, 0.15])

        # ---------------------------------------------
        # 1. GENERATIVE GROUND TRUTH: CROWD SCORE (0-100)
        # Peak hours 10-13 and 16-19; higher on weekends/holidays and high popularity
        # ---------------------------------------------
        hour_factor = np.exp(-((hour - 11.5) ** 2) / 12.0) * 35.0 + np.exp(-((hour - 17.5) ** 2) / 8.0) * 30.0
        weekend_boost = 18.0 if is_weekend else 0.0
        holiday_boost = 22.0 if is_holiday else 0.0
        pop_boost = base_pop * 30.0
        weather_penalty = -25.0 * rain_prob if is_indoor == 0 else 0.0
        noise = np.random.normal(0, 4.0)

        crowd_score = np.clip(10.0 + hour_factor + weekend_boost + holiday_boost + pop_boost + weather_penalty + noise, 5.0, 98.0)

        # ---------------------------------------------
        # 2. GENERATIVE GROUND TRUTH: PER-PERSON COST (INR)
        # ---------------------------------------------
        if cat in ["food"]:
            base_ticket = 0
            activity_cost = np.random.choice([150, 300, 500, 800])
        elif cat in ["adventure"]:
            base_ticket = np.random.choice([200, 500, 800, 1500])
            activity_cost = np.random.choice([500, 1000, 1800])
        elif cat in ["temple", "spiritual"]:
            base_ticket = np.random.choice([0, 20, 50, 100])
            activity_cost = 50
        elif cat in ["museum", "heritage"]:
            base_ticket = np.random.choice([50, 100, 250, 450])
            activity_cost = 100
        else:
            base_ticket = np.random.choice([0, 50, 150, 250])
            activity_cost = 150

        transport_multiplier = {"walking": 0.0, "public": 40.0, "mixed": 100.0, "own_vehicle": 150.0, "taxi": 300.0}[transport]
        food_est = 250.0 if hour in [12, 13, 14, 19, 20, 21] else 80.0
        misc = 50.0

        per_person_cost = float(base_ticket + activity_cost + transport_multiplier + food_est + misc + np.random.normal(0, 25.0))
        per_person_cost = max(50.0, round(per_person_cost, 2))

        # ---------------------------------------------
        # 3. GENERATIVE GROUND TRUTH: DISRUPTION RISK
        # High rain + outdoor -> High Risk; extreme heat -> Medium Risk
        # ---------------------------------------------
        if rain_prob > 0.65 and is_indoor == 0:
            risk_label = "High"
            risk_prob = np.clip(0.7 + (rain_prob - 0.65), 0.7, 0.98)
        elif (rain_prob > 0.35 and is_indoor == 0) or (temp_c > 37.0 and is_indoor == 0) or (crowd_score > 90.0):
            risk_label = "Medium"
            risk_prob = np.random.uniform(0.4, 0.68)
        else:
            risk_label = "Low"
            risk_prob = np.random.uniform(0.05, 0.35)

        rows.append({
            "category": cat,
            "hour": hour,
            "day_of_week": day_of_week,
            "is_weekend": is_weekend,
            "is_holiday": is_holiday,
            "season": season,
            "temp_c": round(temp_c, 1),
            "rain_prob": round(rain_prob, 3),
            "is_indoor": is_indoor,
            "base_popularity": round(base_pop, 2),
            "travelers": travelers,
            "transport_mode": transport,
            # Targets
            "target_crowd_score": round(crowd_score, 1),
            "target_per_person_cost": per_person_cost,
            "target_disruption_risk": risk_label,
            "target_disruption_prob": round(risk_prob, 3)
        })

    df = pd.DataFrame(rows)
    return df


if __name__ == "__main__":
    out_dir = Path("ml/data")
    out_dir.mkdir(parents=True, exist_ok=True)
    df = generate_predictor_training_data(15000)
    csv_path = out_dir / "predictor_training_data.csv"
    df.to_csv(csv_path, index=False)
    print(f"Generated {len(df)} synthetic training records in {csv_path}")

