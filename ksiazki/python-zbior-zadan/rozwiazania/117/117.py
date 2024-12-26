class Wierzcholek:
  def __init__(self, d: int):
    self.dane = d
    self.plewy: Wierzcholek = None
    self.pprawy: Wierzcholek = None
    self.odwiedzony = False
    self.rodzic: Wierzcholek = None  # niekonieczne

  def __str__(self):
    return str(self.dane)

class DrzewoBinarne:
  def __init__(self):
    self.korzen: Wierzcholek = None
    self.pozycja: Wierzcholek = None
    self.dopokazania = dict()  # posłuży do pokazania drzewa metodą VLR

  def dodaj(self, d: int):
    if isinstance(d, list):
      for e in d:
        self.dodaj(e)
      return
    nowy = Wierzcholek(d)
    if self.korzen is None:
      self.korzen = self.pozycja = nowy
    else:
      self.pozycja = self.korzen
      while not (self.pozycja is None):
        if d > self.pozycja.dane and self.pozycja.pprawy is not None:
          self.pozycja = self.pozycja.pprawy
        elif d <= self.pozycja.dane and self.pozycja.plewy is not None:
          self.pozycja = self.pozycja.plewy
        elif d > self.pozycja.dane and self.pozycja.pprawy is None:
          self.pozycja.pprawy = nowy
          nowy.rodzic = self.pozycja
          self.pozycja = self.pozycja.pprawy
          break
        elif d <= self.pozycja.dane and self.pozycja.plewy is None:
          self.pozycja.plewy = nowy
          nowy.rodzic = self.pozycja
          self.pozycja = self.pozycja.plewy
          break

  def buduj(self, p: Wierzcholek, glebokosc: int = 0, pl=''):
    if p is None:
      return
    if not p.odwiedzony:
      self.dopokazania.setdefault(glebokosc, '')
      self.dopokazania[glebokosc] += (
          pl + str(p) + '[' + str(p.rodzic) + ']' + '\t')
      p.odwiedzony = False
    self.buduj(p.plewy, glebokosc + 1, 'L')
    self.buduj(p.pprawy, glebokosc + 1, 'P')

  def pokaz(self):
    self.buduj(self.korzen)
    for linia, tresc in self.dopokazania.items():
      print(tresc)
    self.dopokazania.clear()

db = DrzewoBinarne()
db.dodaj(40)
db.dodaj([10, 60])
db.pokaz()  # przykład z zadania
print()
# dalsze testy drzewa
db.dodaj(10)
db.dodaj([20, 30, 40, 50, 5, 8, 13, 21, -4, -6, -10, -12, 0, 0])
db.pokaz()
# Interpretacja wyświetlonego wyniku:
# Wiersze to poziomy drzewa. L/P to informacja, czy potomek jest lewy, czy prawy.
# W nawiasie [] widać, kto jest rodzicem. [None] oznacza brak rodzica.
