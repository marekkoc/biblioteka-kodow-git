liczba = int(input('Podaj liczbę całkowitą: '))
if liczba < 0:
  liczba -= 1
elif liczba > 0:
  liczba += 1
print(liczba)
if liczba % 2 == 0:
  print('Liczba', liczba, 'jest parzysta.')
else:
  print('Liczba', liczba, 'jest nieparzysta.')
