L = list(range(1, 201))
print(L)
ile = 0
for poz in range(0, len(L) - 5):
  suma = sum(L[poz:poz + 6])
  if suma > 800 and suma <= 1000:
    ile += 1
    print(L[poz:poz + 6], '=', suma)
print(f'Ciągów 6 liczbowych spełniających warunki zadania jest {ile}.')
