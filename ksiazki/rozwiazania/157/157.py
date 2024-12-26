import operator
from enum import Enum
from copy import deepcopy
from random import randint, shuffle

class kolor(Enum):
  trefl = 1
  pik = 2
  karo = 3
  kier = 4

class rodzaj(Enum):
  dwojka = 0
  trojka = 1
  czworka = 2
  piatka = 3
  szostka = 4
  siodemka = 5
  osemka = 6
  dziewiatka = 7
  dziesiatka = 8
  walet = 9
  dama = 10
  krol = 11
  As = 12  # as jest słówkiem zarezerwowanym, dałem As

modyfikator_punktowe = {kolor.trefl: 0, kolor.pik: 1, kolor.karo: 2,
                        kolor.kier: 3}

class Karta:
  def __init__(self, k: kolor, r: rodzaj):
    self.kolor = k
    self.rodzaj = r

  def punkty(self):
    return modyfikator_punktowe[self.kolor] + self.rodzaj.value

  def pokaz(self):
    print(f'{self.rodzaj.name} {self.kolor.name} [{self.punkty()}pkt.]')

class Gracz:

  def __init__(self, n: int):
    self.nr = n
    self.karty = []

  def pokaz_karty(self):
    for k in self.karty:
      k.pokaz()
    print(self.punkty(), 'pkt.')

  # suma punktów z kart
  def punkty(self):
    return sum(map(lambda k: k.punkty(), self.karty))

  def odrzuc_karty(self):
    odrzucone = deepcopy(self.karty)
    self.karty.clear()
    return odrzucone

class Stolik:
  def __init__(self, ilosc=0):
    self.gracze = []
    if ilosc == 0:
      self.ilosc = randint(2, 4)
    else:
      self.ilosc = ilosc
    for i in range(0, self.ilosc):
      self.gracze.append(Gracz(i))

  def ileGraczy(self):
    return len(self.gracze)

  def pokaz_karty_graczy(self):
    for g in self.gracze:
      print(f'Gracz nr: {g.nr}')
      g.pokaz_karty()

class Talia:
  def __init__(self):
    self.karty = []
    for i in range(1, 5):
      for k in range(0, 13):
        self.karty.append(Karta(kolor(i), rodzaj(k)))
    print(f'Utworzono nową talię złożoną z {len(self.karty)} kart.')

  def pokaz(self):
    for k in self.karty: k.pokaz()

  def potasuj(self):
    print(f'Rozpoczynam tasowanie talii kart.')
    shuffle(self.karty)

  def karta_dla_gracza(self, s: Stolik, nrGracza, nKart=1):
    for ile in range(1, nKart + 1):
      if len(self.karty):
        [g for g in s.gracze if g.nr == nrGracza][0].karty.append(
          self.karty[-1])
        self.karty.pop()

  # dodaję kartę do talii, bez sprawdzania, czy istnieje taka karta w talii
  def dodaj_karte(self, k: kolor, r: rodzaj):
    self.karty.append(Karta(k, r))

  def dodaj_karty(self, grupaKart: list):
    self.karty += grupaKart

# start
T = Talia()
T.potasuj()
# T.pokaz() # odkomentuj, by zobaczyć listę potasowanych kart w talii
S = Stolik()
# przekazuję z talii na stoliki graczy po 3 karty dla każdego
for nrGracza in range(0, S.ileGraczy()):
  T.karta_dla_gracza(S, nrGracza, 3)

print(f'Gracze mają następujące karty:')
S.pokaz_karty_graczy()

print(f'Kart w talii zostało {len(T.karty)}.')
# wyłaniam wygranego/wygranych
print('--- START ---')
pozycja = len(S.gracze)
while True:
  # sortowanie od gracza z największą ilością
  # punktów do gracza z najmniejszą ilością
  S.gracze = sorted(S.gracze[0:pozycja],
                    key=operator.methodcaller('punkty'), reverse=True)
  if (S.gracze[0].punkty() > S.gracze[1].punkty()): break  # jest!
  print('Nie udało się wyłonić zwycięzcy, emocjonująca dogrywka!')
  for pozycja in range(0, len(S.gracze)):
    if pozycja == len(S.gracze) or S.gracze[pozycja] != S.gracze[0]:
      pozycja = min(len(S.gracze), pozycja + 1)
      break
    pozycja += 1
  # Już wiem, do jakiej pozycji (bez niej) trzeba wykonać dogrywkę.
  # Zabieram też karty zwycięzcom, by zrobić dogrywkę.
  print(f'Dogrywka. Gracze o podanych numerach zwracają karty do talii.')
  for g in S.gracze[0:pozycja]:
    print('Nr:', g.nr, end=' ')
    T.dodaj_karty(g.odrzuc_karty())
  print()
  print('W talii jest obecnie: ', len(T.karty), 'kart.')
  # potasuj talię
  T.potasuj()
  # rozdaj ponownie karty dla osób z dogrywki
  print(f'Rozdaję ponownie karty odpowiednim graczom w dogrywce')
  for g in S.gracze[0:pozycja]:
    T.karta_dla_gracza(S, g.nr, 3)
    g.pokaz_karty()
  print('W talii pozostało: ', len(T.karty), 'kart.')

# Mam wygranego. Jest na początku listy: S.gracze
print('ZWYCIĘŻA GRACZ NR ', S.gracze[0].nr, 'z takimi kartami:')
S.gracze[0].pokaz_karty()

# Obliczanie prawdopodobieństwa.
# 3 karty mogę wylosować na 52! / (3! * (52-3)!) sposobów, czyli 22100.
# Obliczanie prawdopodobieństwa bez wzorów:
Tsym = Talia()
wszystkieMozliweTrojkiKart = 0
trojkiKartPonizej15 = 0
for poz1 in range(0, len(Tsym.karty)):
  for poz2 in range(poz1 + 1, len(Tsym.karty)):
    for poz3 in range(poz2 + 1, len(Tsym.karty)):
      wszystkieMozliweTrojkiKart += 1
      if (Tsym.karty[poz1].punkty() + Tsym.karty[poz2].punkty() + Tsym.karty[
        poz3].punkty() < 15):
        trojkiKartPonizej15 += 1
print(f'Wszystkich trójek kart: {wszystkieMozliweTrojkiKart}.\n'
      f'Trójek kart nie przekraczających 15 {trojkiKartPonizej15}.\n'
      f'Prawdopodobieństwo to {trojkiKartPonizej15 / wszystkieMozliweTrojkiKart}')
