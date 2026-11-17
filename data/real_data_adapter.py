"""
Real Data Adapter Interface.

Provides a unified contract for integrating external, real-world tourism datasets
(e.g., OpenTripMap API, Foursquare POI API, Kaggle Tourism datasets) into the system
without altering downstream recommender, optimizer, or UI pipelines.
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional
import pandas as pd
import numpy as np

REQUIRED_PLACE_COLUMNS = [
    "id",
    "name",
    "city",
    "lat",
    "lon",
    "category",
    "avg_cost_inr",
    "avg_visit_duration_min",
    "rating",
    "popularity",
    "crowd_level",
    "open_time",
    "close_time",
    "best_season",
    "tags",
]

CANONICAL_CATEGORIES = [
    "heritage",
    "nature",
    "beach",
    "temple",
    "adventure",
    "food",
    "shopping",
    "museum",
    "wildlife",
    "hill_station",
]


class BaseDataAdapter(ABC):
    """Abstract base class for all tourism data adapters."""

    @abstractmethod
    def fetch_places(self, **kwargs) -> pd.DataFrame:
        """Fetch places and transform into the standard system schema."""
        pass

    @abstractmethod
    def fetch_ratings(self, **kwargs) -> pd.DataFrame:
        """Fetch user-place ratings and transform into user_id, place_id, rating."""
        pass

    def validate_schema(self, places_df: pd.DataFrame) -> bool:
        """Verify that all required columns are present and properly typed."""
        missing = [col for col in REQUIRED_PLACE_COLUMNS if col not in places_df.columns]
        if missing:
            raise ValueError(f"Dataset is missing required columns: {missing}")

        # Check types and range bounds
        if places_df["lat"].isnull().any() or places_df["lon"].isnull().any():
            raise ValueError("Latitude and Longitude cannot contain null values.")
        if not (places_df["rating"].between(1.0, 5.0) | places_df["rating"].isnull()).all():
            raise ValueError("Ratings must be between 1.0 and 5.0.")

        return True


class KaggleTourismDataAdapter(BaseDataAdapter):
    """
    Adapter for tabular CSV datasets from Kaggle / TripAdvisor / Google Local POIs.
    Maps arbitrary column aliases to canonical schema.
    """

    def __init__(self, column_mapping: Optional[Dict[str, str]] = None):
        self.column_mapping = column_mapping or {
            "Place_Id": "id",
            "Place_Name": "name",
            "City": "city",
            "Latitude": "lat",
            "Longitude": "lon",
            "Category": "category",
            "Price": "avg_cost_inr",
            "Time_Minutes": "avg_visit_duration_min",
            "Rating": "rating",
            "Popularity": "popularity",
            "Crowd": "crowd_level",
            "Opening_Time": "open_time",
            "Closing_Time": "close_time",
            "Season": "best_season",
            "Tags": "tags",
        }

    def fetch_places(self, file_path: str, **kwargs) -> pd.DataFrame:
        """Load external CSV file and harmonize columns."""
        df = pd.read_csv(file_path)
        rename_dict = {k: v for k, v in self.column_mapping.items() if k in df.columns}
        df = df.rename(columns=rename_dict)

        # Impute defaults if optional columns are absent in source CSV
        if "popularity" not in df.columns:
            df["popularity"] = (df["rating"] / 5.0).clip(0.1, 1.0)
        if "crowd_level" not in df.columns:
            df["crowd_level"] = 0.5
        if "open_time" not in df.columns:
            df["open_time"] = "09:00"
        if "close_time" not in df.columns:
            df["close_time"] = "18:00"
        if "best_season" not in df.columns:
            df["best_season"] = "all"
        if "tags" not in df.columns:
            df["tags"] = df["category"].astype(str)

        self.validate_schema(df)
        return df[REQUIRED_PLACE_COLUMNS]

    def fetch_ratings(self, file_path: str, **kwargs) -> pd.DataFrame:
        """Load ratings file and format."""
        df = pd.read_csv(file_path)
        cols = {"User_Id": "user_id", "Place_Id": "place_id", "Rating": "rating"}
        df = df.rename(columns={k: v for k, v in cols.items() if k in df.columns})
        return df[["user_id", "place_id", "rating"]]


class OpenTripMapAdapter(BaseDataAdapter):
    """
    Adapter for OpenTripMap REST API JSON responses.
    Demonstrates live API integration capability.
    """

    def fetch_places(self, raw_features: List[Dict[str, Any]], city_name: str = "CustomCity", **kwargs) -> pd.DataFrame:
        """Transform GeoJSON FeatureCollection from OpenTripMap into places DataFrame."""
        rows = []
        for i, feat in enumerate(raw_features):
            props = feat.get("properties", {})
            geom = feat.get("geometry", {})
            coords = geom.get("coordinates", [0.0, 0.0])

            # Map raw OSM kind tags to canonical categories
            kinds = props.get("kinds", "")
            cat = "heritage"
            if "nature" in kinds or "natural" in kinds:
                cat = "nature"
            elif "beach" in kinds:
                cat = "beach"
            elif "religion" in kinds or "temple" in kinds or "church" in kinds:
                cat = "temple"
            elif "museum" in kinds:
                cat = "museum"
            elif "food" in kinds or "restaurant" in kinds:
                cat = "food"

            rows.append({
                "id": props.get("xid", f"OTM_{i+1:04d}"),
                "name": props.get("name") or f"Attraction {i+1}",
                "city": city_name,
                "lat": coords[1],
                "lon": coords[0],
                "category": cat,
                "avg_cost_inr": 150.0,
                "avg_visit_duration_min": 90,
                "rating": round(float(props.get("rate", 3) / 3.0 * 2.0 + 3.0), 1),
                "popularity": 0.7,
                "crowd_level": 0.5,
                "open_time": "09:00",
                "close_time": "18:00",
                "best_season": "all",
                "tags": kinds.replace(";", ","),
            })

        df = pd.DataFrame(rows)
        self.validate_schema(df)
        return df

    def fetch_ratings(self, **kwargs) -> pd.DataFrame:
        """OpenTripMap does not provide user ratings; synthetic interaction generation is used."""
        raise NotImplementedError("OpenTripMap API does not provide per-user ratings history.")

