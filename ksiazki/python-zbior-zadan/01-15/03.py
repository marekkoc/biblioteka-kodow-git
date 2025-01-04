"""
Python. Zbior zadan z rozwiazaniami - Tomasz Jasniewski

Strona: 11

Zadanie 3. [1] <abc> {~}
Pobierz liczbę całkowitą z klawiatury i sprawdź, czy JEST podzielna: przez 3 i przez 5;
przez 3, ale nie przez 5; przez 5, ale nie przez 3; ani przez 3, ani przez 5. Właściwą
odpowiedź wyświetl na ekranie.


Created: 2024.12.31
Modified: 2024.12.31
"""
from icecream import ic


################################
### Moje rozwiazanie numer 1 ###
################################
while(dzialanie:=int(input("\nRozpocznij(1), Zakończ(2): "))%2):
    liczba:int = int(input("\nPodaj liczbę: "))
    if(not liczba % 3 and not liczba % 5): print(f"Liczaba {liczba} JEST podzielna przez 3 i JEST podzielna przez 5!")
    elif(not liczba % 3 and liczba % 5): print(f"Liczba {liczba} JEST podzielna przez 3 ale NIE JEST podzilna przez 5!")
    elif(liczba % 3 and not liczba % 5): print(f"Liczba {liczba} NIE JEST podzielna przez 3 ale JEST podzielna przez 5!")
    else:
        print(f"Liczba {liczba} NIE JEST podzielana ANI przez 3 ANI przez 5!")
    

################################
### Moje rozwiazanie numer 2 ###
################################
# dodano operator trójargumentowy

################################
### Moje rozwiazanie numer 3 ###
################################
# dodano operator morsa



#####################################################################################

#############################
### ROZWIAZANIE: SPOSOB 1 ###
#############################
a = int(input('Podaj liczbę całkowitą: '))
if a % 15 == 0:
  print('przez 3 i 5 (15)')
elif a % 3 == 0 and a % 5 != 0:
  print('podzielna przez 3 ale nie przez 5')
elif a % 3 != 0 and a % 5 == 0:
  print('podzielna przez 5 ale nie przez 3')
elif a % 3 != 0 and a % 5 != 0:
  print('nie podzielna przez 3 i nie podzielna przez 5')