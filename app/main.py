import os
from typing import List

import joblib
from fastapi import FastAPI
from pydantic import BaseModel


MODEL_PATH = os.path.join('model', 'model.joblib')

app = FastAPI(title="Rest API for ML model", version="1.0.0", )

model = joblib.load(MODEL_PATH)


class InputData(BaseModel):
    input_values: List[float]


@app.post('/predict/')
async def prediction(input_data: InputData):
    predicted_output = model.predict([input_data.input_values])
    return {'prediction': predicted_output.tolist()}
