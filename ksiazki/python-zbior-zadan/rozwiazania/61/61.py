from random import randint

N = randint(5, 30)
print('N=', N)

def KwadratMalpy(n):
  a, b = randint(2, n - 1), randint(2, n - 1)  # pozycja @
  for wiersz in range(1, n + 1):
    for kolumna in range(1, n + 1):
      if (wiersz == a and kolumna == b):
        print('@', sep='', end='')
      else:
        print('#', end='', sep='')
    print()
  print()
  print()

def KwadratMalpyP(n):
  a, b = randint(2, n - 1), randint(2, n - 1)  # pozycja @
  for wiersz in range(1, n + 1):
    for kolumna in range(1, n + 1):
      if (wiersz == a and kolumna == b):
        print('@', sep='', end='')
      else:
        if wiersz in [1, n] or kolumna in [1, n]:
          print('#', end='', sep='')
        else:
          print(' ', end='', sep='')
    print()
  print()
  print()

KwadratMalpy(N)
KwadratMalpyP(N)
