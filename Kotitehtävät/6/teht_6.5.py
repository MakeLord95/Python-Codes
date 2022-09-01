import random


def odd_number_remover(nbr_lista):
    num = 0
    nbr_lista_no_odds = []
    while num < len(nbr_lista):

        if nbr_lista[num] % 2 == 0:
            nbr_lista_no_odds.append(nbr_lista[num])

        num = num + 1

    # print(nbr_lista_no_odds)
    return nbr_lista_no_odds


if True:
    lista = random.sample(range(1, 100), 10)
    print(f"Alkuperäinen lista: {lista}")
    print(f"Lista ilman parittomia lukuja: {odd_number_remover(lista)}")
