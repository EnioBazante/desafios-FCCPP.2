from fastapi import FastAPI
import requests

app = FastAPI()

USER_SERVICE_URL = "http://user_service:8001"
ORDER_SERVICE_URL = "http://order_service:8002"

@app.get("/users")
def get_users():
    response = requests.get(f"{USER_SERVICE_URL}/users", timeout=5)
    return response.json()

@app.get("/orders")
def get_orders():
    response = requests.get(f"{ORDER_SERVICE_URL}/orders", timeout=5)
    return response.json()
