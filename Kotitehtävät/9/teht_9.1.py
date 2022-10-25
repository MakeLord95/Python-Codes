class Auto:
    def __init__(self, licence, max_speed):
        self.licence = licence
        self.max_speed = max_speed
        self.speed = 0
        self.traveled = 0


    def print_info(self):
        print(f"Auton {self.licence}")
        print(f"Huippunopeus: {self.max_speed}km/h")
        print(f"Tämänhetkinen nopeus: {self.speed}km/h")
        print(f"Kulkema matka: {self.traveled}km\n")

if __name__ == '__main__':
    Car_1 = Auto("ABC-123", 142)
    Car_1.print_info()

    Car_2 = Auto("ASD-169", 150)
    Car_2.print_info()
