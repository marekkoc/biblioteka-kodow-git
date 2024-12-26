"""
Python. Zbior zadan z rozwiazaniami - Tomasz Jasniewski

Strona: 11

Zadanie 1. [2:1,1] <abc> {~}
Pobierz z klawiatury trzy nieujemne liczby całkowite. Jeżeli któraś jest ujemna, po-
wtórz pobieranie. Następnie znajdź największą z nich [1]. Wyświetl sumę pozosta-
łych liczb tyle razy, ile wynosi wartość największej liczby [1].


Created: 2024.12.26
Modified: 2024.12.26
"""
from icecream import ic
#ic.configureOutput(includeContext=False)

################################
### Moje rozwiazanie numer 1 ###
################################
if 0:
    # wczytywanie 3 liczb nieujemnych
    lista_liczb: list[int] = []
    for i in range(3):
        liczba: int = int(input(f"Podaj liczbe {i+1}:"))
        while(liczba < 0):
            liczba: int = int(input(f"Warosc musi byc wieksza od zera! Podaj liczbe {i+1}:"))
        lista_liczb.append(liczba)

    # najwieszka liczba z listy
    liczba_najwieksza = max(lista_liczb)
    ic(liczba_najwieksza)

    # usuwanie najwiekszej liczby z listy
    lista_liczb.remove(liczba_najwieksza)
    suma_pozostalych_liczb: int = sum(lista_liczb)
    ic(lista_liczb)
    ic(suma_pozostalych_liczb)

    # wypisanie sumy pozostalych liczb tyle razy ile wynosi najwieksza liczba
    for k,_ in enumerate(range(liczba_najwieksza)):
        print(f"{k+1} -> {suma_pozostalych_liczb}")

#####################################################################################

#############################
### ROZWIAZANIE: SPOSOB 1 ###
#############################
if 0:
    a = b = c = -1
    while(a < 0 or b < 0 or c < 0):
        a = int (input("Podaj liczbę a: "))
        b = int (input("Podaj liczbę b: "))
        c = int(input("Podaj liczbę c: "))

    # szukam najwiekszej liczby
    if a > b:
        max = a
    else:
        max = b
    if c > max:
        max = c

    # suma dwóch pozostałych liczb
    suma = a + b + c - max
    while max:
        print(suma, end=',')
        max -= 1
    print()

#############################
### ROZWIAZANIE: SPOSOB 2 ###
#############################
if 0:
    print()
    a = b = c = -1
    while (a < 0 or b < 0 or c < 0):
        a, b, c = [int(x) for x in input('Podaj 3 liczby rozdzielone spacją, to jest = a b c: ').split()]
    suma: int = a + b + c - max(a, b, c)
    for i in range(max(a, b, c)):
        print(suma, end=',')
    print()