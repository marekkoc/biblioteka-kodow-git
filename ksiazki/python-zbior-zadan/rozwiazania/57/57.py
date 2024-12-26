from random import randint

N = randint(5, 12)
print('N=', N)
M = randint(5, 12)
print('M=', M)

def ProstokatPusty(n, m):
  for wiersz in range(1, n + 1):
    for kolumna in range(1, m + 1):
      if wiersz in [1, n] or kolumna in [1, m]:
        print('#', end='')
      else:
        print(' ', end='')
    print()

ProstokatPusty(N, M)
