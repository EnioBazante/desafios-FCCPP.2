from fastapi import FastAPI

app = FastAPI()

orders_db = {
    101: {"id": 101, "user_id": 1, "product": "Notebook", "amount": 2500.00},
    102: {"id": 102, "user_id": 2, "product": "Mouse", "amount": 50.00},
    103: {"id": 103, "user_id": 1, "product": "Teclado", "amount": 150.00},
}

@app.get("/orders")
def get_orders():
    return {"orders": list(orders_db.values())}
