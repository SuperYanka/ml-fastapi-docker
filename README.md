# ML API with FastAPI + Docker + Render

A simple API for machine learning model predictions, wrapped with **FastAPI**, packaged in **Docker** and deployed to **Render** 🚀

---

## Description

This project:
- trains a simple model (`LinearRegression`)
- saves it to `model.pkl`
- wraps an API with FastAPI (`POST /predict`)
- packages in Docker
- deploys to [Render](https://render.com)

---

## Demo

> [API docs (Swagger)](https://ml-fastapi-docker.onrender.com)
> `POST /predict` — accepts JSON with features and returns the model prediction

---

##  Project structure

ml-api-project/

├── app.py # FastAPI application

├── train_model.py # model training script

├── model.pkl # saved model

├── requirements.txt # dependencies

├── Dockerfile # Docker instruction

└── test.py # API request

---

## Input data example (POST `/predict`)

json
{
"feature1": 1.5,
"feature2": 2.5
}

**Answer:**


{
  "input": {
    "feature1": 1.5,
    "feature2": 2.5
  },
  "prediction": 11.5
}

