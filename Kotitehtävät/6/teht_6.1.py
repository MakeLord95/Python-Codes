import random


def dice_throw():
    value = random.randint(1, 6)
    return value


while True:
    dice = dice_throw()
    print(dice)

    if dice == 6:
        break
