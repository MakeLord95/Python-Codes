import sys

airports = {"EFET": "Enontekiön lentoasema",
            "EFHK": "Helsinki-Vantaan lentoasema",
            "EFIV": "Ivalon lentoasema",
            "EFJO": "Joensuun lentoasema",
            "EFJY": "Jyväskylän lentoasema",
            "EFHV": "Hyvinkään lentoasema"}

options = ["1", "2", "3"]

print("1. Syötä tietoja / 2. Hae tietoja / 3. Lopeta")
valinta = input("Valinta: ")

if valinta not in options:
    print("Väärä valinta!")
    sys.exit()

valinta_int = int(valinta)

while valinta_int != 3:

    if valinta not in options:
        print("Väärä valinta!")
        break

    valinta_int = int(valinta)

    if valinta_int == 1:
        ICAO_Code_Input = input("Syötä lentoaseman ICAO koodi: ").upper()

        if ICAO_Code_Input not in airports:
            Airport_Name_Input = input("Syötä lentoaseman nimi: ")
            airports[ICAO_Code_Input] = Airport_Name_Input

        else:
            print("Lentokenttä on jo tallennettu sanakirjaan")

    elif valinta_int == 2:
        Airport_Search = input("Syötä lentoaseman ICAO koodi: ").upper()

        if Airport_Search in airports:
            print(airports[Airport_Search])

        else:
            print("Lentokenttää ei ole tietokannassa")

    else:
        print("Exiting")
        break

    print("1. Syötä tietoja / 2. Hae tietoja / 3. Lopeta")
    valinta = input("Valinta: ")
