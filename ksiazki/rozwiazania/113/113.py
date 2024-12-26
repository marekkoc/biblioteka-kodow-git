import operator

bity = []
with open('113_dane.txt', 'r', encoding='utf-8') as f:
  for ln in f:
    bity.append(ln.strip())
# print(bity)
print('Bitów w pliku: =', len(bity))
ilePrzez8 = 0
zliczanie = dict()
for b in bity:
  # na trzech ostatnich pozycjach liczby musi być zero: xxxxx000
  if b[-3:] == '000':
    ilePrzez8 += 1
  # jak nie ma klucza b, to wpisane będzie 0. Jak jest - bez zmian.
  zliczanie.setdefault(b, 0)
  zliczanie[b] += 1

print('Liczb bitowych podzielnych przez 8 jest:', ilePrzez8)

zliczanie = list(
  sorted(zliczanie.items(), key=operator.itemgetter(1), reverse=True))
maks = zliczanie[0][1]
for b, ile in zliczanie:
  if ile == maks:
    print('Największą ilość razy wystąpiła liczba', b, '=',
          ile, 'razy.')
  else:
    break

bityPomoc = bity.copy()

poz = 0
while True:
  nast = poz + 1
  while nast < len(bityPomoc):
    if sum(map(lambda a: int(a[0] == a[1]),
               list(zip(bityPomoc[poz], bityPomoc[nast])))) >= 5:
      bityPomoc.pop(nast)
      nast -= 1
    nast += 1
  poz += 1
  if poz >= len(bityPomoc): break
print('Pozostało ', len(bityPomoc), 'liczb:')
print(*bityPomoc, sep='\n')
