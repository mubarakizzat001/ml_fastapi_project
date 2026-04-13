import os
import joblib


class BaseModel():
    def __init__(self):
        self.model = self._load_model()

    def _load_model(self):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        model_path = os.path.join(base_dir, "ml_model_package", "models", "risk_flag_model.joblib")
        if not os.path.exists(model_path):
            raise FileNotFoundError(
                f"Model not found at {model_path}. Please train the model first in the notebook."
        )
        return joblib.load(model_path)