from fastapi import FastAPI
import random
import sqlite3

app = FastAPI()

DB_PATH = "/app/data/dice.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("CREATE TABLE IF NOT EXISTS rolls (dice TEXT, result INTEGER)")
    conn.close()

init_db()

def save_roll(dice, result):
    conn = sqlite3.connect(DB_PATH)
    conn.execute("INSERT INTO rolls (dice, result) VALUES (?, ?)", (dice, result))
    conn.commit()
    conn.close()

@app.get("/random_d6")
def random_d6():
    result = random.randint(1, 6)
    save_roll("d6", result)
    return {"dice": "d6", "result": result}

@app.get("/random_d/{x}")
def random_d(x: int):
    result = random.randint(1, x)
    save_roll(f"d{x}", result)
    return {"dice": f"d{x}", "result": result}
