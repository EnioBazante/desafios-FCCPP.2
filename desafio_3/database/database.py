from fastapi import FastAPI
import sqlite3

app = FastAPI()

DB_PATH = "/app/data/dice.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("CREATE TABLE IF NOT EXISTS rolls (dice TEXT, result INTEGER)")
    conn.close()

init_db()

@app.post("/save")
def save_roll(dice: str, result: int):
    conn = sqlite3.connect(DB_PATH)
    conn.execute("INSERT INTO rolls (dice, result) VALUES (?, ?)", (dice, result))
    conn.commit()
    conn.close()
    return {"saved": True}
