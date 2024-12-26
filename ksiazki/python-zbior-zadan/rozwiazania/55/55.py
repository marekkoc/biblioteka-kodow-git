from random import randint

N = randint(5, 12)
print('N=', N)

def X(n):
  # wzór na ilość spacji przed pierwszym # i po nim
  if n & 1:
    spacje1 = list(range(n // 2 + 1)) + list(range(n // 2))[::-1]
    spacje2 = list(range(n - 2, -1, -2)) + [0] + list(range(1, n - 1, 2))
  else:
    spacje1 = list(range(n // 2)) + list(range(n // 2))[::-1]
    spacje2 = list(range(n - 2, -1, -2)) + list(range(0, n - 1, 2))

  for wiersz in range(n):
    if n & 1 and spacje2[wiersz] == 0:
      print(spacje1[wiersz] * ' ', '#', spacje2[wiersz] * ' ', sep='')
    else:
      print(spacje1[wiersz] * ' ', '#', spacje2[wiersz] * ' ', '#', sep='')

X(N)
