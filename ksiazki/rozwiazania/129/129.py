class Wierzcholek:
  def __init__(self, d: int):
    """Konstruktor wierzchołka.
    Podaj wartość przechowywanej liczby całkowitej."""
    self.dane = d
    self.plewy: Wierzcholek = None
    self.pprawy: Wierzcholek = None
    self.odwiedzony = False
    self.rodzic: Wierzcholek = None
    self.tozsamosc = ''  # wierzchołek wie, czy jest lewym czy prawym potomkiem

  def __str__(self):
    return str(self.dane)

  def __del__(self):
    print('Wierzchołek', self.dane, '(', self.tozsamosc, ') zniknął z pamięci.')

class DrzewoBinarne:
  def __init__(self):
    """Konstruktor drzewa."""
    self.korzen: Wierzcholek = None
    self.pozycja: Wierzcholek = None
    # posłuży do pokazania drzewa metodą VLR z uwzględnieniem poziomów
    self.dopokazania = dict()
    # aktualnie wskazywany wierzchołek
    self.wskazany: Wierzcholek = None

  def dodaj(self, d: int):
    """Dodawanie nowego wierzchołka lub listy wierzchołków."""
    if isinstance(d, list):
      for e in d:
        self.dodaj(e)
      return
    nowy = Wierzcholek(d)
    if self.korzen is None:
      self.korzen = self.pozycja = self.wskazany = nowy
      nowy.tozsamosc = 'korzeń'
    else:
      self.pozycja = self.korzen
      while self.pozycja is not None:
        if d > self.pozycja.dane and self.pozycja.pprawy is not None:
          self.pozycja = self.pozycja.pprawy
        elif d <= self.pozycja.dane and self.pozycja.plewy is not None:
          self.pozycja = self.pozycja.plewy
        elif d > self.pozycja.dane and self.pozycja.pprawy is None:
          self.pozycja.pprawy = nowy
          nowy.tozsamosc = 'prawy'
          nowy.rodzic = self.pozycja
          self.pozycja = self.pozycja.pprawy
          break
        elif d <= self.pozycja.dane and self.pozycja.plewy is None:
          self.pozycja.plewy = nowy
          nowy.tozsamosc = 'lewy'
          nowy.rodzic = self.pozycja
          self.pozycja = self.pozycja.plewy
          break
      del self.pozycja

  def wezWskazany(self):
    """Zwróć wartość wskazanego aktualnie wierzchołka."""
    if not (self.wskazany is None):
      return self.wskazany.dane

  def pokazWsazany(self):
    """Pokaż wskazany wierzchołek."""
    if not (self.wskazany is None):
      print('Wskazany aktualnie:', self.wskazany, end=' ')
      if not (self.wskazany.rodzic is None):
        print('[', self.wskazany.rodzic.dane, ']', sep='', end='')
      i = 0
      if self.wskazany.plewy: i += 1
      if self.wskazany.pprawy: i += 1
      print(' Potomków=', i, sep='')
      print()

  def buduj(self, p: Wierzcholek, glebokosc: int = 0, pl=''):
    """Pomocnicza dla metody pokaz(self), rysującej drzewo."""
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
    """Pokazuje drzewo."""
    print('DRZEWO: L-lewy potomek, P-prawy potomek,'
          ' [n]-wartość rodzica, [None] - brak rodzica')
    self.buduj(self.korzen)
    for linia, tresc in self.dopokazania.items():
      print(tresc)
    self.dopokazania.clear()

  def szukaj(self, szukana: int) -> bool:
    """
    :param szukana: szukana wartość w drzewie
    :return: True/False
    """
    pomoc = self.korzen
    while True:
      if not (pomoc is None):
        if pomoc.dane == szukana:
          return True
        elif szukana < pomoc.dane:
          pomoc = pomoc.plewy
        else:
          pomoc = pomoc.pprawy
      else:
        return False

  def __pos__(self):
    """Przesun się do prawego potomka"""
    if not (self.wskazany.pprawy is None):
      self.wskazany = self.wskazany.pprawy
    else:
      print('Niemożliwe przejście do prawego potomka.')

  def __neg__(self):
    """Przesuń się do lewego potomka"""
    if not (self.wskazany.plewy is None):
      self.wskazany = self.wskazany.plewy
    else:
      print('Niemożliwe przejście do lewego potomka.')

  def __invert__(self):
    """Przesuń się do rodzica"""
    if not (self.wskazany.rodzic is None):
      self.wskazany = self.wskazany.rodzic
    else:
      print('Niemożliwe przejście do rodzica.')

  def testPoprawnosci(self, w: Wierzcholek) -> bool:
    lewy = prawy = True
    if (w.plewy is not None and w.dane < w.plewy.dane
        or w.pprawy is not None and w.dane >= w.pprawy.dane):
      return False
    if w.plewy is not None and w.dane >= w.plewy.dane:
      lewy = self.testPoprawnosci(w.plewy)
    if w.pprawy is not None and w.dane < w.pprawy.dane:
      prawy = self.testPoprawnosci(w.pprawy)
    if lewy and prawy: return True
    return False

  def kasujWskazanyBezPotomkow(self):
    """Kasuję obecnie wskazany wierzchołek, o ile nie ma potomków."""
    if self.wskazany.rodzic is not None:
      r = self.wskazany.rodzic
    else:
      r = None
    if self.wskazany is not None:
      print('!!! Rozpoczynam kasowanie wskazanego bez potomków.')
      if self.wskazany.pprawy is None and self.wskazany.plewy is None:
        if self.wskazany.tozsamosc == 'lewy':
          if self.wskazany.rodzic is not None:
            self.wskazany.rodzic.plewy = None
        elif self.wskazany.tozsamosc == 'prawy':
          if self.wskazany.rodzic is not None:
            self.wskazany.rodzic.pprawy = None
        del self.wskazany
        self.wskazany = r
      else:
        print('!!!Operacja kasowania wstrzymana. Istnieją potomkowie.')

  def wartosci(self, w: Wierzcholek):
    if w is not None:
      yield w.dane
      yield from self.wartosci(w.plewy)
      yield from self.wartosci(w.pprawy)

  def kopia(self, bez=[]):
    nowe = DrzewoBinarne()
    wart = list(self.wartosci(self.korzen))
    for n in wart:
      if n not in bez:
        nowe.dodaj(n)
    return nowe

db = DrzewoBinarne()
db.dodaj(40)
db.dodaj([10, 60])
db.pokaz()  # przykład z zadania
print()
# dalsze testy drzewa
db.dodaj(10)
db.dodaj([20, 30, 40, 50, 5, 8, 13, 21, -4, -6, -10, -12, 0, 0, 42])
db.pokaz()  # pokaż całe drzewo
db.pokazWsazany()  # pokaż wskazanego
# przeszukiwanie
print(db.szukaj(111), db.szukaj(40))  # 111 False, 40 True
# poruszanie się wewnątrz drzewa:
+db  # idź do prawego
db.pokazWsazany()
-db  # idź do lewego
db.pokazWsazany()
-db  # idź do lewego (o ile się da!)
db.pokazWsazany()  # ten sam, bo nie miał lewego potomka
~db  # idź do rodzica
~db
db.pokazWsazany()
~db  # nie da się, nie ma rodzica
# testy poprawności
print('Poprawność:', db.testPoprawnosci(db.korzen))
# a teraz zepsujemy drzewo...
+db
-db
# db.wskazany.dane = 1000 # zepsułem drzewo, reguła złamana!
db.pokaz()  # widać 1000 na niewłaściwej pozycji
print('Poprawność:', db.testPoprawnosci(db.korzen))

# teraz idziemy do liścia (ostatnie korzenie) i kasujemy
-db
db.pokazWsazany()
db.kasujWskazanyBezPotomkow()
db.pokazWsazany()
db.kasujWskazanyBezPotomkow()
db.kasujWskazanyBezPotomkow()
db.pokazWsazany()
db.kasujWskazanyBezPotomkow()
db.pokaz()

nowe = db.kopia([10, -4, -6, -10, -12])
nowe.pokaz()

print()
print('Koniec programu, czyszczenie:')
print('_' * 60)
