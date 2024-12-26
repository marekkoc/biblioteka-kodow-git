import operator

class Zawodnik:
  def __init__(self, id: int, imie: str, gatunek: str):
    self.imie = imie
    self.gatunek = gatunek
    self.id = id

  def __str__(self):
    return 'ID=' + str(self.id) + ' ' + self.imie + ' (' + self.gatunek + ')'

zawodnicy = dict()  # {id, Zawodnik}

class Trasa:
  def __init__(self, nr, dzien, miesiac, rok):
    self.nr = nr
    self.dzien = dzien
    self.miesiac = miesiac
    self.rok = rok

  def __str__(self):
    return str(self.nr) + ' ' + self.dzien + '.' + self.miesiac + '.' + self.rok

zawody = dict()  # {nr, Trasa}
wyniki = dict()  # {nr_trasy, {id_zwierzaka,punkty}}

print('Oczytywanie listy z zawodnikami...')
with open('137_zawodnicy.txt', 'r', encoding='utf-8') as f:
  f.readline()  # nagłówki
  for ln in f:
    id, imie, gatunek = ln.split(' ')
    zawodnicy[int(id)] = Zawodnik(int(id), imie, gatunek.strip())

for id, z in zawodnicy.items():
  print(id, z)

print('Odczytywanie listy zawodów...')
with open('137_zawody.txt', 'r', encoding='utf-8') as f:
  f.readline()  # nagłówki
  for ln in f:
    nr, data = ln.split(' ')
    dzien, miesiac, rok = data.split('.')
    zawody[int(nr)] = Trasa(int(nr), dzien, miesiac, rok.strip())

for nr, z in zawody.items():
  print(nr, z)

print('Odczytywanie wyników...')
with open('137_wyniki.txt', 'r', encoding='utf-8') as f:
  f.readline()  # nagłówki
  for ln in f:
    nr, id, punkty = ln.split(' ')
    wyniki.setdefault(int(nr), [])
    wyniki[int(nr)].append((int(id), int(punkty)))

for nr, p in wyniki.items():
  print(nr, p)

print('Załadowano wszystkie pliki.')
print('*' * 60)
# Podaj listę (id, imię i gatunek) zwierząt o trzech najlepszych wynikach punktowych.
punkty = dict()
punkty_plywanie = dict()
for nr, lista in wyniki.items():
  for id, wynik in lista:
    punkty.setdefault(id, 0)
    punkty[id] += wynik
    if nr % 2 == 0:
      punkty_plywanie.setdefault(id, 0)
      punkty_plywanie[id] += wynik
''' odkomentuj, jak chcesz zobaczyć sumy
for id, wynik in punkty.items():
  print('Zwierzę id=', id, zawodnicy[id].imie, zawodnicy[id].gatunek, 'zdobyło',
        wynik, 'punktów.')
'''

punkty_sort = sorted(punkty.items(), key=operator.itemgetter(1), reverse=True)
print('Najlepsze 3 wyniki:')
najl = set()
for id, wynik in punkty_sort:
  najl.add(wynik)
  if len(najl) <= 3:
    print(zawodnicy[id].imie, zawodnicy[id].gatunek, wynik)

# Podaj zwycięzcę zawodów (lub zwycięzców w przypadku tej samej liczby punktów),
# wyświetlając id, imię i gatunek. Uwzględnij tylko wyniki zawodów, które
# odbyły się w wakacje (lipiec i sierpień).
print()
numery = set()
for nr, z in zawody.items():
  if z.miesiac == '08' or z.miesiac == '07':
    numery.add(nr)

punkty_wakacje = dict()  # id_zwirza : punkty razem
for nr, lista in wyniki.items():
  if nr not in numery:
    continue
  for id, wynik in lista:
    punkty_wakacje.setdefault(id, 0)
    punkty_wakacje[id] += wynik
print('Wakacyjne zdobycze punktowe, I miejsce:')

punkty_wakacje = dict(
  sorted(punkty_wakacje.items(), key=operator.itemgetter(1), reverse=True))
najl = set()
for id, wynik in punkty_wakacje.items():
  najl.add(wynik)
  if len(najl) <= 1:
    print('Zwierzę id = ', id, zawodnicy[id].imie, zawodnicy[id].gatunek,
          'zdobyło', wynik, 'punktów.')
print()

# Przyjmując, że zawody o parzystych numerach wymagały od zawodników umiejętności
# dobrego pływania, podaj listę (id, imię i gatunek) najgorszego pływaka.

print('Zdobyte punkty zależne od pływania, ostatnie miejsce:')
punkty_plywanie = dict(
  sorted(punkty_plywanie.items(), key=operator.itemgetter(1)))
najg = set()
for id, wynik in punkty_plywanie.items():
  najg.add(wynik)
  if len(najg) <= 1:
    print('Zwierzę id = ', id, zawodnicy[id].imie, zawodnicy[id].gatunek,
          'zdobyło', wynik, 'punktów.')

# Uwzględniając tylko te zawody, które odbywały się w poniedziałki,
# podaj dane (id, imię i gatunek) najgorszego zawodnika. 1 stycznia 2022 to sobota.

# Wyznaczam poniedziałkowe zawody (ich numery), rok 2022 ma 365 dni.
print()
poniedzialki_w_roku = []
start = 6  # sobota
d = 1  # dzień miesiąca
m = 1  # miesiąc
miesiace = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for i in range(1, 366):
  if start == 1:
    poniedzialki_w_roku.append((d, m))
  if start + 1 == 8:
    start = 1
  else:
    start += 1
  miesiace[m - 1] -= 1
  d += 1
  if miesiace[m - 1] == 0:
    m += 1
    d = 1
zawody_poniedzialkowe = set()
for nr, trasa in zawody.items():
  for dm in poniedzialki_w_roku:
    if int(trasa.dzien) == dm[0] and int(trasa.miesiac) == dm[1]:
      zawody_poniedzialkowe.add(nr)
      break

punkty_poniedzialki = dict()  # id_zwierza : punkty razem
for nr, lista in wyniki.items():
  if nr not in zawody_poniedzialkowe: continue
  for id, wynik in lista:
    punkty_poniedzialki.setdefault(id, 0)
    punkty_poniedzialki[id] += wynik
punkty_poniedzialki = dict(
  sorted(punkty_poniedzialki.items(), key=operator.itemgetter(1)))

print('Najgorszy poniedziałkowy wynik:')
najg = set()
for id, wynik in punkty_poniedzialki.items():
  najg.add(wynik)
  if len(najg) <= 1:
    print(
      f'Zwierzę id = {id}, {zawodnicy[id].imie} {zawodnicy[id].gatunek} zdobyło {wynik} punktów.')
