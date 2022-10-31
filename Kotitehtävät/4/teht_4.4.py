import random

rand_nbr = random.randint(1, 10)

while True:
    user_nbr = int(input("Arvaa koneen arpoma numero: "))

    if user_nbr == rand_nbr:
        print("Oikein!")
        break

    elif user_nbr > rand_nbr:
        print("Liian suuri arvaus!")

    elif user_nbr < rand_nbr:
        print("Liian pieni arvaus")

    else:
        user_nbr = int(input("Arvaa koneen arpoma numero: "))
