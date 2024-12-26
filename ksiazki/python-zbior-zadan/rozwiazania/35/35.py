L = list(range(1, 31))
print(L)
ile = 0
for poz in range(0, len(L) - 4):
  if sum(L[poz:poz + 5:2]) % 5 == 0:
    print(L[poz:poz + 5:2], 'Suma=', sum(L[poz:poz + 5:2]))
    ile += 1
print('Trójek oddzielonych o 1, których suma podzielna jest przez 5 znaleziono: ', ile)

ile = 0
for poz in range(0, len(L) - 6):
  if sum(L[poz:poz + 7:3]) % 5 == 0:
    print(L[poz:poz + 7:3], 'Suma=', sum(L[poz:poz + 7:3]))
    ile += 1
print('Trójek oddzielonych o 2, których suma podzielna jest przez 5 znaleziono: ', ile)
