from abc import ABC, abstractmethod


class Ptak(ABC):

    def __init__(self, gatunek, szybkosc):
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def lec(self):
        print("Tu", self.gatunek, "Osiągam prędkość", self.szybkosc)

    @abstractmethod
    def wydajOdglos(self):
        pass


class Orzel(Ptak):

    def __init__(self, szybkosc):
        super().__init__("Orzeł bielik", szybkosc)

    def poluj(self):
        print("Tu", self.gatunek, "Rozpocząłem polowanie")

    def wydajOdglos(self):
        print("PIIII!")


class Pingwin(Ptak):

    def __init__(self, szybkosc):
        super().__init__("Pingwin pikpok", szybkosc)

    def slizgaj(self):
        print("Tu", self.gatunek, "Rozpocząłem ślizganie!")

    def lec(self):
        print("Tu", self.gatunek, "Sorry, ja nie latam :(")

    def wydajOdglos(self):
        print("GRRRR!")


o = Orzel(100)
p = Pingwin(10)
p.wydajOdglos()
