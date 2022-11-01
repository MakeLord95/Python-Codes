from Auto import Auto


class Sahkoauto(Auto):
    def __init__(self, licence, max_speed, akkukapasitetti):
        super().__init__(licence, max_speed)
        self.akkukapasiteetti = akkukapasitetti

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
