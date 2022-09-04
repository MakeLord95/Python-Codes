res = None
seasons = ("Kevät", "Kesä", "Syksy", "Talvi")
while True:
    user = int(input("Syötä kuukauden numero: "))

    if user == 3 or user == 4 or user == 5:
        print(seasons[0])

    elif user == 6 or user == 7 or user == 8:
        print(seasons[1])

    elif user == 9 or user == 10 or user == 11:
        print(seasons[2])

    elif user == 12 or user == 1 or user == 2:
        print(seasons[3])

    else:
        print("Et syöttänyt kuukautta!")
        break
