a = int(input('Podaj liczbę całkowitą: '))
if a % 15 == 0:
  print('przez 3 i 5 (15)')
elif a % 3 == 0 and a % 5 != 0:
  print('podzielna przez 3 ale nie przez 5')
elif a % 3 != 0 and a % 5 == 0:
  print('podzielna przez 5 ale nie przez 3')
elif a % 3 != 0 and a % 5 != 0:
  print('nie podzielna przez 3 i nie podzielna przez 5')
