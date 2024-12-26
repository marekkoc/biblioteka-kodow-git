from random import randint

N = randint(3, 10)
# może być więcej niż 10, ale to nie konkurs na wysokość choinki.
print('N=', N)

# wykorzystamy Piramidę z innego zadania
def Piramida(n, spacje=0):
  for wiersz in range(1, n // 2 + 2):
    print(' ' * spacje, end='')
    print(' ' * (n // 2 - wiersz + 1), '#' * (wiersz * 2 - 1), sep='')

def Choinka(n):
  start = 5
  for czlon in range(1, n + 1):
    Piramida(start, n - czlon)
    start += 2
  print(' ' * ((start - 2) // 2), '#', sep='')  # pieniek

Choinka(N)
print()

def PiramidaP(n, spacje=0):
  for wiersz in range(1, n // 2 + 2):
    print(' ' * spacje, end='')
    print(' ' * (n // 2 - wiersz + 1), end='')
    if wiersz == 1 or wiersz == n // 2 + 1:
      print('#' * (wiersz * 2 - 1), end='')
    else:
      print('#', ' ' * (wiersz * 2 - 3), '#', end='', sep='')
    print()

def ChoinkaP(n):
  start = 5
  for czlon in range(1, n + 1):
    PiramidaP(start, n - czlon)
    start += 2
  print(' ' * ((start - 2) // 2), '#', sep='')  # pieniek

ChoinkaP(N)
