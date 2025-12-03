import time
import sys
import requests

sys.stdout.reconfigure(line_buffering=True)

GATEWAY_URL = "http://gateway:8000"

def testar():
    while True:
        print("\nTeste /users:", flush=True)
        r = requests.get(f"{GATEWAY_URL}/users")
        print("Status:", r.status_code, flush=True)
        print("Resposta:", r.text, flush=True)

        print("\nTeste /orders:", flush=True)
        r = requests.get(f"{GATEWAY_URL}/orders")
        print("Status:", r.status_code, flush=True)
        print("Resposta:", r.text, flush=True)

        print("\nTimeout de 5 segundos")
        time.sleep(5)

if __name__ == "__main__":
    testar()
