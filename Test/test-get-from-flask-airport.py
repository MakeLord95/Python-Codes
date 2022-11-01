import requests


airport = str(input("Syötä lentokentän ICAO-koodi: "))
address = f"http://127.0.0.1:5000/kentta/?={airport}"

answer = requests.get(address).json()

print(answer)
