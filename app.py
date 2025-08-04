from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Загружаем модель
model = joblib.load("model.pkl")

app = FastAPI()

# 👇 Шаг 1: Описание структуры входных данных
class InputData(BaseModel):
    feature1: float
    feature2: float

# 👇 Шаг 2: POST-запрос на /predict
@app.post("/predict")
def predict(data: InputData):
    X = np.array([[data.feature1, data.feature2]])
    prediction = model.predict(X)[0]
    return {
        "input": data.dict(),
        "prediction": prediction
    }
