c = [1, 2, 3, 2, 5, 6, 9, 1, 3, 7, 5, 8, 0, 9, 3, 1, 2, 5, 7, 6, 3, 4, 2, 1, 0, 8, 9, 7, 8, 4,
     6, 3, 2, 5, 4, 7, 8, 9, 1, 3, 2, 5, 4, 7, 5, 6, 8, 0, 1, 2, 3, 6, 5, 8, 7, 1, 1, 2, 3, 4,
     4, 5, 5, 6, 8, 9, 0, 9, 8, 1, 9, 7, 5, 4, 1, 2, 7, 6, 9, 3, 4, 2, 6]

# sposób 1
for poz in range(0, len(c)):
  suma = 0
  for dl in range(0, len(c) - poz):
    suma += c[poz + dl]
    if suma == 10:
      print('Podciąg: ', c[poz:poz + dl + 1], 'Pozycje: ',
            list(range(poz, poz + dl + 1)))
    elif suma > 10:
      break
print()

# sposób 2
N = len(c)
for dlugosc in range(N, 0, -1):
  for start in range(0, N - dlugosc + 1):
    koniec = start + dlugosc - 1
    suma = 0
    for x in range(start, koniec + 1):
      suma += c[x]
      if suma > 10: break
    if suma == 10:
      print('Podciąg :', c[start:koniec + 1], 'Pozycje :',
            list(range(start, koniec + 1)))

# sposób 3 (z wyrażeniami regularnymi)
print()
import re

cs = ''.join([str(e) for e in c])
dl = len(cs)
while dl > 1:
  od = -1
  while True:
    p = re.compile(f'[0-9]{{{dl}}}')
    m = p.search(cs, od + 1)
    if m:
      (od, ile) = m.span()
      if sum(int(i) for i in m.group()) == 10: print('Podciąg: ', m.group(),
                                                     f'Pozycja od {od} do {ile - 1}')
    else:
      break
  dl -= 1
