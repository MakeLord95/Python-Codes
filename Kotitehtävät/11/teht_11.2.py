import random


class Auto:
    def __init__(self, licence, max_speed):
        self.licence = licence
        self.max_speed = max_speed
        self.speed = 0
        self.traveled = 0

    def tulosta_tiedot(self):
        print(f"Auton {self.licence}")
        print(f"Matkamittarin lukema: {self.traveled}km\n")

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


class Sahkoauto(Auto):
    def __init__(self, licence, max_speed, akkukapasitetti):
        super().__init__(licence, max_speed)
        self.akkukapasiteetti = akkukapasitetti

    def tulosta_tiedot(self):
        super().tulosta_tiedot()


class Polttomoottoriauto(Auto):
    def __init__(self, licence, max_speed, bensatankki_litra):
        super().__init__(licence, max_speed)
        self.bensatankki_litra = bensatankki_litra

    def tulosta_tiedot(self):
        super().tulosta_tiedot()


if __name__ == '__main__':
    electric_car = Sahkoauto("ABC-15", 180, 52.5)
    petrol_car = Polttomoottoriauto("ACD-123", 165, 32.3)

    electric_car.accelerate(random.randint(1, 180))
    electric_car.travel(3)

    petrol_car.accelerate(random.randint(1, 165))
    petrol_car.travel(3)

    electric_car.tulosta_tiedot()
    petrol_car.tulosta_tiedot()
