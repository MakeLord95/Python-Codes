class Julkaisu:
    def __init__(self, name):
        self.nimi = name

    def tulosta_tiedot(self):
        print(f"Julkaisun nimi: {self.nimi}")


class Kirja(Julkaisu):
    def __init__(self, name, writer, page_count):
        super().__init__(name)
        self.writer = writer
        self.page_count = page_count

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Kirjan kirjoittaja: {self.writer}")
        print(f"Kirjan sivumäärä: {self.page_count}\n")


class Lehti(Julkaisu):
    def __init__(self, name, editor_in_chief):
        super().__init__(name)
        self.editor_in_chief = editor_in_chief

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Lehden päätoimittaja: {self.editor_in_chief}")


if __name__ == '__main__':
    julkaisut = [Kirja("Hytti n:o 6", "Rosa Liksom", 200), Lehti("Aku Ankka", "Aki Hyyppä")]

    for i in julkaisut:
        i.tulosta_tiedot()
