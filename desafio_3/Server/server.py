from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/random_d6")
def random_d6():
    return {"d6_aleatorio": random.randint(1, 6)}

@app.get("/random_d/{x}")
def random_dx(x: int):
    return {"resultado": random.randint(6, x)}