airports = {"EFET": "Enontekiön lentoasema",
            "EFHK": "Helsinki-Vantaan lentoasema",
            "EFIV": "Ivalon lentoasema",
            "EFJO": "Joensuun lentoasema",
            "EFJY": "Jyväskylän lentoasema"}

print("1. Syötä tietoja / 2. Hae tietoja / 3. Lopeta")
valinta = int(input("Valinta: "))

while valinta != 3:

    if valinta == 1:
        ICAO_Code_Input = input("Syötä lentoaseman ICAO koodi: ").upper()
        Airport_Name_Input = input("Syötä lentoaseman nimi: ")
        airports[ICAO_Code_Input] = Airport_Name_Input

    elif valinta == 2:
        Airport_Search = input("Syötä lentoaseman ICAO koodi: ").upper()
        print(airports[Airport_Search])

    print("1. Syötä tietoja / 2. Hae tietoja / 3. Lopeta")
    valinta = int(input("Valinta: "))
