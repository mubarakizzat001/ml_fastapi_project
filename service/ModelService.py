
import pandas as pd
from service.BaseModel import BaseModel



class ModelService(BaseModel):
    def __init__(self):
        super().__init__()

    def predict(self, data: dict):
        model = self.model
        df = pd.DataFrame([data])
  
        pred = model.predict(df)
        proba = None
        if hasattr(model, "predict_proba"):
            proba = model.predict_proba(df)[:, 1]

  
        if proba is not None:
            return{
            "Probability:": float(proba[0]),
            "Prediction:": int(pred[0])
                }

        return {
        "Prediction:": int(pred[0])
        }
