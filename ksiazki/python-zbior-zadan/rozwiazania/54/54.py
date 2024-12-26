from random import randint

L = []
ile = randint(10, 100)
print('Ilość = ', ile)
for i in range(ile):
  L.append(randint(1, 50))
print(L)

def zmiany(x):
  if x % 2 == 0:
    return 0
  return -x

print(list(map(zmiany, L))[::-1])
