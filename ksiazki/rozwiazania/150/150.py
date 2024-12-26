import random
from functools import cmp_to_key

class Dane:
  def __init__(self, oznaczajPierwsze=False):
    self.w = random.randint(10, 99)  # zakres nie ma większego znaczenia
    self.oznaczajPierwsze = oznaczajPierwsze

  def __mul__(self, other):
    for i in range(other):
      yield Dane()

  def pierwsza(self):
    for i in range(2, self.w):
      if self.w % i == 0: return False
    return True

  def __str__(self):
    if self.oznaczajPierwsze and self.pierwsza():
      return str(self.w) + '*'
    else:
      return str(self.w)

  def __repr__(self):
    if self.oznaczajPierwsze and self.pierwsza():
      return str(self.w) + '*'
    else:
      return str(self.w)

lista = [e for e in Dane() * 20]
print(lista)

print('Sortowanie parzyste-nieparzyste:')
f = lambda e: e.w % 2 == 1  # nieparzysta jest "większa"
lista = sorted(lista, key=f)
print(lista)

print('Sortowanie parzyste malejąco - nieparzyste rosnąco:')

def g(e1, e2):
  if e1.w % 2 == 0 and e2.w % 2 == 0 and e1.w >= e2.w: return -1
  if e1.w % 2 == 1 and e2.w % 2 == 1 and e1.w <= e2.w: return -1
  if e1.w % 2 == 0 and e2.w % 2 == 1: return -1
  return 0

lista = sorted(lista, key=cmp_to_key(g))
print(lista)

print('Sortowanie pierwsze* - pozostałe:')

for e in lista: e.oznaczajPierwsze = True
lista = sorted(lista, key=lambda e: e.pierwsza(), reverse=True)
print(lista)
