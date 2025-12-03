import time
import requests

URL = "http://localhost:8000"  

def testar():
    while True:

        print("\nEnviando request: ")

        r = requests.get(f"{URL}/random_d6")
        print("\nstatus: ", r.status_code)
        print("Resposta: ", r.text, )

        for x in [6, 10, 20]:

            print("\nTeste, dado de", x, "lados")
            r = requests.get(f"{URL}/random_d/{x}")
            print("\nStatus:", r.status_code)
            print("Resposta:", r.text)

        print("\n timeout de 5 segundos")
        time.sleep(5)

if __name__ == "__main__":
    testar()

