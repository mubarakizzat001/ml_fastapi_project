from fastapi import FastAPI
from service.ModelService import ModelService
from scalar_fastapi import get_scalar_api_reference
from api import FinanceAppSchema


app = FastAPI()
model_service = ModelService()

@app.get("/")
def read_root():
    return {"message": "Welcome to the ML Model API!"}

@app.post("/predict")
def predict(data: FinanceAppSchema):
    return model_service.predict(data)

@app.get("/scalar",include_in_schema=False)
def scalar_api():
    return get_scalar_api_reference(
        openapi_url= app.openapi_url,
        title="ML Model API"
    )

