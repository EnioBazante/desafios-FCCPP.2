from fastapi import FastAPI, HTTPException
import random
import requests

app = FastAPI()

@app.get("/roll/{sides}")
def roll_dice(sides: int, depth: int = 0):

    if sides < 2 or sides > 9999:
        raise HTTPException(status_code=400)
    
    if depth >= 5: 
        return {"service": "A", "dice_sides": sides}
    
    result = random.randint(1, sides)
    

    response = requests.get(f"http://service_b:8002/roll/{result}?depth={depth + 1}", timeout=2)
    next_roll = response.json()

    
    return {
        "service": "A",
        "dice_sides": sides,
        "next": next_roll
    }
