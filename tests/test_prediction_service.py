import pandas as pd

from backend.app.services.prediction_service import (
    predict_prakruti,
    FEATURE_COLUMNS,
)


def test_prediction_service():

    df = pd.read_csv("data/raw/Data.csv")

    sample = df.iloc[0]

    answers = {
        feature: sample[feature]
        for feature in FEATURE_COLUMNS
    }

    prediction = predict_prakruti(answers)

    print("\nPredicted Dosha:", prediction)

    assert prediction in [
        "Kapha",
        "Pitta",
        "Vata",
        "pitta+kapha",
        "vata+kapha",
        "vata+pitta",
    ]