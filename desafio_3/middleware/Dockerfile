FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY middleware.py .

ENV PYTHONUNBUFFERED=1

CMD ["uvicorn", "middleware:app", "--host", "0.0.0.0", "--port", "8000"]
