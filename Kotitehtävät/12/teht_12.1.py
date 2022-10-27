import requests

address = "https://api.chucknorris.io/jokes/random"

answer = requests.get(address).json()

print(answer["value"])
