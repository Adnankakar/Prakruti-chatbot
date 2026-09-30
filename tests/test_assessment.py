"""
Tests for assessment endpoint validation and scoring.
Run from project root: pytest tests/
"""

import pandas as pd
import pytest
from fastapi.testclient import TestClient

from backend.app.main import app
from backend.app.services.prediction_service import predict_prakruti, FEATURE_COLUMNS
from backend.app.services.scoring_service import calculate_vpk_scores
from backend.app.api.questions import QUESTIONS, FEATURE_BY_ID, VALID_OPTIONS

client = TestClient(app)

KNOWN_CLASSES = {"Kapha", "Pitta", "Vata", "pitta+kapha", "vata+kapha", "vata+pitta"}


# ---------------------------------------------------------------------------
# Build a complete valid payload from row 0 of the dataset
# ---------------------------------------------------------------------------

def _valid_answers_payload() -> list[dict]:
    df = pd.read_csv("data/raw/Data.csv")
    sample = df.iloc[0]
    id_to_feature = {q["id"]: q["feature"] for q in QUESTIONS}
    return [
        {"question_id": qid, "value": str(sample[feature])}
        for qid, feature in id_to_feature.items()
    ]


# ---------------------------------------------------------------------------
# Prediction service tests
# ---------------------------------------------------------------------------

def test_predict_prakruti_returns_known_class():
    df = pd.read_csv("data/raw/Data.csv")
    sample = df.iloc[0]
    answers = {f: sample[f] for f in FEATURE_COLUMNS}
    assert predict_prakruti(answers) in KNOWN_CLASSES


def test_predict_prakruti_missing_feature_raises():
    df = pd.read_csv("data/raw/Data.csv")
    sample = df.iloc[0]
    answers = {f: sample[f] for f in FEATURE_COLUMNS}
    del answers["Body Size"]
    with pytest.raises(ValueError, match="Missing model features"):
        predict_prakruti(answers)


# ---------------------------------------------------------------------------
# VPK scoring tests
# ---------------------------------------------------------------------------

def test_vpk_scores_sum_to_100():
    df = pd.read_csv("data/raw/Data.csv")
    sample = df.iloc[0]
    answers = {f: sample[f] for f in FEATURE_COLUMNS}
    pct = calculate_vpk_scores(answers)
    assert abs(sum(pct.values()) - 100.0) < 0.01


def test_vpk_scores_invalid_option_raises():
    df = pd.read_csv("data/raw/Data.csv")
    sample = df.iloc[0]
    answers = {f: sample[f] for f in FEATURE_COLUMNS}
    answers["Body Size"] = "INVALID_VALUE"
    with pytest.raises(ValueError):
        calculate_vpk_scores(answers)


# ---------------------------------------------------------------------------
# Questions endpoint
# ---------------------------------------------------------------------------

def test_get_questions_returns_29():
    response = client.get("/api/questions")
    assert response.status_code == 200
    data = response.json()
    assert data["total_questions"] == 29
    assert len(data["questions"]) == 29


def test_get_questions_have_required_fields():
    response = client.get("/api/questions")
    for q in response.json()["questions"]:
        assert "id" in q
        assert "feature" in q
        assert "question" in q
        assert "options" in q
        assert len(q["options"]) > 0


# ---------------------------------------------------------------------------
# Assessment endpoint — happy path
# ---------------------------------------------------------------------------

def test_assessment_valid_request():
    payload = {"answers": _valid_answers_payload()}
    response = client.post("/api/assessment", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["ml_prediction"] in KNOWN_CLASSES
    assert "vpk_percentages" in data
    assert abs(sum(data["vpk_percentages"].values()) - 100.0) < 0.01
    assert "recommendation" in data
    assert "disclaimer" in data


# ---------------------------------------------------------------------------
# Assessment endpoint — validation failures
# ---------------------------------------------------------------------------

def test_assessment_empty_answers_rejected():
    response = client.post("/api/assessment", json={"answers": []})
    assert response.status_code == 400


def test_assessment_duplicate_question_id_rejected():
    answers = _valid_answers_payload()
    answers.append(answers[0])  # duplicate
    response = client.post("/api/assessment", json={"answers": answers})
    assert response.status_code == 400


def test_assessment_invalid_option_rejected():
    answers = _valid_answers_payload()
    answers[0]["value"] = "NOT_A_VALID_OPTION_XYZ"
    response = client.post("/api/assessment", json={"answers": answers})
    assert response.status_code == 422


def test_assessment_incomplete_rejected():
    answers = _valid_answers_payload()[:10]  # only 10 of 29
    response = client.post("/api/assessment", json={"answers": answers})
    assert response.status_code == 400


def test_assessment_unknown_question_id_rejected():
    answers = _valid_answers_payload()
    answers[0]["question_id"] = 9999
    response = client.post("/api/assessment", json={"answers": answers})
    assert response.status_code == 400


# ---------------------------------------------------------------------------
# Recommendations endpoint
# ---------------------------------------------------------------------------

def test_recommendations_valid_dosha():
    for dosha in KNOWN_CLASSES:
        encoded = dosha.replace("+", "%2B")
        response = client.get(f"/api/assessment/recommendations/{encoded}")
        assert response.status_code == 200
        data = response.json()
        assert "recommendation" in data


def test_recommendations_unknown_dosha_404():
    response = client.get("/api/assessment/recommendations/Unknown")
    assert response.status_code == 404
