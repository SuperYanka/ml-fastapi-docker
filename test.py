import requests

payload = {
    "feature1": 1.0,
    "feature2": 2.0
}

r = requests.post("http://127.0.0.1:8000/predict", json=payload)
print(r.json())
