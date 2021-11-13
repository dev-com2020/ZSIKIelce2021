# lambda <parametry> : <wyrażenie>
dodaj = lambda x: x + 1


# print(dodaj(3))


# print((lambda x,y : x + y)(3,3))

def fun(f, liczba):
    return f(liczba)


# def dodaj_jeden(x):
#     return x + 1
#
# def kwadrat(par):
#     return par*par
#
# print(fun(dodaj_jeden,7))
# print(fun(kwadrat,7))

print(fun(lambda x: x + 1, 7))
print(fun(lambda x: x * x, 7))
