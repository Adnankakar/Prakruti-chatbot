from pathlib import Path
from typing import Any

import joblib
import pandas as pd


# --------------------------------------------------
# Paths
# --------------------------------------------------

# prediction_service.py
#       ↓
# services
#       ↓
# app
#       ↓
# backend
#       ↓
# prakruti-chatbot (project root)

PROJECT_ROOT = Path(__file__).resolve().parents[3]

MODEL_PATH = (
    PROJECT_ROOT
    / "ml"
    / "models"
    / "prakruti_random_forest.pkl"
)


# --------------------------------------------------
# Model configuration
# --------------------------------------------------

FEATURE_COLUMNS = [
    "Body Size",
    "Body Weight",
    "Height",
    "Bone Structure",
    "Complexion",
    "General feel of skin",
    "Texture of Skin",
    "Hair Color",
    "Appearance of Hair",
    "Shape of face",
    "Eyes",
    "Eyelashes",
    "Blinking of Eyes",
    "Cheeks",
    "Nose",
    "Teeth and gums",
    "Lips",
    "Nails",
    "Appetite",
    "Liking tastes",
    "Metabolism Type",
    "Climate Preference",
    "Stress Levels",
    "Sleep Patterns",
    "Dietary Habits",
    "Physical Activity Level",
    "Water Intake",
    "Digestion Quality",
    "Skin Sensitivity",
]


# --------------------------------------------------
# Load model once when backend starts
# --------------------------------------------------

if not MODEL_PATH.exists():
    raise FileNotFoundError(
        f"Prakruti model not found at: {MODEL_PATH}"
    )

model = joblib.load(MODEL_PATH)


# --------------------------------------------------
# Prediction function
# --------------------------------------------------

def predict_prakruti(answers: dict[str, Any]) -> str:
    """
    Predict the Prakruti/Dosha class using the
    existing trained Random Forest pipeline.

    `answers` must contain the 29 raw feature names
    expected by the trained model.
    """

    missing_features = [
        feature
        for feature in FEATURE_COLUMNS
        if feature not in answers
    ]

    if missing_features:
        raise ValueError(
            f"Missing model features: {missing_features}"
        )

    # Preserve the exact feature order used during training.
    input_data = {
        feature: [answers[feature]]
        for feature in FEATURE_COLUMNS
    }

    input_df = pd.DataFrame(input_data)

    prediction = model.predict(input_df)

    if len(prediction) == 0:
        raise ValueError("Model returned no prediction.")

    return str(prediction[0])


# --------------------------------------------------
# Optional probability information
# --------------------------------------------------

def predict_with_probabilities(
    answers: dict[str, Any]
) -> dict[str, Any]:
    """
    Return the predicted class and model probabilities.

    These probabilities are ML prediction probabilities.
    They must NOT be presented as Vata/Pitta/Kapha
    percentage scores.
    """

    missing_features = [
        feature
        for feature in FEATURE_COLUMNS
        if feature not in answers
    ]

    if missing_features:
        raise ValueError(
            f"Missing model features: {missing_features}"
        )

    input_data = {
        feature: [answers[feature]]
        for feature in FEATURE_COLUMNS
    }

    input_df = pd.DataFrame(input_data)

    prediction = model.predict(input_df)

    result = {
        "prediction": str(prediction[0])
    }

    if hasattr(model, "predict_proba"):
        probabilities = model.predict_proba(input_df)[0]

        classes = getattr(model, "classes_", [])

        result["probabilities"] = {
            str(cls): float(prob)
            for cls, prob in zip(classes, probabilities)
        }

    return result