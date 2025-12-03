FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY service_a.py .

ENV PYTHONUNBUFFERED=1

CMD ["uvicorn", "service_a:app", "--host", "0.0.0.0", "--port", "8001"]
