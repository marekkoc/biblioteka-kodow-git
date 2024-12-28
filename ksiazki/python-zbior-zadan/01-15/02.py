"""
Python. Zbior zadan z rozwiazaniami - Tomasz Jasniewski

Strona: 11

Zadanie 2. [1] <abc> {~}
Pobraną z klawiatury liczbę całkowitą zweryfikuj pod kątem parzystości. Wyświetl
adekwatny komunikat, gdy jest lub nie jest parzysta.


Created: 2024.12.28
Modified: 2024.12.28
"""
from icecream import ic


################################
### Moje rozwiazanie numer 1 ###
################################
if 0:
    run: int = int(input("\nWybierz: Powtórz(1) lub Zatrzymaj(2): "))
    while(run == 1):
        liczba: int = int(input("Podaj liczbę: "))
        if liczba % 2:
            print(f"Liczaba {liczba} jest nieparzysta!")
        else:
            print(f"Liczaba {liczba} jest parzysta!")
        run: int = int(input("\nWybierz: Powtórz(1) lub Zatrzymaj(2): "))


################################
### Moje rozwiazanie numer 2 ###
################################
# dodano operator trójargumentowy
if 0:
    run: int = int(input("\nWybierz: Powtórz(1) lub Zatrzymaj(2): "))
    while(run == 1):
        liczba: int = int(input("Podaj liczbę: "))
        decyzja: str = "nieparzysta" if liczba % 2 else "parzysta"
        print(f"\nLiczaba {liczba} jest {decyzja}!")
        run: int = int(input("\nWybierz: Powtórz(1) lub Zatrzymaj(2): "))

################################
### Moje rozwiazanie numer 3 ###
################################
# dodano operator morsa
if 1:
    while(run:= int(input("\nWybierz: Powtórz(1) lub Zatrzymaj(0): "))):
        liczba: int = int(input("Podaj liczbę: "))
        decyzja: str = "nieparzysta" if liczba % 2 else "parzysta"
        print(f"\nLiczaba {liczba} jest {decyzja}!")
        


#####################################################################################

#############################
### ROZWIAZANIE: SPOSOB 1 ###
#############################
a = int(input('Podaj liczbę całkowitą:'))
if a % 2 == 0:
  print(f'{a} jest liczbą parzystą.')
else:
  print(f'{a} nie jest liczbą parzystą.')
# w miejsce {a} zostanie wstawiona wartość zmiennej a