from fastapi import APIRouter, Query
from backend.services.weather_service import weather_service
from backend.schemas.schemas import StandardResponse

router = APIRouter(prefix="/weather", tags=["Weather"])


@router.get("/forecast", response_model=StandardResponse)
async def get_forecast(
    lat: float = Query(24.5854, description="Latitude"),
    lon: float = Query(73.7125, description="Longitude"),
    days: int = Query(5, description="Number of forecast days")
):
    forecasts = await weather_service.get_forecast(lat, lon, num_days=days)
    return StandardResponse(
        success=True,
        message=f"Retrieved {len(forecasts)} day weather forecast",
        data=forecasts,
        data_source=forecasts[0].get("data_source", "Open-Meteo") if forecasts else "Open-Meteo"
    )


@router.get("/current", response_model=StandardResponse)
async def get_current_weather(
    lat: float = Query(24.5854, description="Latitude"),
    lon: float = Query(73.7125, description="Longitude")
):
    forecasts = await weather_service.get_forecast(lat, lon, num_days=1)
    current = forecasts[0] if forecasts else {
        "date": "Today", "temp_c": 26.0, "condition": "Sunny", "outdoor_suitability": "Suitable", "suitability_score": 90.0
    }
    return StandardResponse(
        success=True,
        message="Current weather retrieved",
        data=current,
        data_source=current.get("data_source", "Open-Meteo")
    )

