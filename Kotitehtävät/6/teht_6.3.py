gallon = int(input("Syötä bensiinin määrä Yhdysvaltain nestegallonoina: "))


def gallon_to_liter(retard_unit):
    liter = retard_unit / 0.264172052
    return liter


while gallon >= 0:
    gallon_2 = gallon_to_liter(gallon)
    print(f"{gallon} US gal on {gallon_2:.4f} l")

    if gallon < 0:
        break

    else:
        gallon = int(input("Syötä bensiinin määrä Yhdysvaltain nestegallonoina: "))
