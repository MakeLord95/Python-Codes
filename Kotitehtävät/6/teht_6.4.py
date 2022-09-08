import random


def number_list(nbr_list):
    summa = sum(nbr_list)
    return summa


if True:
    lista = random.sample(range(1, 101), 10)
    print(f"Listan summa: {number_list(lista)}")
    # print(f"Listan numerot: {lista}")
