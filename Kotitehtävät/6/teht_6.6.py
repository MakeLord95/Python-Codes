import math


def pizza_calculator(pizza_dia_cm, pizza_price):
    pizza_area_cm2 = math.pi / 4 * (pizza_dia_cm ** 2)
    pizza_area_m2 = pizza_area_cm2 * 0.01 * 0.01
    pizza_price_per_m2 = pizza_price / pizza_area_m2

    return pizza_price_per_m2


if True:
    pizza_1_dia_cm = float(input("Ensimmäisen pizzan halkaisia (cm): "))
    pizza_1_price = float(input("Ensimmäisen pizzan hinta (€): "))

    pizza_2_dia_cm = float(input("Toisen pizzan halkaisia (cm) : "))
    pizza_2_price = float(input("Toisen pizzan hinta (€): "))

    pizza_1_price_per_m2 = pizza_calculator(pizza_1_dia_cm, pizza_1_price)
    pizza_2_price_per_m2 = pizza_calculator(pizza_2_dia_cm, pizza_2_price)

    if pizza_1_price_per_m2 > pizza_2_price_per_m2:
        print("Toinen pizza on neliöhinnaltaan parempi!")

    elif pizza_2_price_per_m2 > pizza_1_price_per_m2:
        print("Ensimmäinen pizza on neliöhinnaltaan parempi!")

    else:
        print("Pizzat ovat neliöhinnaltaan samanlaisia")
