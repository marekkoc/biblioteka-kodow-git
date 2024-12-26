import random

T = 1000

class Szescian:
  def __init__(self, a):
    self.a = a

  def __str__(self):
    return f'[{str(self.a)}]'

  def __lt__(self, other):
    return self.a < other.a

  def __gt__(self, other):
    return self.a > other.a

  def __eq__(self, other):
    return self.a == other.a

Li = []  # wszystkie sześciany

def segregator(N: int):
  if N > T: return (0, 0)  # za duże N
  A = []  # jako stos A (ostatni element to szczyt stosu)
  B = []  # jako stos B (ostatni element to szczyt stosu)
  for i in range(1, N + 1):
    szescian = Li[i - 1]
    if i % 2 == 1:  # nieparzysta pozycja sześcianu
      if len(A) == 0 or A[-1] < szescian:
        A.append(szescian)
    else:
      if len(B) == 0 or B[-1] > szescian:
        B.append(szescian)
  return (len(A), len(B))

def gen():
  for i in range(1, T + 1):
    Li.append(Szescian(round(random.randint(1, 1000) / 100, 2)))

def objetosc(N):
  if N > T: return 0
  o = 0
  # pozycje na liście Li. Z nich wylosuję N pozycji.

  wszystkie_pozycje = list(range(0, T))
  random.shuffle(wszystkie_pozycje)
  for poz in wszystkie_pozycje[0:N]:
    o += Li[poz].a ** 3  # objętość ogólna zwiększa się o objętość sześcianu
  return o

gen()
print(*Li, sep='')
print(len(Li))

print(objetosc(3))  # objętość 3 przypadkowych sześcianów z listy Li

ile = 100
ileA, ileB = segregator(ile)
print(
  f'Dla N={ile} na stosie A znalazło się {ileA} sześcianów.'
  f' Na stosie B znalazło się {ileB} sześcianów.')

# testy operatorów <, > (oraz ==)
print(Szescian(10) < Szescian(20))  # True
print(Szescian(10) > Szescian(20))  # False
print(Szescian(10) == Szescian(20))  # False
print(Szescian(10) == Szescian(10))  # True
