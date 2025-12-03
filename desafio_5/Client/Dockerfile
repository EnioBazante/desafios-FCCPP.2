FROM python:3.9-slim

WORKDIR /app

RUN pip install requests

COPY client.py .

CMD ["python", "client.py"]
