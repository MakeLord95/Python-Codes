import requests

lat = ""
lon = ""
units = ""
API_key = "2f216a569415f45775cd6b7fe63dcecc"

if __name__ == '__main__':
    city_name = str(input("Syötä kaupunki: "))

    address = f"https://api.openweathermap.org/geo/1.0/direct?q={city_name}&appid={API_key}"

    answer = requests.get(address).json()

    for a in answer:
        lat = a["lat"]
        lon = a["lon"]

    print("Missä formaatissa haluat lämpötilan? \nc. Celsius\nk. Kelvin\nf. Fahrenheit")
    units_question = str(input("Valinta (c / k / f): "))

    while units_question not in ("c", "k", "f"):
        print("Väärä syöte.")

        print("Missä formaatissa haluat lämpötilan? \nc. Celsius\nk. Kelvin\nf. Fahrenheit")
        units_question = str(input("Valinta (c / k / f): "))

    if units_question in ("c", "k", "f"):

        if units_question == "c":
            units = "metric"

        elif units_question == "k":
            units = "standard"

        elif units_question == "f":
            units = "imperial"

    address_2 = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&lang=fi&units={units}"

    answer_2 = requests.get(address_2).json()

    print("Säätila:", end=' ')
    for a in answer_2["weather"]:
        print(a["description"])

    print("Lämpötila:", end=' ')
    print(answer_2["main"]["temp"], end='')
    print(f"°{units_question.upper()}")
