import operator

dane = {}
odczyt = []
with open('112_dane.txt', 'r', encoding='utf-8') as f:
  f.readline()  # omijam nagłówki
  for d in f:
    odczyt.append(d.split('\t'))

for o in odczyt:
  for poz in range(0, 3):  # testy
    gdziePrzecinek = o[poz].find(',')
    if gdziePrzecinek >= 0:
      o[poz] = float(
        o[poz][0:gdziePrzecinek] + '.' + o[poz][gdziePrzecinek + 1:])
    else:
      o[poz] = float(o[poz])
  dane[int(o[3].strip('\n'))] = o[0:3]

# print(dane)  # { id: [test1, test2, test3], ...}

# Ile osób w przynajmniej jednym teście uzyskało wynik poniżej 10,00%?
ile = 0
for id, testy in dane.items():
  if testy[0] < 10.00 or testy[1] < 10.00 or testy[2] < 10.00:
    ile += 1
print('Osób poniżej 10.00 w przynajmniej jednym teście:', ile)

# Ile osób osiągnęło takie wyniki testów, że różnica pomiędzy dwoma dowolnymi z nich nigdy nie przekracza 2,00%?
ile = 0
for id, testy in dane.items():
  a, b, c = testy
  if abs(a - b) <= 2.00 and abs(a - c) <= 2.00 and abs(b - c) <= 2.00:
    ile += 1
print('Osób, u których różnica między dowolnymi testami nie przekracza 2.00:',
      ile)

# Podaj identyfikator osób (id_osoby), które osiągnęły trzy najwyższe średnie procentowe
# (średni procent oblicz jako średnia arytmetyczna ze wszystkich trzech testów danej osoby).
srednie = {}
for id, testy in dane.items():
  a, b, c = testy
  srednie[id] = (a + b + c) / 3
srednie = dict(
  sorted(srednie.items(), key=operator.itemgetter(1), reverse=True))
# print(srednie)
print('ID osób o najwyższych trzech średnich:')
# zbiór przechowa 3 najwyższe średnie, może je bowiem mieć więcej niż 3 osoby
naj = set()
for id, sre in srednie.items():
  naj.add(sre)  # taka średnia już jest wśród najwyższych
  if len(naj) > 3: break  # starczy
  print(id,
        round(sre, 2))  # te osoby (id) mają średnie wśród trzech najwyższych

# Znajdź osobę (osoby), których różnica między najniższym a najwyższym wynikiem procentowym jest największa.
roznice = {}
for id, testy in dane.items():
  a, b, c = testy
  roznice[id] = max(abs(a - b), abs(a - c), abs(b - c))
roznice = dict(
  sorted(roznice.items(), key=operator.itemgetter(1), reverse=True))
# print(roznice)
print('Osoby o największej różnicy pomiędzy wynikami testów:')
naj = set()
for id, roz in roznice.items():
  naj.add(roz)
  if len(naj) > 1: break
  print(id, round(roz, 2))
