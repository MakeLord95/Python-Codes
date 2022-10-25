import random


class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot


    def tunti_kuluu(self):
        for auto in self.autot:
            auto.accelerate(random.randint(-10, 15))
            auto.travel(1)


    def tulosta_tilanne(self):
        for auto in self.autot:
            auto.print_info()


    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.traveled >= self.pituus:
                return True

            else:
                continue



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
            self.traveled = self.traveled + (self.speed * aika)


if __name__ == '__main__':
    Cars = []
    for i in range(10):
        Cars.append(Car(f"ABC-{str(i+1)}", random.randint(100, 200)))

    name = "Suuri romuralli"
    distance = 8000

    race = Kilpailu(name, distance, Cars)

    tunti = 0

    while True:
        race.tunti_kuluu()

        if race.kilpailu_ohi():
            print("Kilpailu ohi!\n")
            race.tulosta_tilanne()
            break

        else:
            tunti = tunti + 1

            if tunti % 10 == 0:
                print(f"Tunti: {tunti}\n")
                race.tulosta_tilanne()

            else:
                continue
