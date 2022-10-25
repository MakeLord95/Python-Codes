class Auto:
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


if __name__ == '__main__':
    Car = Auto("ABC-123", 142)

    Car.accelerate(30)
    Car.accelerate(70)
    Car.accelerate(50)
    Car.print_info()

    Car.accelerate(-200)
    Car.print_info()
