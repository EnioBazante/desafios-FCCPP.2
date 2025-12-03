from fastapi import FastAPI

app = FastAPI()

users_db = {
    1: {"id": 1, "name": "João Silva", "email": "joao@email.com"},
    2: {"id": 2, "name": "Maria Santos", "email": "maria@email.com"},
    3: {"id": 3, "name": "Pedro Costa", "email": "pedro@email.com"},
}

@app.get("/users")
def get_users():
    return {"users": list(users_db.values())}
