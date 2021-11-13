import re


def start():
    print("Hejka!")


def switch():
    for x in [1, 2, 3, 4, 5, 6]:
        print("start", x)
        if x == 2:
            print("2")
            continue
        if x == 4:
            print("4")
            break
        print("koniec")


def napis():
    s = "qwerty"
    s = s[:2] + "X" + s[3:5] + s[6:]
    print(s)


def regex():
    y = "aa bb cc bb ff bb ee"

    print(re.sub("[bc]+", "XX", y, 2))
    print(re.sub("[bc]+", "XX", y))

    print(re.sub('bb (.*) bb', "X \\1 X", y))
    print(re.sub('.*bb (.*) bb.*', "\\1 X", y))
    print(re.sub('.*?bb (.*) bb.*', "\\1", y))


def dzialanie(operacja):
    if operacja == 'dodaj':
        def f(a, b):
            return a + b
        return f
    elif operacja == 'mnozenie':
        def f(a, b):
            return a * b
        return f

def dwa(funkcja, argument):
    return funkcja(2, argument)


def dni():
    dni_tyg = ['poniedziałek', 'wtorek', 'środa', 'czwartek', 'piątek', 'sobota', 'niedziela']
    for i in dni_tyg[2:6]:
        print('-', i)


def cut(start=2, end=6):
    dni_tyg = ['poniedziałek', 'wtorek', 'środa', 'czwartek', 'piątek', 'sobota', 'niedziela']
    return dni_tyg[start:end]

print(cut())

