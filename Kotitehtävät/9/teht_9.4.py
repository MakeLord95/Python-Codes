import sys
import random


class Car:
    def __init__(self, licence, max_speed):
        self.licence = licence
        self.max_speed = max_speed
        self.speed = 0
        self.traveled = 0


    def print_info(self):
        print(f"Auton {self.licence}")
        print(f"Nopeus: {self.speed} km/h")
        print(f"Huippunopeus: {self.max_speed} km/h")
        print(f"Kulkema matka: {self.traveled} km\n")


    def accelerate(self, speed_change):
        if 0 < self.speed + speed_change < self.max_speed:
            self.speed = self.speed + speed_change

        elif self.speed + speed_change <= 0:
            self.speed = 0

        elif self.speed + speed_change > self.max_speed:
            self.speed = self.max_speed


    def travel(self, aika):
        if aika < 0:
            self.traveled = self.traveled

        elif aika > 0:
            self.traveled = self.traveled + self.speed * aika


if __name__ == '__main__':
    Cars = []
    for i in range(10):
        Cars.append(Car(f"ABC-{str(i+1)}", random.randint(100, 200)))

    while True:
        for Car in Cars:
            Car.accelerate(random.randint(-10, 15))
            Car.travel(1)

            if Car.traveled > 10000:
                for Car in Cars:
                    Car.print_info()
                sys.exit()
