"""Serve the model."""
from joblib import load
from fastapi import FastAPI, Body
from src.iris import Iris
from model import MODEL_FILENAME

app = FastAPI(
    title="Iris ML API",
    description="API for iris dataset ml model",
    version="1.0",
)

clf = None


@app.on_event('startup')
async def load_model():
    """Read and assign the model."""
    clf.model = load(f'src/{MODEL_FILENAME}')


@app.post('/predict', tags=["predictions"])
async def get_prediction(iris: Iris):
    data = dict(iris)['data']
    prediction = clf.model.predict(data).tolist()
    log_proba = clf.model.predict_proba(data).tolist()
    return {"prediction": prediction,
            "log_proba": log_proba}