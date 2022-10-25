import random


class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.nykyinen = alin


    def print_info(self):
        print(f"\nHissin ylin kerros: {self.ylin}")
        print(f"Hissin alin kerros: {self.alin}")
        print(f"Hissin nykyinen kerros: {self.nykyinen}\n")


    def go_to_floor(self, kerros):

        if self.alin > kerros > self.ylin:
            self.nykyinen = self.nykyinen

        elif self.alin <= kerros <= self.ylin:

            if self.nykyinen < kerros:
                x = self.alin

                while x <= kerros:
                    Hissi.floor_up(self, kerros)
                    x = x + 1

            elif self.nykyinen > kerros:
                x = self.ylin

                while x >= kerros:
                    Hissi.floor_down(self, kerros)
                    x = x - 1


    def floor_up(self, kerros):
        if self.nykyinen < kerros:
            self.nykyinen = self.nykyinen + 1
            print(f"Hissi on kerroksessa {self.nykyinen}")


    def floor_down(self, kerros):
        if self.nykyinen > kerros:
            self.nykyinen = self.nykyinen - 1
            print(f"Hissi on kerroksessa {self.nykyinen}")


if __name__ == '__main__':
    Elevator = Hissi(1, 10)

    Elevator.go_to_floor(random.randint(1, 10))
    Elevator.print_info()

    Elevator.go_to_floor(1)
    Elevator.print_info()
