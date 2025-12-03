FROM python:3.9-slim

WORKDIR /app

COPY ./requirement.txt .

RUN pip3 install -r requirement.txt

COPY client.py .

CMD ["python3", "client.py"]
