import math
import random

user = int(input("Syötä pisteiden määrä: "))

circle_points = 0
square_points = 0
pi = 0

user_int = int(math.pow(user, 2))

for i in range(user_int):

    random_x = random.uniform(-1, 1)
    random_y = random.uniform(-1, 1)

    origin_dist = random_x ** 2 + random_y ** 2

    if origin_dist <= 1:
        circle_points += 1

    square_points += 1

    pi = 4 * circle_points / square_points

print(f"Piin likiarvo: {pi}")
