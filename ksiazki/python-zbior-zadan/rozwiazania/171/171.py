class Prostopadloscian:
  def __init__(self, a, b, c):
    self.a = a
    self.b = b
    self.c = c

  def objetosc(self):
    return self.a * self.b * self.c

  def polePodstawy(self):
    return self.a * self.b

  def __lt__(self, inny):
    if self.objetosc() < inny.objetosc():
      return True
    elif self.objetosc() > inny.objetosc():
      return False
    if self.c < inny.c:
      return True
    elif self.c > inny.c:
      return False
    if self.polePodstawy() < inny.polePodstawy():
      return True
    elif self.polePodstawy() > inny.polePodstawy():
      return False

  def __eq__(self, inny):
    return (self.objetosc() == inny.objetosc() and
            self.c == inny.c and self.polePodstawy() == inny.polePodstawy())

  def __gt__(self, inny):
    return not (self < inny or self == inny)

  def __ge__(self, inny):
    return not self < inny

  def __le__(self, inny):
    return self == inny or self < inny

  @staticmethod
  def quicksort(L, lewy: int, prawy: int):
    if prawy <= lewy: return
    pivot = L[lewy]
    z_lewa = lewy + 1
    pozycja = lewy + 1
    while z_lewa <= prawy:
      if pivot >= L[z_lewa]:
        L[z_lewa], L[pozycja] = L[pozycja], L[z_lewa]
        pozycja += 1
      z_lewa += 1
    L[lewy], L[pozycja - 1] = L[pozycja - 1], L[lewy]
    Prostopadloscian.quicksort(L, lewy, pozycja - 2)
    Prostopadloscian.quicksort(L, pozycja, prawy)

  def __str__(self):
    return (f'\n<{self.a}, {self.b}, {self.c} Objętość={self.objetosc()}'
            f' PolePodst={self.polePodstawy()} Wysokość= {self.c}>')

  def __repr__(self):
    return self.__str__()

from random import randint

L = []
for i in range(100):
  L.append(Prostopadloscian(randint(1, 100),
                            randint(1, 100), randint(1, 100)))
Prostopadloscian.quicksort(L, 0, len(L) - 1)
# po posortowaniu
print(L)
