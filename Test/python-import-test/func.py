import random


def tulosta(user):
    print(user)


def for_loop(arg):
    for i in arg:
        print(i)


def while_loop(arg, arg2):
    while arg <= arg2:
        print(arg)
        arg = arg + 1


def dice_throw(faces):
    d = random.randint(1, faces)
    print(d)
