def airport_lookup(gps_code):
    if gps_code in airports:
        print(airports[gps_code])

    else:
        print("Lentokenttää ei ole tietokannassa")


def airport_add(gps_code_input):
    if gps_code_input not in airports:
        airport_name_input = input("Syötä lentoaseman nimi: ")
        airports[ICAO_Code_Input] = airport_name_input

    else:
        print("Lentokenttä on jo tallennettu sanakirjaan")


def user_input_checker(user_input):
    options = ["1", "2", "3"]

    if user_input not in options:
        print("Väärä valinta!")
        # sys.exit()
        return 3

    else:
        user_input_int = int(user_input)

        return user_input_int


airports = {"EFET": "Enontekiön lentoasema",
            "EFHK": "Helsinki-Vantaan lentoasema",
            "EFIV": "Ivalon lentoasema",
            "EFJO": "Joensuun lentoasema",
            "EFJY": "Jyväskylän lentoasema",
            "EFHV": "Hyvinkään lentoasema"}

print("1. Syötä tietoja / 2. Hae tietoja / 3. Lopeta")
valinta = input("Valinta: ")

valinta_int = user_input_checker(valinta)

while valinta_int != 3:

    valinta_int = user_input_checker(valinta)

    if valinta_int == 1:
        ICAO_Code_Input = input("Syötä lentoaseman ICAO koodi: ").upper()
        airport_add(ICAO_Code_Input)

    elif valinta_int == 2:
        Airport_Search = input("Syötä lentoaseman ICAO koodi: ").upper()
        airport_lookup(Airport_Search)

    else:
        print("Exiting")
        break

    print("1. Syötä tietoja / 2. Hae tietoja / 3. Lopeta")
    valinta = input("Valinta: ")
