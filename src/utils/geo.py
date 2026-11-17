import numpy as np
import pandas as pd
from typing import Tuple


def haversine_distance_km(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """
    Compute great-circle distance between two GPS coordinates using the Haversine formula.
    
    Args:
        lat1, lon1: Coordinates of location 1 in decimal degrees.
        lat2, lon2: Coordinates of location 2 in decimal degrees.
        
    Returns:
        Distance in kilometers.
    """
    if lat1 == lat2 and lon1 == lon2:
        return 0.0

    R = 6371.0  # Earth's radius in kilometers
    phi1 = np.radians(lat1)
    phi2 = np.radians(lat2)
    delta_phi = np.radians(lat2 - lat1)
    delta_lambda = np.radians(lon2 - lon1)

    a = np.sin(delta_phi / 2.0) ** 2 + np.cos(phi1) * np.cos(phi2) * np.sin(delta_lambda / 2.0) ** 2
    c = 2.0 * np.arctan2(np.sqrt(a), np.sqrt(1.0 - a))
    return float(R * c)


def compute_travel_time_minutes(
    distance_km: float,
    avg_speed_kmh: float = 42.0,
    traffic_factor: float = 1.15,
    min_transfer_min: float = 15.0
) -> float:
    """
    Estimate realistic travel time between two places in minutes.
    
    Includes vehicle movement at average speed, terrain/traffic inflation,
    and a minimum boarding/parking overhead.
    """
    if distance_km <= 0.05:
        return 0.0
    
    raw_hours = distance_km / max(avg_speed_kmh, 10.0)
    travel_min = raw_hours * 60.0 * traffic_factor
    # Add modest transfer / parking overhead
    total_min = travel_min + min_transfer_min
    return round(float(total_min), 1)


def build_distance_and_time_matrices(
    places_df: pd.DataFrame,
    avg_speed_kmh: float = 42.0,
    traffic_factor: float = 1.15,
    min_transfer_min: float = 15.0
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Generate pairwise distance (km) and travel time (minutes) matrices for all places.
    
    Args:
        places_df: DataFrame containing 'id', 'lat', 'lon'.
        avg_speed_kmh: Average speed in km/h.
        traffic_factor: Multiplier for road winding and urban traffic.
        min_transfer_min: Base transfer time in minutes.
        
    Returns:
        (dist_matrix_df, time_matrix_df) indexed and columned by place id.
    """
    place_ids = places_df["id"].tolist()
    coords = places_df[["lat", "lon"]].to_numpy()
    n = len(place_ids)

    dist_matrix = np.zeros((n, n), dtype=np.float32)
    time_matrix = np.zeros((n, n), dtype=np.float32)

    for i in range(n):
        for j in range(i + 1, n):
            d = haversine_distance_km(coords[i, 0], coords[i, 1], coords[j, 0], coords[j, 1])
            t = compute_travel_time_minutes(d, avg_speed_kmh, traffic_factor, min_transfer_min)
            dist_matrix[i, j] = dist_matrix[j, i] = d
            time_matrix[i, j] = time_matrix[j, i] = t

    dist_df = pd.DataFrame(dist_matrix, index=place_ids, columns=place_ids)
    time_df = pd.DataFrame(time_matrix, index=place_ids, columns=place_ids)
    return dist_df, time_df

