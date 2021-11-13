class Samochod:
    def __init__(self):
        self.silnik = False
        self.bieg = 0
        self.predkosc = 0

    def uruchom(self):
        self.silnik = True

    def wylacz(self):
        self.silnik = False

    def biegNastepny(self):
        if self.bieg <= 6: self.bieg += 1; print(self.bieg)

    def biegPoprzedni(self):
        if self.bieg >= 0: self.bieg -= 1; print(self.bieg)

    def przyspiesz(self):
        if self.silnik == True and self.bieg > 0: self.predkosc += 10; print(self.predkosc)

    def hamuj(self):
        if self.predkosc >= 10:
            self.predkosc -= 10
        else:
            self.predkosc = 0
        print(self.predkosc)

audi = Samochod()
audi.uruchom()
audi.biegNastepny()
audi.przyspiesz()
audi.biegPoprzedni()
audi.hamuj()
audi.wylacz()