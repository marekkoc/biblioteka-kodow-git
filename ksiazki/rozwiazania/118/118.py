import operator

dane = dict()
with open('118_dane.txt', 'r', encoding='utf-8') as f:
  for ln in f:
    um, id = [int(i.strip()) for i in ln.split('\t')]
    dane[id] = um  # dane[id gracza] = umiejętność
dane = dict(sorted(dane.items(), key=operator.itemgetter(1), reverse=True))

print('Kody graczy o 10-u najlepszych wynikach:')
najl10 = set()
for id, um in dane.items():
  najl10.add(um)
  if len(najl10) > 10: break
  print('Gracz id = ', id, '(wynik=', um, ')')

print('Średnia wartość umiejętności wszystkich graczy:')
srednia = 0
for id, um in dane.items():
  srednia += um
print(srednia / len(dane))

from math import sqrt

def pierwsza(n: tuple):
  id = n[0]
  for i in range(2, int(sqrt(id)) + 1):
    if id % i == 0: return False
  return True

dane = dict(sorted(dane.items(), key=operator.itemgetter(1), reverse=False))
polacy = dict(filter(pierwsza, dane.items()))
print('Kody graczy z Polski o trzech najgorszych ocenach umiejętności:')
najl3 = set()
for id, um in polacy.items():
  najl3.add(um)
  if len(najl3) > 3: break
  print('Gracz id = ', id, '(wynik=', um, ')')
