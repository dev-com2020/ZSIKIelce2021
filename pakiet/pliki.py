import os

def proces():
    print("pid to: ", os.getpid())
    pid = os.fork()
    if pid == 0:
        print("Mój PID to:", os.getpid())
    else:
        print("PID Potomka: ", pid)

def zapisz():
    plik = open('dane.txt', 'wt', encoding='utf8')
    plik.write("teskt1\n")
    plik.write("tekst2\ntekst3\n")
    plik.close()
    # a - append, dodaje do istniejących
    # w - zapis/nadpisanie
    # r - odczyt

def openF():
    plik = open('dane.txt', 'rt', encoding='utf8')
    napis = plik.readline()
    print(napis)
    plik.close()

