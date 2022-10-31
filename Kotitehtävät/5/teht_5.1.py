import random

dice = int(input("Syötä arpakuutioiden lukumäärä: "))
# dice_nbr = 0
dice_sum = 0

for value in range(dice):
    # dice_nbr = dice_nbr + 1
    luku = random.randint(1, 6)
    dice_sum += luku
    # print(f"{dice_nbr}. nopan arvottu luku: {luku}")

print(f"Arvottujen noppien summa: {dice_sum}")
