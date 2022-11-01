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
