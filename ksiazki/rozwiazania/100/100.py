wiersze = []
with open('100_dane.txt', 'r', encoding='utf-8') as f:
  for linia in f:
    wiersze.append([int(n.strip()) for n in linia.split('\t')])

print(wiersze)

# z wierszy zbuduję kolumny (transpozycja)
kolumny = [list(i) for i in zip(*wiersze)]
print(kolumny)

# można też tak:
kolumny = [*zip(*wiersze)]
print(kolumny)

print('Średnia arytmetyczna w pierwszej kolumnie', sum(kolumny[0]) / 30)
print('Średnia arytmetyczna w ostatniej kolumnie', sum(kolumny[5]) / 30)

maks = max(*sum(kolumny, ()))  # największa liczba w zbiorze
print('Największa liczba w zbiorze:', maks)
ilemax = list(filter(lambda e: e[1] > 0, list(
  [(nr + 1, k.count(maks)) for nr, k in enumerate(kolumny)])))
for nr, i in ilemax:
  print('W kolumnie', nr, 'znaleziono wartość', maks, ': ', i, '(ilość)')

print('Wierszy nie zawierających liczb podzielnych przez 10 jest',
      30 - len(list(filter(lambda l: len(l),
                           [list(filter(lambda e: e % 10 == 0, w)) for w in
                            wiersze]))))

print('Wierszy, w których trzy pierwsze liczby zachowują '
      'niemalejący porządek, jest', len(list(filter(
  lambda l: l[0] <= l[1] <= l[2], [w[:3] for w in wiersze]))))

print('Wiersze, w których jest dokładnie 3 liczby z zakresu <85;100>, jest',
      len(list(filter(lambda l: len(l) == 3,
                      [list(filter(lambda e: e in range(85, 101), w)) for w in
                       wiersze]))))
