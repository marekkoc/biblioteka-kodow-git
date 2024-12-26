from random import random

LIMIT = 250000
dodajProcent = .55  # szansa na dodanie do kolejki

class Klient:
  licznik = 0

  def __init__(self):
    Klient.licznik += 1

kolejka = []  # lista wystarczy, by symulować kolejkę

# PRZYPADEK 1
wejsc_do_petli_symulacji = 0
opuscilo = 0
while len(kolejka) < LIMIT:
  if random() <= dodajProcent:
    kolejka.append(Klient())
    wejsc_do_petli_symulacji += 1
  elif len(kolejka) > 0:
    kolejka.pop()
    opuscilo += 1
    wejsc_do_petli_symulacji += 1
  # Jeżeli szansa wskazała na opuszczenie kolejki, ale kolejka jest
  # pusta - nic się nie dzieje.
print('Przypadek 1:')
print(f'Pętla wykonała się {wejsc_do_petli_symulacji} razy.')
print(f'Utworzonych klientów: {Klient.licznik}.')
print(f'Klientów, którzy opuścili kolejkę: {opuscilo}.')
print(f'Utworzono {Klient.licznik} klientów.')
print(f'W kolejce znajduje się {len(kolejka)} klientów.')

# opuściło/pozostało
print(f'Odp.: {opuscilo / len(kolejka)}')
# opuściło/utworzeni klienci
print(f'Odp.: {opuscilo / Klient.licznik}')
# opuściło/utworzeni klienci
print(f'Odp.: {opuscilo / wejsc_do_petli_symulacji}')

# PRZYPADEK 2
opuscilo = 0
wejsc_do_petli_symulacji = 0
kolejka.clear()
Klient.licznik = 0
while len(kolejka) < LIMIT:
  wejsc_do_petli_symulacji += 1
  if random() <= dodajProcent:
    kolejka.append(Klient())
  elif len(kolejka) > 0:
    kolejka.pop()
    opuscilo += 1
  else:
    kolejka.append(Klient())
    kolejka.pop()
    wejsc_do_petli_symulacji += 1  # dwa wydarzenia, więc jeszcze raz +1
    opuscilo += 1

print()
print('Przypadek 2:')
print(f'Pętla wykonała się {wejsc_do_petli_symulacji} razy.')
print(f'Utworzonych klientów: {Klient.licznik}.')
print(f'Klientów, którzy opuścili kolejkę: {opuscilo}.')
print(f'Utworzono {Klient.licznik} klientów.')
print(f'W kolejce znajduje się {len(kolejka)} klientów.')

# opuściło/pozostało
print(f'Odp.: {opuscilo / len(kolejka)}')
# opuściło/utworzeni klienci
print(f'Odp.: {opuscilo / Klient.licznik}')
# opuściło/utworzeni klienci
print(f'Odp.: {opuscilo / wejsc_do_petli_symulacji}')

'''
    Interpretacja:
    W pierwszym przypadku licznik kroków pętli jest z reguły troszkę mniejszy,
    ponieważ ignorujemy te kroki pętli, które próbują wypuścić klienta z pustej
    kolejki. Podobnie liczba utworzonych klientów w pierwszym przypadku 
    jest zazwyczaj nieznacznie mniejsza, gdyż w tym pierwszym przypadku 
    nie tworzymy klienta, a w drugim przypadku zawsze go dodajemy
    i od razu wypuszczamy.
    
    Obliczone i wymagane w zadaniu stosunki są bardzo podobne. Wartość bliska
    4.5 oznacza, przy szansie 45% na opuszczenie i 55% na pojawienie się
    w kolejce, że trzeba utworzyć około 1 380 000 klientów, 
    by kolejka osiągnęła 250 000 - zatem
    trzeba utworzyć około 4.5 razy więcej osób od tej liczby, którą ma osiągnąć kolejka.
    Sprawdź to dla np. 500 000 osób w kolejce, lub więcej. 
    Proporcja będzie w przybliżeniu taka sama! 
    Wynika to ze stosunku 45/55.

    Wartość zbliżona do 0.82 to stosunek osób, które opuściły kolejkę, do
    wszystkich utworzonych. Łatwo zauważyć, że do proporcji 1 brakuje 0.18,
    i gdyby tę wartość pomnożyć przez 4.5 i dodać do 0.18 otrzymamy... około 1.
    Zatem 0.82 to właśnie ten 4.5-krotny narzut do wartości 0.18, a ta z kolei
    wyraża tutaj owe 250,000 osób (W stosunku do wszystkich
    utworzonych to właśnie około 0.18. Sprawdź to instrukcją:
    print(f'ODP: {250000 / Klient.licznik}');

    Wartość 0.45 to wartość dokładnie oddająca szansę na opuszczenie kolejki
    w kolejnych zdarzeniach. Nie może być inna przy odpowiednio dużej próbie
    i generatorze losowym o dobrym rozkładzie.
'''
