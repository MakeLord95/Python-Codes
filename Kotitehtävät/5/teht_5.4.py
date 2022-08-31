lista = []
res = None

for x in range(5):

    city = str(input("Syötä kaupunki: "))
    lista.append(city)
    res = lista

citys = res[0:5]
print(citys)
