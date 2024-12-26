iloscitxt = '1x500, 16x200, 4x100, 0x50, 23x20, 11x10, 27x5' \
            ', 12x2, 48x1, 30x0.5, 14x0.2, 7x0.1, 28x0.05, 13x0.02, 89x0.01'
ilosci = dict()
for a, b in [x.split('x') for x in iloscitxt.split(', ')]:
  ilosci[float(b)] = int(a)
print(ilosci)

kwotytxt = '769.50, 433.11, 950.00, 34.12, 57.98, 432.78' \
           ', 99.22, 11.45, 30.21, 450.99, 1644.88, 3.44'
kwoty = [float(x) for x in kwotytxt.split(', ')]
print(kwoty)

def wydajReszte(reszta, bank):
  nominaly = [500, 200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02,
              0.01]
  komunikat = []
  for n in nominaly:
    while reszta >= n and bank[n] > 0:
      reszta = round(reszta - n, 2)
      bank[n] -= 1
      komunikat.append(str(n))
  if (reszta > 0.0): return (False, bank, '')
  return (True, bank, ','.join(komunikat))

print('Suma w kasie:', sum([kwota * ile for kwota, ile in ilosci.items()]))
# rozpoczynam wydawanie kwot
for reszta in kwoty:
  sukces, bank, komunikat = wydajReszte(reszta, ilosci.copy())
  if (sukces):
    print('Udało się wydać resztę:', reszta, ':', end=' ')
    print(komunikat)
    ilosci = bank
  else:
    print('Nie udało się wydać reszty:', reszta)

print('Stan kasy:', ilosci)
print('Suma w kasie:', sum([kwota * ile for kwota, ile in ilosci.items()]))
