from datetime import datetime
from sqlalchemy import (
    Column, Integer, String, Float, Boolean, Text, DateTime, ForeignKey, JSON
)
from sqlalchemy.orm import relationship
from backend.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(String(50), primary_key=True, index=True)
    username = Column(String(100), unique=True, index=True, nullable=True)
    email = Column(String(150), unique=True, nullable=True)
    budget_level = Column(String(30), default="medium")
    pace_preference = Column(String(30), default="moderate")
    preferences = Column(JSON, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    trips = relationship("Trip", back_populates="user", cascade="all, delete-orphan")
    ratings = relationship("UserRating", back_populates="user", cascade="all, delete-orphan")


class Place(Base):
    __tablename__ = "places"

    id = Column(String(50), primary_key=True, index=True)
    name = Column(String(200), index=True, nullable=False)
    destination = Column(String(100), index=True, nullable=False)
    state = Column(String(100), nullable=True)
    country_code = Column(String(10), default="IN")
    lat = Column(Float, nullable=False)
    lon = Column(Float, nullable=False)
    category = Column(String(50), index=True, nullable=False)
    avg_cost_inr = Column(Float, default=100.0)
    avg_visit_duration_min = Column(Float, default=60.0)
    rating = Column(Float, default=4.0)
    popularity = Column(Float, default=0.5)
    crowd_level = Column(Float, default=0.5)
    open_time = Column(String(10), default="09:00")
    close_time = Column(String(10), default="18:00")
    is_indoor = Column(Boolean, default=False)
    best_season = Column(String(30), default="all")
    tags = Column(String(255), default="")
    image_url = Column(String(500), nullable=True)
    data_source = Column(String(50), default="curated_seed")
    created_at = Column(DateTime, default=datetime.utcnow)


class Trip(Base):
    __tablename__ = "trips"

    id = Column(String(50), primary_key=True, index=True)
    user_id = Column(String(50), ForeignKey("users.id"), nullable=True)
    destination = Column(String(100), nullable=False)
    start_date = Column(String(20), nullable=True)
    num_days = Column(Integer, default=3)
    budget_inr = Column(Float, default=15000.0)
    estimated_cost_inr = Column(Float, default=0.0)
    pace = Column(String(30), default="moderate")
    transport = Column(String(30), default="taxi")
    travelers_count = Column(Integer, default=1)
    feasibility_score = Column(Float, default=85.0)
    status = Column(String(30), default="active")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = relationship("User", back_populates="trips")
    days = relationship("TripDay", back_populates="trip", cascade="all, delete-orphan")
    versions = relationship("ItineraryVersion", back_populates="trip", cascade="all, delete-orphan")
    chat_sessions = relationship("ChatSession", back_populates="trip", cascade="all, delete-orphan")


class TripDay(Base):
    __tablename__ = "trip_days"

    id = Column(Integer, primary_key=True, autoincrement=True)
    trip_id = Column(String(50), ForeignKey("trips.id"), nullable=False)
    day_number = Column(Integer, nullable=False)
    date = Column(String(20), nullable=True)
    total_travel_time_min = Column(Float, default=0.0)
    total_visit_time_min = Column(Float, default=0.0)
    total_cost_inr = Column(Float, default=0.0)
    feasibility = Column(Float, default=85.0)

    trip = relationship("Trip", back_populates="days")
    items = relationship("ItineraryItem", back_populates="day", cascade="all, delete-orphan")


class ItineraryItem(Base):
    __tablename__ = "itinerary_items"

    id = Column(Integer, primary_key=True, autoincrement=True)
    day_id = Column(Integer, ForeignKey("trip_days.id"), nullable=False)
    place_id = Column(String(50), ForeignKey("places.id"), nullable=False)
    order = Column(Integer, default=1)
    slot = Column(String(30), default="morning")  # morning, afternoon, evening
    arrival_time = Column(String(10), default="09:00")
    departure_time = Column(String(10), default="10:30")
    visit_duration_min = Column(Float, default=90.0)
    travel_time_from_prev_min = Column(Float, default=15.0)
    travel_distance_km = Column(Float, default=5.0)
    cost_inr = Column(Float, default=0.0)
    crowd_forecast = Column(Float, default=0.5)
    disruption_risk = Column(String(20), default="Low")
    is_indoor = Column(Boolean, default=False)
    personalization_score = Column(Float, default=0.8)
    why_recommended = Column(JSON, nullable=True)

    day = relationship("TripDay", back_populates="items")
    place = relationship("Place")


class ItineraryVersion(Base):
    __tablename__ = "itinerary_versions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    trip_id = Column(String(50), ForeignKey("trips.id"), nullable=False)
    version_number = Column(Integer, default=1)
    description = Column(String(255), default="Initial optimized plan")
    itinerary_data = Column(JSON, nullable=False)
    pareto_solutions = Column(JSON, nullable=True)
    feasibility_score = Column(Float, default=85.0)
    total_cost = Column(Float, default=0.0)
    created_at = Column(DateTime, default=datetime.utcnow)

    trip = relationship("Trip", back_populates="versions")


class ItineraryChange(Base):
    __tablename__ = "itinerary_changes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    trip_id = Column(String(50), ForeignKey("trips.id"), nullable=False)
    version_id = Column(Integer, ForeignKey("itinerary_versions.id"), nullable=True)
    original_place_id = Column(String(50), nullable=True)
    replacement_place_id = Column(String(50), nullable=True)
    reason = Column(Text, nullable=False)
    weather_condition = Column(String(100), nullable=True)
    old_cost = Column(Float, default=0.0)
    new_cost = Column(Float, default=0.0)
    time_diff_min = Column(Float, default=0.0)
    auto_adjusted = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)


class WeatherSnapshot(Base):
    __tablename__ = "weather_snapshots"

    id = Column(Integer, primary_key=True, autoincrement=True)
    destination = Column(String(100), index=True, nullable=False)
    date = Column(String(20), nullable=False)
    temp_c = Column(Float, default=25.0)
    rain_probability = Column(Float, default=0.1)
    condition = Column(String(50), default="Sunny")
    outdoor_suitability_score = Column(Float, default=85.0)
    disruption_window = Column(String(100), nullable=True)
    data_source = Column(String(50), default="Open-Meteo")
    recorded_at = Column(DateTime, default=datetime.utcnow)


class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    place_id = Column(String(50), index=True, nullable=True)
    prediction_type = Column(String(30), nullable=False)  # crowd, cost, disruption
    predicted_value = Column(Float, nullable=False)
    category = Column(String(50), nullable=True)
    confidence = Column(Float, default=0.85)
    model_version = Column(String(50), default="v1.0.0")
    data_source = Column(String(50), default="MLModelPredictionProvider")
    created_at = Column(DateTime, default=datetime.utcnow)


class ChatSession(Base):
    __tablename__ = "chat_sessions"

    id = Column(String(50), primary_key=True, index=True)
    trip_id = Column(String(50), ForeignKey("trips.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    trip = relationship("Trip", back_populates="chat_sessions")
    messages = relationship("ChatMessage", back_populates="session", cascade="all, delete-orphan")


class ChatMessage(Base):
    __tablename__ = "chat_messages"

    id = Column(Integer, primary_key=True, autoincrement=True)
    session_id = Column(String(50), ForeignKey("chat_sessions.id"), nullable=False)
    role = Column(String(20), nullable=False)  # user, assistant, system
    content = Column(Text, nullable=False)
    tool_calls = Column(JSON, nullable=True)
    proposed_changes = Column(JSON, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    session = relationship("ChatSession", back_populates="messages")


class SavedTrip(Base):
    __tablename__ = "saved_trips"

    id = Column(String(50), primary_key=True, index=True)
    user_id = Column(String(50), ForeignKey("users.id"), nullable=True)
    trip_id = Column(String(50), ForeignKey("trips.id"), nullable=False)
    name = Column(String(200), nullable=False)
    share_token = Column(String(100), unique=True, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)


class UserRating(Base):
    __tablename__ = "user_ratings"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String(50), ForeignKey("users.id"), nullable=False)
    place_id = Column(String(50), ForeignKey("places.id"), nullable=False)
    rating = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="ratings")
    place = relationship("Place")


class ModelRun(Base):
    __tablename__ = "model_runs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    model_name = Column(String(100), nullable=False)
    model_version = Column(String(50), nullable=False)
    metrics = Column(JSON, nullable=False)
    data_source = Column(String(100), default="synthetic_training_data")
    trained_at = Column(DateTime, default=datetime.utcnow)


class EvaluationResult(Base):
    __tablename__ = "evaluation_results"

    id = Column(Integer, primary_key=True, autoincrement=True)
    experiment_name = Column(String(100), nullable=False)
    metric_type = Column(String(50), nullable=False)  # recommender, optimizer, end_to_end
    data = Column(JSON, nullable=False)
    evaluated_at = Column(DateTime, default=datetime.utcnow)


class Activity(Base):
    __tablename__ = "activities"

    id = Column(String(50), primary_key=True, index=True)
    name = Column(String(200), nullable=False)
    category = Column(String(50), nullable=False)
    is_indoor = Column(Boolean, default=False)
    avg_duration_min = Column(Float, default=60.0)
    weather_sensitivity = Column(String(20), default="High")

