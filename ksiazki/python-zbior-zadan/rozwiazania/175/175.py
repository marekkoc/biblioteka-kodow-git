import operator

dane2023 = dict()  # {'data':licznik}
dane2024 = dict()

with open('175_spis.txt', 'r', encoding='utf-8') as f:
  for ln in f:
    data, licznik = ln.strip().split('\t')
    if data[0:4] == '2023':
      dane2023[data] = float(licznik.replace(',', '.'))
    else:
      dane2024[data] = float(licznik.replace(',', '.'))

'''
Dane:
Start w roku 2023, 15000.00 km
7 litrów / 100km
5zł/1 litr w 2023
9zł/1 litr w 2024 (inflacja czy co?)
'''
# 2023
km23 = 0
start = 15000
print('Licznik początkowy dla roku 2023 =', start)
analiza = dict()
for data, licznik in dane2023.items():
  analiza[data] = round(licznik - start, 2)
  km23 += round(licznik - start, 2)
  start = licznik
print('Przejechane km w 2023 roku = ', round(km23, 2))

# 2024
km24 = 0
start = list(dane2023.items())[-1][1]  # stan licznika z ostatniego wpisu 2023
print('Licznik początkowy dla roku 2024 =', start)
for data, licznik in dane2024.items():
  analiza[data] = round(licznik - start, 2)
  km24 += round(licznik - start, 2)
  start = licznik
print('Przejechane km w 2024 roku = ', round(km24, 2))

koszt = km23 / 100 * 7 * 5 + km24 / 100 * 7 * 9
print('Koszt =', round(koszt, 2), 'zł')

analiza = sorted(analiza.items(), key=operator.itemgetter(1), reverse=True)
print('Dzień o największej ilości przejechanych kilometrów: ',
      analiza[0][0], '\t', analiza[0][1], 'km', sep='')
