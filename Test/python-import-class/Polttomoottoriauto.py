from Auto import Auto


class Polttomoottoriauto(Auto):
    def __init__(self, licence, max_speed, bensatankki_litra):
        super().__init__(licence, max_speed)
        self.bensatankki_litra = bensatankki_litra

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
