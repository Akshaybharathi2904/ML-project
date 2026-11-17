from typing import Dict, Any, List, Tuple
import httpx
from backend.config import settings
from src.utils.geo import haversine_distance_km, compute_travel_time_minutes


class RoutingService:
    def __init__(self):
        self.osrm_url = "https://router.project-osrm.org/route/v1/driving"

    async def get_route(
        self,
        lat1: float,
        lon1: float,
        lat2: float,
        lon2: float
    ) -> Dict[str, Any]:
        """
        Compute driving route between two GPS coordinates using OSRM or Haversine fallback.
        """
        # Calculate Haversine fallback values first
        dist_km = haversine_distance_km(lat1, lon1, lat2, lon2)
        travel_min = compute_travel_time_minutes(dist_km)
        fallback_coords = [[lat1, lon1], [lat2, lon2]]

        if not settings.MOCK_MODE and dist_km > 0.05:
            try:
                coords_str = f"{lon1},{lat1};{lon2},{lat2}"
                async with httpx.AsyncClient(timeout=3.5) as client:
                    resp = await client.get(
                        f"{self.osrm_url}/{coords_str}",
                        params={"overview": "simplified", "geometries": "geojson"},
                        headers={"User-Agent": settings.USER_AGENT}
                    )
                    if resp.status_code == 200:
                        data = resp.json()
                        routes = data.get("routes", [])
                        if routes:
                            route = routes[0]
                            osrm_dist_km = round(route.get("distance", 0.0) / 1000.0, 2)
                            osrm_dur_min = round(route.get("duration", 0.0) / 60.0 + 10.0, 1)
                            geojson_pts = route.get("geometry", {}).get("coordinates", [])
                            # GeoJSON coordinates are [lon, lat] -> convert to [lat, lon]
                            polyline_pts = [[pt[1], pt[0]] for pt in geojson_pts] if geojson_pts else fallback_coords

                            return {
                                "distance_km": osrm_dist_km,
                                "duration_min": osrm_dur_min,
                                "geometry": polyline_pts,
                                "data_source": "OSRM Live Routing API"
                            }
            except Exception:
                pass

        # Haversine Speed Model Fallback
        return {
            "distance_km": round(dist_km, 2),
            "duration_min": round(travel_min, 1),
            "geometry": fallback_coords,
            "data_source": "Haversine Speed Model (Fallback)"
        }


routing_service = RoutingService()

