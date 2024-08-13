"""Serve the model."""
import pickle
from contextlib import asynccontextmanager
from lightgbm import LGBMRegressor
import pandas as pd
from pydantic import BaseModel
from fastapi import FastAPI


MODEL_NAME: str = "median_income_regressor"


class FeatureSet(BaseModel):
    """A Pydantic class that will hold the data model for the feature set"""
    HouseAge: float
    AveRooms: float
    AveBedrms: float
    Population: float
    AveOccup: float
    Latitude: float
    Longitude: float


def median_income_regressor(feature_set_dict: dict) -> dict:
    """Model loading & prediction."""
    with open("model.pkl", 'rb') as model_file:
        model: LGBMRegressor = pickle.load(model_file)
    feature_set_df = pd.DataFrame(feature_set_dict, index=[0])
    response = model.predict(feature_set_df)
    print(f"Model response: {response}\n")
    return {"prediction": response[0]}


ML_MODELS = {}


@asynccontextmanager
async def ml_lifespan_manager(app: FastAPI):
    """
    A context manager for the machine learning model life span, which
    enables machine learning models to be shared across various
    incoming user requests.
    """
    # load the ml model and prediction logic
    ML_MODELS[MODEL_NAME] = median_income_regressor
    yield
    # release the resources + cleanup
    ML_MODELS.clear()


app = FastAPI(lifespan=ml_lifespan_manager)


@app.get("/")
def root():
    return {"message": "Welcome to the machine learning service template for scikit-learn models!"}


@app.post("/predict")
async def predict(feature_set: FeatureSet):
    """An endpoint to call via browser."""
    return ML_MODELS[MODEL_NAME](feature_set.dict())
