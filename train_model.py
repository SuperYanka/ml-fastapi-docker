import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Генерируем данные (например, зависимость y = 2 * x1 + 3 * x2)
df = pd.DataFrame({
    "feature1": [1, 2, 3, 4, 5],
    "feature2": [2, 3, 4, 5, 6],
})
df["target"] = 2 * df["feature1"] + 3 * df["feature2"]

# Обучаем модель
X = df[["feature1", "feature2"]]
y = df["target"]
model = LinearRegression()
model.fit(X, y)

# Сохраняем модель в файл
joblib.dump(model, "model.pkl")
