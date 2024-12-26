from random import randint

N = 0
while not N & 1:
  N = randint(7, 27)
print('N=', N)

def Piramida(n):
  for wiersz in range(1, n // 2 + 2):
    print(' ' * (n // 2 - wiersz + 1), '#' * (wiersz * 2 - 1))
  print()

def PiramidaP(n):
  for wiersz in range(1, n // 2 + 2):
    print(' ' * (n // 2 - wiersz + 1), end='')
    if wiersz == 1 or wiersz == n // 2 + 1:
      print('#' * (wiersz * 2 - 1), end='')
    else:
      print('#', ' ' * (wiersz * 2 - 3), '#', end='', sep='')
    print()
  print()

Piramida(N)
PiramidaP(N)
