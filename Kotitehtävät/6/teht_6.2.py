import random


def dice_throw(d):
    value = random.randint(1, d)
    return value


face = int(input("Syötä tahkojen määrä: "))

while True:
    dice = dice_throw(face)
    print(dice)

    if dice == face:
        break
