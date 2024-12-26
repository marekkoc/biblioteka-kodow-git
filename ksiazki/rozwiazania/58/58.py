from random import randint

N = randint(5, 12)
print('N=', N)

def TrojkatL(n):
  for wiersz in range(1, n + 1):
    print('#' * wiersz)
  print()

def TrojkatP(n):
  for wiersz in range(1, n + 1):
    print(' ' * (n - wiersz), '#' * wiersz, sep='')
  print()

def RogiObfitosci(n):
  for wiersz in range(1, n + 1):
    print('#' * wiersz, ' ' * (n - wiersz), sep='', end='')
    print(' ' * (n - wiersz), '#' * wiersz, sep='')
  print()

TrojkatL(N)
TrojkatP(N)
RogiObfitosci(N)
