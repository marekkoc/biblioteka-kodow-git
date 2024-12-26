suma = 0
while True:
  x = float(input('Podaj liczbę: '))
  print(2 * x)
  if x >= 1 and x <= 10:
    print(f'Kończę, pomijając liczbę {x} i jej wielokrotność {2 * x}.')
    break
  else:
    suma += 2 * x
print('Suma=', suma)
