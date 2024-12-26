class ElementKolejki:
  def __init__(self, lista):
    self.dane = []
    self.dane.extend(lista)
    self.za = None  # jaki element `stoi` za tym elementem

  def __str__(self):
    return str(self.dane)

  def __del__(self):
    print('ElementKolejki: usuwanie. Dane:', self, 'ID:', id(self))

class Kolejka:
  def __init__(self):
    self.len = 0
    self.pierwszy = None
    self.ostatni = None

  def naKoniec(self, lista=[]):
    nowy = ElementKolejki(lista)
    if self.len == 0:
      self.pierwszy = nowy
    else:
      self.ostatni.za = nowy
    self.ostatni = nowy
    self.len += 1

  def opuscPoczatek(self):
    if self.len == 1:
      self.len -= 1
      del self.pierwszy, self.ostatni  # to ten sam element, gdy jest tylko 1
    elif self.len > 1:
      pomoc = self.pierwszy.za
      # Operacja del nie jest konieczna.
      # Obiekt zniknie wraz z ostatnią referencją do niego.
      del self.pierwszy
      self.pierwszy = pomoc
      self.len -= 1
    else:
      pass

  def pokazPierwszy(self):
    return self.pierwszy.dane

  def pokazOstatni(self):
    return self.ostatni.dane

  def pokazWszystko(self):
    if self.len > 0:
      print('W kolejce znajdują się: ', end=' ')
      pomoc = self.pierwszy
      while pomoc:
        print(pomoc, end=' ')
        pomoc = pomoc.za
      print()
    else:
      print('Kolejka jest pusta.')

k = Kolejka()

k.naKoniec([1, 2, 3])  # dodawanie elementu do kolejki (na koniec)
k.naKoniec([4, 5])
k.naKoniec([7, 8, 9, 10])

print(k.pokazPierwszy())  # pokaż pierwszy (dane z listy)
print(k.pokazOstatni())  # pokaż ostatni
print(k.len)  # ilość elementów w kolejce

k.opuscPoczatek()  # element z początku opuszcza kolejkę (o ile jest)
print(k.pokazPierwszy())
print(k.pokazOstatni())

k.pokazWszystko()

k.opuscPoczatek()
k.opuscPoczatek()
k.opuscPoczatek()
print(k.len)
k.pokazWszystko()

print()
print('*' * 60)
print('Sprzątanie pamięci na koniec programu.')
print('*' * 60)
