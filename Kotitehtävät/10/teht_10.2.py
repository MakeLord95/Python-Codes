class Talo:
    def __init__(self, alin_kerros, ylin_kerros, nbr_of_elevators):
        self.elevators = []
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nbr_of_elevators = nbr_of_elevators

        for i in range(nbr_of_elevators):
            self.elevators.append(Hissi(alin_kerros, ylin_kerros))


    def print_data(self):
        print(f"Talon ylin kerros: {self.ylin_kerros}")
        print(f"Talon alin kerros: {self.alin_kerros}")
        print(f"Hissien lukumäärä: {self.nbr_of_elevators}")

        for i in self.elevators:
            i.print_info()


    def aja_hissia(self, hissi_nbr, kohde):
        elevator = self.elevators[hissi_nbr - 1]
        elevator.go_to_floor(kohde)


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
            print(f"Hissi on kerroksessa {self.nykyinen}\n")


    def floor_down(self, kerros):
        if self.nykyinen > kerros:
            self.nykyinen = self.nykyinen - 1
            print(f"Hissi on kerroksessa {self.nykyinen}\n")


if __name__ == '__main__':
    lowest_floor = 1
    top_floor = 50
    hissi_lkm = 3

    house = Talo(lowest_floor, top_floor, hissi_lkm)
    house.print_data()

    elevator_to_drive = 2
    floor_to_go = 15

    house.aja_hissia(elevator_to_drive, floor_to_go)
    house.print_data()
