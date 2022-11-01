import random

from Polttomoottoriauto import Polttomoottoriauto
from Sahkoauto import Sahkoauto

if __name__ == '__main__':
    electric_car = Sahkoauto("ABC-15", 180, 52.5)
    petrol_car = Polttomoottoriauto("ACD-123", 165, 32.3)

    electric_car.accelerate(random.randint(1, 180))
    electric_car.travel(3)

    petrol_car.accelerate(random.randint(1, 165))
    petrol_car.travel(3)

    electric_car.tulosta_tiedot()
    petrol_car.tulosta_tiedot()
