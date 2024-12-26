"""
Poniższe rozwiązanie opatrzyłem nadmiarowymi metodami wewnątrz klas. Zrobiłem
to nie bez powodu. Metody __init__, __del__ i __str__, opatrzone
odpowiednimi komunikatami, pozwolą uważnemu czytelnikowi dokładnie prześledzić,
co dzieje się podczas tworzenia obiektów, i kiedy następuje ich skasowanie.
"""

class Dane:
  def __init__(self, napis, liczba):
    self.napis = napis
    self.liczba = liczba
    print('Nowe Dane', self, 'ID=', id(self))

  def __str__(self):
    return f'<{self.napis}, {str(self.liczba)}>'

  def __del__(self):
    print('Skasowano Dane ID=', id(self), self)

class ElementStosu:
  def __init__(self, napis, liczba):
    self.dane = Dane(napis, liczba)
    self.podSpodem = None
    print('Nowy ElementStosu, ID=', id(self))

  def __str__(self):
    return str(self.dane)

  def __del__(self):
    print('Skasowano ElementStosu', 'ID=', id(self))

class Stos:
  def __init__(self):
    self.len = 0
    self.szczyt = None

  def dodaj(self, napis, liczba):
    nowy = ElementStosu(napis, liczba)
    if self.len == 0:
      self.szczyt = nowy
    else:
      nowy.podSpodem = self.szczyt
      self.szczyt = nowy
    self.len += 1

  def usun(self):
    if self.len > 0:
      self.len -= 1
      pomoc = self.szczyt.podSpodem
      del self.szczyt  # porzucam obiekt szczytowy
      self.szczyt = pomoc

  def pokazSzczyt(self):
    return 'Na szczycie stosu leży' + str(self.szczyt)

  def szczytKopia(self):
    print('Rozpoczyna się kopiowanie szczytowego elementu.')
    import copy
    self.len += 1
    nowy = copy.deepcopy(self.szczyt)  # głęboka kopia
    nowy.dane.napis += ' (deepcopy)'
    nowy.podSpodem = self.szczyt
    self.szczyt = nowy

  def pokazWszystkie(self):
    temp = self.szczyt
    while temp:
      print(temp)
      temp = temp.podSpodem

# Dla obiektów A i B klasy Dane, obie wartości tak wykorzystane są referencją.
A = Dane('Karaczan', 1000)
B = A
B.napis = 'Wiewiórka'
B.liczba = 5000
print(A, B)  # zmiana B zmienia A -> te same dane
del A, B  # sprzątam

print(60 * '_')
print()

s = Stos()
s.dodaj('Karaczan', 1000)
s.dodaj('Muchomor', -400)
s.dodaj('Wiewiórka', 5000)
print(s.pokazSzczyt(), 'Obiektów:', s.len)
s.usun()
print(s.pokazSzczyt(), 'Obiektów:', s.len)
s.szczytKopia()
print(s.pokazSzczyt(), 'Obiektów:', s.len)
s.pokazWszystkie()

print()
print(60 * '=')
print('Zakończenie programu poprzedza czyszczenie obiektów:')
print(60 * '=')
# w momencie zakończenia programu dane stosu i tak są kasowane:
