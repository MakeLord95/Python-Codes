import requests


luku = int(input("Syötä luku: "))
address = f"http://127.0.0.1:5000/alkuluku/?={luku}"

answer = requests.get(address).json()

print(answer)
