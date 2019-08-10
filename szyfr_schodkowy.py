from turtle import *

def kwadrat(a, kolor):
    color('black', kolor)
    begin_fill()
    for i in range(4):
        fd(a)
        lt(90)
    end_fill()

def kostka(a, litera):
    liczba = ord(litera) - 96
    pom = 5
    n = 0
    index = 0
    while pom > 1:
        for i in range(pom):
            n += 1
            if liczba > n:
                kwadrat(a, 'green')
                fd(a)
            else:
                kwadrat(a, 'white')
                fd(a)
        bk(a)
        rt(90)
        bk(a)
        if index % 2 == 0 and index != 0:
            pom -= 1
        n -= 1
        index += 1
    rt(90)
    fd(2*a)
    lt(90)
    pu()
    fd(4*a)
    pd()

def kwadrat_duzy(a):
    for i in range(4):
        fd(5*a)
        lt(90)

def szyfruj(slowo, ile_wierszy):
    speed(0)
    ht()
    if 760 / len(slowo) < 480 / min(ile_wierszy, len(slowo)):
        a = 760 / len(slowo) / 5
    else:
        a = 480 / min(ile_wierszy, len(slowo)) / 5
    pu()
    bk(len(slowo)*a*5/2)
    lt(90)
    bk(ile_wierszy*a*5/2)
    rt(90)
    pd()
    for i in range(ile_wierszy):
        for j in range(len(slowo)):
            kwadrat_duzy(a)
            fd(5*a)
        bk(5*a*len(slowo))
        lt(90)
        fd(5*a)
        rt(90)
    kierunek = 'dol'
    fd(a)
    lt(90)
    for i in range(len(slowo)):
        if i % (ile_wierszy - 1) == 0 and kierunek == 'dol' and i != 0:
            bk(5*a)
            kostka(a, slowo[i])
            lt(90)
            kierunek = 'gora'
        elif i % (ile_wierszy - 1) == 0 and kierunek == 'gora':
            pu()
            fd(5*a)
            pd()
            kostka(a, slowo[i])
            lt(90)
            kierunek = 'dol'
        elif kierunek == 'dol':
            bk(5*a)
            kostka(a, slowo[i])
            lt(90)
        elif kierunek == 'gora':
            pu()
            fd(5*a)
            pd()
            kostka(a, slowo[i])
            lt(90)

szyfruj("dokumentygoogle",5)
