class Element:
  def __init__(self, d, p):
    self.dane: int = d
    self.priorytet: bool = p

  # poniższe funkcje gt, eq oraz ge definiują
  # operatory pomiędzy obiektami Element
  def __gt__(self, other):
    return (self.priorytet == True and other.priorytet == False or
            self.priorytet == other.priorytet and self.dane > other.dane)

  def __eq__(self, other):
    return (self.priorytet == other.priorytet and self.dane == other.dane)

  def __ge__(self, other):
    return (self > other or self == other)

  def __str__(self):
    return '<' + str(self.dane) + ':' + str(self.priorytet) + '>'

from copy import deepcopy

def mergesort(v: list, lewy: int, prawy: int):
  if lewy >= prawy: return
  temp = deepcopy(v)
  q = (lewy + prawy) // 2
  mergesort(temp, lewy, q)
  mergesort(temp, q + 1, prawy)
  poz = lewy
  lkrok = lewy
  pkrok = q + 1
  while lkrok <= q and pkrok <= prawy:
    if temp[lkrok] <= temp[pkrok]:
      v[poz] = temp[lkrok]
      poz += 1
      lkrok += 1
    else:
      v[poz] = temp[pkrok]
      poz += 1
      pkrok += 1
  while lkrok <= q:
    v[poz] = temp[lkrok]
    poz += 1
    lkrok += 1
  while pkrok <= prawy:
    v[poz] = temp[pkrok]
    poz += 1
    pkrok += 1

V = [Element(10, True), Element(-5, False), Element(1, True),
     Element(50, False), Element(0, False), Element(0, True),
     Element(33, False), Element(-5, True), Element(-5, True),
     Element(12, False), Element(-6, False), Element(-7, True),
     Element(44, False), Element(1, True), Element(20, False),
     Element(17, False), Element(19, False), Element(33, True),
     Element(-22, True)]
print(*V)
mergesort(V, 0, len(V) - 1)
print(*V)  # posortowane
