class Element:
  def __init__(self, dane: list):
    self.oceny = dane  # oceny typu float

  def sa(self):
    return sum(self.oceny) / len(self.oceny)

  def __eq__(self, other):
    return abs(self.sa() - other.sa()) <= 0.5

  def __lt__(self, other):
    return self.sa() < other.sa() and other.sa() - self.sa() > 0.5

  def __gt__(self, other):
    return self.sa() > other.sa() and self.sa() - other.sa() > 0.5

  def __str__(self):
    return str(self.oceny) + ' średnia:' + str(round(self.sa(), 3)) + '\n'

L = [Element([1, 1, 2, 3, 6]), Element([1, .5, .9, 3.5, 2, 6]),
     Element([8, 11, 3, 4, 0.1, 3, 2, 0.01]),
     Element([3, 6, 4, 1, 3.5, 22]), Element([1, 1, 2, 3, 6]),
     Element([1, .5, .9, 3.5, 2, 3, 9, 6, 8, 4]),
     Element([1]), Element([0.5, 0.5, 0.2]), Element([-2, -5, 1, -0.5])]

# teraz sortowanie bąbelkowe z elementami:

# rosnąco
for i in range(len(L), 0, -1):
  for poz in range(0, i - 1):
    if L[poz] > L[poz + 1]:
      L[poz], L[poz + 1] = L[poz + 1], L[poz]
print('Porządek rosnący:')
print(*L, sep='')

# malejąco
for i in range(len(L), 0, -1):
  for poz in range(0, i - 1):
    if L[poz] < L[poz + 1]:
      L[poz], L[poz + 1] = L[poz + 1], L[poz]
print('Porządek malejący:')
print(*L, sep='')
