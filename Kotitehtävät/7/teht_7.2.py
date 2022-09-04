names = set()
user = input("Syötä nimi: ")

while user != "":

    if user not in names and user != "":
        print("Uusi nimi")
        names.add(user)

    elif user in names:
        print("Aiemin syötetty nimi")

    user = input("Syötä nimi: ")


for p in names:
    print(p)
