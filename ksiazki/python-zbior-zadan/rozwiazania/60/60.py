from random import randint

N = 0
while not N & 1:
  N = randint(7, 27)
print('N=', N)

def Diament(n):
  for wiersz in range(1, n // 2 + 2):
    print(' ' * (n // 2 - wiersz + 1), '#' * (wiersz * 2 - 1), sep='')
  n -= 2
  for wiersz in range(1, n // 2 + 2):
    print(' ' * (wiersz), '#' * (n - wiersz * 2 + 2), sep='')
  print()

def DiamentP(n):
  for wiersz in range(1, n // 2 + 2):
    if wiersz != 1:
      print(' ' * (n // 2 - wiersz + 1), '#', ' ' * (wiersz * 2 - 3), '#',
            sep='')
    else:
      print(' ' * (n // 2 - wiersz + 1), '#' * (wiersz * 2 - 1), sep='')
  n -= 2
  for wiersz in range(1, n // 2 + 2):
    if wiersz != n // 2 + 1:
      print(' ' * (wiersz), '#', ' ' * (n - wiersz * 2), '#', sep='')
    else:
      print(' ' * (wiersz), '#' * (n - wiersz * 2 + 2), sep='')
  print()

Diament(N)
DiamentP(N)
