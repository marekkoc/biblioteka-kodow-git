import math
from random import randint

def czyPierwsza(n: int):
  if n < 2: return False
  for dzielnik in range(2, int(math.sqrt(n)) + 1):
    if n % dzielnik == 0:
      return False
  return True

# test
for i in range(1, 100):
  if czyPierwsza(i):
    print(i, end=', ')
print()

# część zadania z losowaniem
ile = 0
for i in range(1000):
  if czyPierwsza(randint(2, 1000)):
    ile += 1
print('Wylosowano ', ile,
      'liczb pierwszych dla 1000 losowań z zakresu <2;1000>.')
