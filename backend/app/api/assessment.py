from typing import List

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from app.services.prediction_service import predict_prakruti, FEATURE_COLUMNS
from app.services.scoring_service import calculate_vpk_scores
from app.services.recommendation_service import get_recommendation
from app.api.questions import FEATURE_BY_ID, VALID_OPTIONS

router = APIRouter(prefix="/assessment", tags=["Assessment"])

DISCLAIMER = (
    "This self-assessment is for general wellness and educational purposes only "
    "and is not medical advice or a medical diagnosis."
)


# ---------------------------------------------------------------------------
# Schemas
# ---------------------------------------------------------------------------

class Answer(BaseModel):
    question_id: int = Field(..., gt=0)
    value: str


class AssessmentRequest(BaseModel):
    answers: List[Answer]


class AssessmentResponse(BaseModel):
    ml_prediction: str
    vpk_percentages: dict[str, float]
    recommendation: dict
    disclaimer: str


# ---------------------------------------------------------------------------
# Validation helpers
# ---------------------------------------------------------------------------

def _validate_and_map(answers: List[Answer]) -> dict[str, str]:
    """
    Validate answers and return {feature_name: value}.
    Raises HTTPException on any validation failure.
    """
    if not answers:
        raise HTTPException(status_code=400, detail="No answers submitted.")

    ids_seen = set()
    for a in answers:
        if a.question_id in ids_seen:
            raise HTTPException(
                status_code=400,
                detail=f"Duplicate answer for question_id {a.question_id}."
            )
        ids_seen.add(a.question_id)

        feature = FEATURE_BY_ID.get(a.question_id)
        if feature is None:
            raise HTTPException(
                status_code=400,
                detail=f"Unknown question_id: {a.question_id}."
            )

        if not a.value.strip():
            raise HTTPException(
                status_code=400,
                detail=f"Empty value for question_id {a.question_id}."
            )

        if a.value not in VALID_OPTIONS[feature]:
            raise HTTPException(
                status_code=422,
                detail=(
                    f"Invalid option '{a.value}' for question_id {a.question_id} "
                    f"('{feature}'). Valid options: {sorted(VALID_OPTIONS[feature])}"
                ),
            )

    # Check all 29 features are answered
    answered_features = {FEATURE_BY_ID[a.question_id] for a in answers}
    missing = [f for f in FEATURE_COLUMNS if f not in answered_features]
    if missing:
        raise HTTPException(
            status_code=400,
            detail=f"Incomplete assessment. Missing answers for: {missing}"
        )

    return {FEATURE_BY_ID[a.question_id]: a.value for a in answers}


# ---------------------------------------------------------------------------
# Endpoints
# ---------------------------------------------------------------------------

@router.post("", response_model=AssessmentResponse)
def submit_assessment(request: AssessmentRequest):
    """
    POST /api/assessment

    Validate answers → ML prediction → VPK scoring → recommendations.
    ML prediction and VPK percentages are kept completely separate.
    """
    feature_answers = _validate_and_map(request.answers)

    # ML prediction (uses existing trained pipeline)
    try:
        ml_prediction = predict_prakruti(feature_answers)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"ML prediction failed: {e}")

    # Rule-based VPK scoring (independent of ML)
    try:
        vpk_percentages = calculate_vpk_scores(feature_answers)
    except ValueError as e:
        raise HTTPException(status_code=500, detail=str(e))

    # Recommendations based on ML prediction
    try:
        recommendation = get_recommendation(ml_prediction)
    except ValueError as e:
        raise HTTPException(status_code=500, detail=str(e))

    return AssessmentResponse(
        ml_prediction=ml_prediction,
        vpk_percentages=vpk_percentages,
        recommendation=recommendation,
        disclaimer=DISCLAIMER,
    )


@router.get("/recommendations/{dosha}")
def get_dosha_recommendation(dosha: str):
    """
    GET /api/assessment/recommendations/{dosha}

    Returns wellness recommendations for a given dosha class.
    """
    try:
        return {"dosha": dosha, "recommendation": get_recommendation(dosha)}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
