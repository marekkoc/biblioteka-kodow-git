'''
Korzystam z:
(A * B) mod C = ((A mod C) * (B mod C)) mod C

Obliczamy rekurencyjnie f(a, b, x) = (a**x%b) ==
(a*a**(x-1))%b == ((a%b) * (a**(x-1)%b))%b ==
(a%b**f(a, b, x-1))%b  -> tu widać mechanizm rekurencji
'''

def funkcja(a, b, x):
  '''
  Bo a do potęgi 0 to 1, a 1%b == 1 (warunek stopu rekurencji)
  '''
  if x[0] == 0: return 1
  w = ((a % b) * funkcja(a, b, [x[0] - 1])) % b
  return w

def istnieje(a, b, c, x):
  for i in range(0, b):
    x[0] = i
    if funkcja(a, b, x) == c:
      return True
  return False

'''
Uwaga! Głęboka rekurencja może spowodować wyjątek przepełnienia stosu.
Poniższa zasobożerna instrukcja: 
  sys.setrecursionlimit(10000)
pozwala mi na zwiększenie domyślnego limitu. Dzięki temu ostatni przykład
zostanie policzony.
'''
import sys

print(sys.getrecursionlimit())  # domyślnie pozwala się na 1000 rekursji.
sys.setrecursionlimit(10000)  # zaszalejemy!

x = [0]
print('Dla 551, 6634, 457:', end=' ')
if istnieje(551, 6634, 457, x):
  print(x[0])
else:
  print('-')

print('Dla 78, 11, 3', end=' ')
if istnieje(78, 11, 3, x):
  print(x[0])
else:
  print('-')

print('Dla 2280, 3045, 660:', end=' ')
if istnieje(2280, 3045, 660, x):
  print(x[0])
else:
  print('-')

print('Dla 4568, 9065, 1505:', end=' ')
if istnieje(4568, 9065, 1505, x):
  print(x[0])
else:
  print('-')
