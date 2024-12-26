import operator

def czyPierwsza(n):
  if n < 2: return False
  for i in range(2, n - 1):
    if n % i == 0: return False
  return True

dane = []
with open('142_cyfry.txt', 'r', encoding='utf-8') as f:
  for ln in f:
    dane.append([])
    for c in ln.strip():
      dane[-1].append(int(c))

def dobryKwadrat(n, x, y):
  suma = 0
  for i in range(x, x + n):
    for j in range(y, y + n):
      suma += dane[i][j]
  if czyPierwsza(suma): return suma
  return 0

ile_kwadratow = 0
wszystkie_mozliwe_kwadraty = 0
ile_pierwszych = dict()  # {liczba pierwsza: ilość kwadratów o tej liczbie}

for n in range(2, 26):  # N z zakresu <2;25>
  for x in range(0, 25):
    if x + n - 1 >= 25: break
    for y in range(0, 25):
      if n + y - 1 >= 25: break
      wszystkie_mozliwe_kwadraty += 1
      suma = dobryKwadrat(n, x, y)
      if suma > 0:
        ile_kwadratow += 1
        print(f'Kwadrat o boku {n} utworzył '
              f'liczbę pierwszą = {suma}. Pozycja {x + 1}x{y + 1}')
        ile_pierwszych.setdefault(suma, 0)
        ile_pierwszych[suma] += 1
print(f'Wszystkich kwadratów w zbiorze K jest {ile_kwadratow}.')
print(f'Wszystkich możliwych kwadratów jest {wszystkie_mozliwe_kwadraty}.')

print(f'Liczby pierwsze:', sorted(ile_pierwszych.keys()))

for pierwsza, ile in dict(
    sorted(ile_pierwszych.items(), key=operator.itemgetter(0))).items():
  print(f'Liczba pierwsza {pierwsza} jest w {ile} kwadratach.')
