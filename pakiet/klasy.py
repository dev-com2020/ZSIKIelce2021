class Czlowiek:
    imie = ""
    wiek = None
    plec = ""

    def __init__(self, imie, wiek, plec):
        self.imie = imie
        self.wiek = wiek
        self.plec = plec

    def przywitaj(self):
        print("Cześć. Mam na imię", self.imie)

    def ruszaj(self):
        if self.plec == "k":
            print("Ruszyłam w drogę")
        else:
            print("Ryszyłem w drogę")

    def mysl(self):
        if self.wiek < 2:
            print("Dopiero się ucze")
        else:
            print("Nie ma problemu")


adam = Czlowiek("Adam", 45, "m")
# adam.wiek = 45
# adam.imie = "Adam"
# adam.plec = "m"

ewa = Czlowiek("Ewa", 36, "k")
# ewa.wiek = 36
# ewa.imie = "Ewa"
# ewa.plec = "k"

print("Obiekt->", adam.imie, adam.wiek, adam.plec, '\n')
print("Obiekt->", ewa.imie, ewa.wiek, ewa.plec, '\n')
