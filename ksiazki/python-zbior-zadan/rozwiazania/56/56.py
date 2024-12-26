from random import randint

N = randint(5, 12)
print('N=', N)

def Szachownica(n):
  for wiersz in range(1, n + 1):
    for kolumna in range(1, n + 1):
      if (wiersz % 2 and kolumna % 2) or (not wiersz % 2 and not kolumna % 2):
        print('#', end='')
      else:
        print(' ', end='')
    print()

Szachownica(N)
