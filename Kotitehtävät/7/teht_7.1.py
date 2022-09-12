user_str = input("Syötä kuukauden numero: ")

res = None
seasons = ("Kevät", "Kesä", "Syksy", "Talvi")

while user_str != "":

    user_int = int(user_str)

    if user_int == 3 or user_int == 4 or user_int == 5:
        print(seasons[0])

    elif user_int == 6 or user_int == 7 or user_int == 8:
        print(seasons[1])

    elif user_int == 9 or user_int == 10 or user_int == 11:
        print(seasons[2])

    elif user_int == 12 or user_int == 1 or user_int == 2:
        print(seasons[3])

    else:
        print("Et syöttänyt kuukautta!")
        break

    user_str = input("Syötä kuukauden numero: ")

if user_str == "":
    print("Et syöttänyt kuukautta!")
