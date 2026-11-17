import os
from pathlib import Path
from typing import List
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str = "TRAVELMATE AI"
    PROJECT_VERSION: str = "2.0.0"
    API_V1_PREFIX: str = "/api"
    
    # Database: SQLite default for offline development & tests, MySQL for production
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./travelmate.db")
    
    # LLM API Keys (Optional: rule-based intent router serves as fallback)
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")
    GROQ_API_KEY: str = os.getenv("GROQ_API_KEY", "")
    
    # Operation Mode
    MOCK_MODE: bool = os.getenv("MOCK_MODE", "true").lower() in ("true", "1", "yes")
    RANDOM_SEED: int = 42
    
    # Paths
    BASE_DIR: Path = Path(__file__).resolve().parent.parent
    MODELS_DIR: Path = Path(__file__).resolve().parent.parent / "models"
    RESULTS_DIR: Path = Path(__file__).resolve().parent.parent / "results"
    MOCK_DATA_DIR: Path = Path(__file__).resolve().parent.parent / "data" / "mock"
    
    # CORS
    CORS_ORIGINS: List[str] = ["*"]
    
    # External APIs User-Agent
    USER_AGENT: str = "TRAVELMATE-AI/2.0 (Academic Research; contact@travelmate.ai)"
    
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()

