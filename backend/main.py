from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.config import settings
from backend.database import engine, Base
import backend.models.models  # Ensure models are registered

# Create database tables if not existing
Base.metadata.create_all(bind=engine)

# Import API Routers
from backend.api.destinations import router as destinations_router
from backend.api.places import router as places_router
from backend.api.weather import router as weather_router
from backend.api.predictions import router as predictions_router
from backend.api.recommendation import router as recommendation_router
from backend.api.itinerary import router as itinerary_router
from backend.api.chat import router as chat_router
from backend.api.simulation import router as simulation_router
from backend.api.analytics import router as analytics_router
from backend.api.evaluation import router as evaluation_router
from backend.api.trips import router as trips_router
from backend.api.users import router as users_router

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="An Intelligent and Personalized Travel Planning System Using Hybrid ML & Multi-Objective Optimization",
    version=settings.PROJECT_VERSION,
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health", tags=["Health"])
def health_check():
    return {
        "status": "healthy",
        "service": settings.PROJECT_NAME,
        "version": settings.PROJECT_VERSION,
        "mock_mode": settings.MOCK_MODE,
        "database": "connected"
    }


# Mount Routers
api_prefix = settings.API_V1_PREFIX
app.include_router(destinations_router, prefix=api_prefix)
app.include_router(places_router, prefix=api_prefix)
app.include_router(weather_router, prefix=api_prefix)
app.include_router(predictions_router, prefix=api_prefix)
app.include_router(recommendation_router, prefix=api_prefix)
app.include_router(itinerary_router, prefix=api_prefix)
app.include_router(chat_router, prefix=api_prefix)
app.include_router(simulation_router, prefix=api_prefix)
app.include_router(analytics_router, prefix=api_prefix)
app.include_router(evaluation_router, prefix=api_prefix)
app.include_router(trips_router, prefix=api_prefix)
app.include_router(users_router, prefix=api_prefix)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)

