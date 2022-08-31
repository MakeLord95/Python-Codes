num = int
lista = []
res = None

while num != "":
    num = str(input("Anna luku: "))

    if num != "":
        lista.append(num)
        res = [eval(i) for i in lista]

    if input == "":
        break

res.sort(reverse=True)
fi = res[0:5]
print(f"Suurimmat luvut ovat: {fi}")
