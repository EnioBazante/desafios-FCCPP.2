import time
import sys
import requests

sys.stdout.reconfigure(line_buffering=True)
URL = "http://server:8000"  

def testar():
    while True:
        print("\nEnviando request: ", flush=True)

        r = requests.get(f"{URL}/random_d6")
        print("\nstatus: ", r.status_code, flush=True)
        print("Resposta: ", r.text, flush=True)

        for x in [6, 10, 20]:
            print("\nTeste, dado de", x, "lados", flush=True)
            r = requests.get(f"{URL}/random_d/{x}")
            print("\nStatus:", r.status_code, flush=True)
            print("Resposta:", r.text, flush=True)

        print("\n timeout de 5 segundos")
        time.sleep(5)

if __name__ == "__main__":
    testar()
