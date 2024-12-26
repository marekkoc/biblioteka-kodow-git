class ElementListy:
  def __init__(self, d: int = 0):
    self.dane = d
    self.lewy: ElementListy = None
    self.prawy: ElementListy = None

  def __str__(self):
    return '<' + str(self.dane) + '>'

  def __del__(self):
    print('Usunięto z pamięci ', self)

class ListaDC:
  def __init__(self):
    self.len = 0
    self.wskazany: ElementListy = None

  def element(self):
    return self.wskazany

  def wLewo(self):
    if self.len > 1:
      self.wskazany = self.wskazany.lewy

  def wPrawo(self):
    if self.len > 1:
      self.wskazany = self.wskazany.prawy

  def wyswietl(self, kierunek='P'):
    if self.len > 0:
      if kierunek == 'P':  # wyświetlamy idąc w prawo
        for krok in range(1, self.len + 1):
          print(self.wskazany, end=' ')
          self.wPrawo()
        print('Elementów:', self.len)
      else:
        for krok in range(1, self.len + 1):
          print(self.wskazany, end=' ')
          self.wLewo()
        print('Elementów:', self.len)
    else:
      print('ListaDC jest pusta.')

  def wstawZa(self, d: int = 0):
    if isinstance(d, list):
      for e in d:
        self.wstawZa(e)
      return  # po prostu wyjdzie z funkcji
    nowy = ElementListy(d)
    if self.len == 0:
      pass
    elif self.len == 1:
      nowy.prawy = nowy.lewy = self.wskazany
      self.wskazany.lewy = self.wskazany.prawy = nowy
    else:
      nowy.lewy = self.wskazany
      nowy.prawy = self.wskazany.prawy
      self.wskazany.prawy.lewy = nowy
      self.wskazany.prawy = nowy
    self.wskazany = nowy
    self.len += 1

  def usun(self):
    if self.len > 0:
      print('Usuwam', self.wskazany)
      if self.len == 1:
        self.wskazany = None
      elif self.len == 2:
        pomoc: ElementListy = self.wskazany.lewy
        pomoc.lewy = pomoc.prawy = None
        self.wskazany = pomoc
      else:
        pomoc: ElementListy = self.wskazany
        pomoc.lewy.prawy = pomoc.prawy
        pomoc.prawy.lewy = pomoc.lewy
        self.wskazany = pomoc.prawy
      self.len -= 1

  def usunWszystkie(self, d: int):
    while True:
      znaleziony = False
      for krok in range(1, self.len + 1):
        if self.wskazany.dane == d:
          self.usun()
          znaleziony = True
          break
        self.wPrawo()
      if not znaleziony: break

# testy działania
ldc = ListaDC()  # nowa lista dwukierunkowa cykliczna
ldc.wyswietl()  # pokaż zawartość (pusta)
ldc.wstawZa(1)  # wstaw jeden element
ldc.wstawZa(
  [10, 15, 30, 30, 50, 100])  # wstawia kolejno: za 1->10, za 10->15 itd.
print(ldc.len) # ilość elementów
ldc.wyswietl('L')  # wyświetla idąc w lewo
ldc.wyswietl()  # wyświetla idąc w prawo
ldc.wPrawo()  # przesuń się wewnątrz listy na następny element w prawo
ldc.wyswietl()
ldc.wLewo()  # przesuń się w lewo
ldc.wyswietl()
print(ldc.element())  # pokaż aktualnie wskazany
print(ldc.wskazany)  # można też tak bez pośrednictwa metody
ldc.usun()
ldc.wyswietl()
ldc.usunWszystkie(30)  # usuwam wszystkie 30
ldc.wyswietl()
# usuwam prawie wszystkie
ldc.usun()
ldc.usun()
ldc.usun()
ldc.wyswietl()
ldc.wPrawo()  # sprawdzam cykliczność w prawo dla 1-ego elementu
ldc.wyswietl()
ldc.wLewo()  # sprawdzam cykliczność w lewo dla 1-ego elementu
ldc.wyswietl()
# usuwam wszystko
ldc.usun()
ldc.usun()
ldc.wyswietl()
ldc.wstawZa(1000)
ldc.wyswietl()

print('=' * 60)
print('Koniec programu. Sprzątanie po sobie.')
print('=' * 60)
