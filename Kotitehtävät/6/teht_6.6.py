import math


def pizza_calculator(pizza_dia_cm, pizza_price):
    pizza_area_cm2 = math.pi / 4 * pizza_dia_cm ** 2
    pizza_area_m2 = pizza_area_cm2 * 0.01 * 0.01
    pizza_price_m2 = pizza_price / pizza_area_m2

    return pizza_price_m2


if True:
    pizza_1_dia_cm = float(input("1. pizzan halkaisia (cm): "))
    pizza_1_price = float(input("1. pizzan hinta: "))
    pizza_2_dia_cm = float(input("2. pizzan halkaisia (cm) : "))
    pizza_2_price = float(input("2. pizzan hinta: "))

    pizza_1 = pizza_calculator(pizza_1_dia_cm, pizza_1_price)
    pizza_2 = pizza_calculator(pizza_2_dia_cm, pizza_2_price)

    if pizza_1 > pizza_2:
        print("2. pizza on neliöhinnaltaan parempi!")

    else:
        print("1. pizza on neliöhinnaltaan parempi!")
