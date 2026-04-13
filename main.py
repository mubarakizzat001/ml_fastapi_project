import os
import pandas as pd
import joblib


def load_model():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(base_dir, "ml_model_package", "models", "risk_flag_model.joblib")
    if not os.path.exists(model_path):
        raise FileNotFoundError(
            f"Model not found at {model_path}. Please train the model first in the notebook."
        )
    return joblib.load(model_path)


def load_sample_row():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(base_dir, "ml_model_package", "data", "Test Data.csv")
    df = pd.read_csv(data_path)

    # Drop Id and target if present to match training features
    if "Id" in df.columns:
        df = df.drop(columns=["Id"])
    if "Risk_Flag" in df.columns:
        df_features = df.drop(columns=["Risk_Flag"])
    else:
        df_features = df

    # Take a single sample for testing
    return df_features.iloc[:1]


def main():
    model = load_model()
    sample = load_sample_row()

    pred = model.predict(sample)
    proba = None
    if hasattr(model, "predict_proba"):
        proba = model.predict_proba(sample)[:, 1]

    print("Sample input:")
    print(sample)
    print("Prediction:", pred)
    if proba is not None:
        print("Probability:", proba)


if __name__ == "__main__":
    main()
