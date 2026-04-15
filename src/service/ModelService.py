
from api import FinanceAppRead
import pandas as pd
from service.BaseModel import BaseModel




class ModelService(BaseModel):
    def __init__(self):
        super().__init__()

    def predict(self, app: FinanceAppRead):
        model = self.model
        data = app.model_dump()
        df = pd.DataFrame([data])
  
        Prediction = model.predict(df)
        Probability = None
        if hasattr(model, "predict_proba"):
            Probability = model.predict_proba(df)[:, 1]

  
        if Probability is not None:
            return{
            "probability:": float(Probability[0]),
            "prediction:": int(Prediction[0])
                }

        return {
        "prediction:": int(Prediction[0])
        }
