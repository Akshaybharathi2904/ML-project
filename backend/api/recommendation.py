from fastapi import APIRouter, Query, HTTPException
from backend.engines.recommendation_engine import recommendation_engine
from backend.services.places_service import places_service
from backend.schemas.schemas import RecommendationRequest, StandardResponse

router = APIRouter(prefix="/recommend", tags=["Recommendation"])


@router.post("", response_model=StandardResponse)
def get_recommendations(req: RecommendationRequest):
    scored_places, feat_mat = recommendation_engine.rank_destination_places(
        destination=req.destination,
        user_interests=req.interests,
        budget_level=req.budget_level,
        pace=req.pace,
        season=req.season,
        seed_ratings=req.seed_ratings,
        top_k=req.num_candidates
    )

    results = []
    for rank_idx, (_, r) in enumerate(scored_places.iterrows()):
        reasons = recommendation_engine.explain_place(r["id"], scored_places, feat_mat)
        results.append({
            "id": r["id"],
            "name": r["name"],
            "category": r["category"],
            "destination": r.get("destination", req.destination),
            "lat": float(r["lat"]),
            "lon": float(r["lon"]),
            "avg_cost_inr": float(r["avg_cost_inr"]),
            "avg_visit_duration_min": float(r["avg_visit_duration_min"]),
            "rating": float(r["rating"]),
            "popularity": float(r["popularity"]),
            "crowd_level": float(r["crowd_level"]),
            "is_indoor": bool(r.get("is_indoor", False)),
            "personalization_score": round(float(r["personalization_score"]) * 100.0, 1),
            "content_score": round(float(r.get("content_score", 0.7)) * 100.0, 1),
            "collab_score": round(float(r.get("collab_score", 0.7)) * 100.0, 1),
            "baseline_score": round(float(r.get("baseline_score", 75.0)), 1),
            "ranking": rank_idx + 1,
            "why_recommended": reasons
        })

    return StandardResponse(
        success=True,
        message=f"Generated {len(results)} personalized recommendations",
        data=results,
        data_source="Hybrid Model (Content-Based + SVD Factorization + LightGBM)"
    )


@router.get("/explain/{place_id}", response_model=StandardResponse)
def explain_place_recommendation(place_id: str, destination: str = Query("Udaipur")):
    shap_data = recommendation_engine.explain_place_with_shap(place_id=place_id, destination=destination)
    return StandardResponse(
        success=True,
        message=f"SHAP feature attribution computed for {place_id}",
        data=shap_data,
        data_source="SHAP TreeExplainer (Feature Attribution)"
    )

