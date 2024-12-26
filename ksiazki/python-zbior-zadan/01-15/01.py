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
ic.configureOutput(includeContext=False)

# Moje rozwiazanie numer 1
lista_liczb: list[int] = []
for i in range(3):
    liczba: int = int(input(f"Podaj liczbe {i+1}:"))
    while(liczba < 0):
        liczba: int = int(input(f"Warosc musi byc wieksza od zera! Podaj liczbe {i+1}:"))
    lista_liczb.append(liczba)

ic(lista_liczb)