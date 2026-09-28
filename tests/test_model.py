from pathlib import Path
import joblib
import pandas as pd


# --------------------------------------------------
# Paths
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

MODEL_PATH = (
    PROJECT_ROOT
    / "ml"
    / "models"
    / "prakruti_random_forest.pkl"
)

DATA_PATH = (
    PROJECT_ROOT
    / "data"
    / "raw"
    / "Data.csv"
)


# --------------------------------------------------
# Test 1: Model file exists
# --------------------------------------------------

def test_model_file_exists():
    assert MODEL_PATH.exists(), f"Model not found: {MODEL_PATH}"


# --------------------------------------------------
# Test 2: Model can be loaded
# --------------------------------------------------

def test_model_can_be_loaded():
    model = joblib.load(MODEL_PATH)

    assert model is not None

    print("\nModel loaded successfully.")
    print("Model type:", type(model))


# --------------------------------------------------
# Test 3: Model can make prediction
# --------------------------------------------------

def test_model_prediction():

    # Load model
    model = joblib.load(MODEL_PATH)

    # Load dataset
    df = pd.read_csv(DATA_PATH)

    # Remove target column
    X = df.drop(columns=["Dosha"])

    # Take one sample
    sample = X.iloc[[0]]

    # Predict
    prediction = model.predict(sample)

    # Check prediction exists
    assert len(prediction) == 1

    print("\nPrediction successful.")
    print("Predicted Dosha:", prediction[0])

print(test_model_file_exists())

