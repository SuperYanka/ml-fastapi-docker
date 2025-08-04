# 1. Базовый образ
FROM python:3.11

# 2. Рабочая папка внутри контейнера
WORKDIR /app

# 3. Копируем файлы в контейнер
COPY . .

# 4. Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# 5. Команда запуска сервера
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
