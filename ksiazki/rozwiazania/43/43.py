from random import randint

Lista = [-1] * 20  # tu będę wstawiać
print(
  Lista)  # Na razie lista jest pełna wartości -1. Liczby dopiero zostaną tutaj wstawione.
WolnePozycje = list(range(20))
while len(WolnePozycje):
  poz = randint(0, len(WolnePozycje) - 1)
  Lista[WolnePozycje[poz]] = randint(0, 20)  # losowa liczba
  print(
    f'Wstawiam liczbę {Lista[WolnePozycje[poz]]} na pozycję {WolnePozycje[poz]}.')
  del WolnePozycje[poz]  # to pole już nie jest wolne
print(Lista)
