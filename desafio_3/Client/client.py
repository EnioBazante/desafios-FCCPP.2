import time
import sys
import requests

sys.stdout.reconfigure(line_buffering=True)
URL = "http://middleware:8000"

def testar():
    time.sleep(5)
    
    while True:
        print("\nEnviando request: ", flush=True)

        r = requests.get(f"{URL}/random_d6")
        print("status: ", r.status_code, flush=True)
        print("Resposta: ", r.text, flush=True)

        for x in [6, 10, 20]:
            print(f"\nTeste, dado de {x} lados", flush=True)
            r = requests.get(f"{URL}/random_d/{x}")
            print("Status:", r.status_code, flush=True)
            print("Resposta:", r.text, flush=True)

        print("\ntimeout de 5 segundos")
        time.sleep(5)

if __name__ == "__main__":
    testar()
