def temp(od, do):
  if od == do:
    yield od
  elif od < do:
    while od <= do:
      yield od
      od += 1
  else:
    while od >= do:
      yield od
      od -= 1

# funkcja zwracająca listę z liczbami z zakresu <od;do>
def oddo(od, do): return list(temp(od, do))

# test poprawności
print(oddo(-10, 10))
print(oddo(10, -10))
print(oddo(5, 5))

# generowanie list do zadania
from random import randint

listy = []
for i in range(10):
  listy.append(oddo(randint(-10, 10), randint(-10, 10)))

print(listy)
# Słownik `zliczanie` zawiera informację o tym, ile razy konkretna liczba wystąpiła
# w wygenerowanych zbiorach
zliczanie = dict(zip(oddo(-10, 10), [0] * 21))

for li in listy:
  for liczba in zliczanie:
    if liczba in li:
      zliczanie[liczba] += 1
# już mamy odpowiedzi, teraz je tylko
print(zliczanie)
for liczba, ile in zliczanie.items():
  if (ile >= 5):
    print(
      f'Liczba = {liczba} wystąpiła w {ile} spośród 10 wygenerowanych list.')
