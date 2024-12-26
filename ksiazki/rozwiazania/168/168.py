from enum import Enum
from fractions import Fraction
from time import sleep

class Klawisz(Enum):
  Pauza = 1
  C = 2
  D = 3
  E = 4
  F = 5
  G = 6
  A = 7
  H = 8
  Cis = 9
  Dis = 10
  Fis = 11
  Gis = 12
  Ais = 13

class Oktawa(Enum):
  O1 = 1  # 'O1 nie 01'
  O2 = 2
  O3 = 3
  O4 = 4

class atom:
  domyslnie = Fraction(1, 16)  # minimalna jednostka czasu

  def __init__(self, licznik=None, mianownik=None):
    if licznik is not None and mianownik is not None:
      self.wartosc = Fraction(licznik, mianownik)
    else:
      self.wartosc = atom.domyslnie

  def __call__(self, *args, **kwargs):
    return self.wartosc

class czas:
  def __init__(self, i: int, licznik=1, mianownik=16):
    self.ile = i
    self.atom = atom(licznik, mianownik)

class Dzwiek:
  def __init__(self, klaw: Klawisz, okt: Oktawa, czas_tr: int):
    self.klawisz = klaw
    self.oktawa = okt
    self.czas_trwania = czas(czas_tr)

class Melodia:
  def __init__(self):
    self.nutki = []  # lista dźwięków Dzwiek

  def dodaj(self, k: Klawisz, o: Oktawa, t: int):
    if o == Oktawa.O4 and k != Klawisz.C:
      print(f'Niedozwolony zakres!')  # D4, E4 itd. Można tylko C4.
      return
    self.nutki.append(Dzwiek(k, o, t))

  def graj(self):
    print('START')
    for d in self.nutki:
      if d.klawisz != Klawisz.Pauza:
        print(f'{d.klawisz.name} {d.oktawa.name} ...', end='')
      else:
        print(' (pauza) ', end='')
      # obliczam czas trwania w przybliżonych mikrosekundach
      catom = (d.czas_trwania.atom().numerator /
               d.czas_trwania.atom().denominator)
      print(f'{d.czas_trwania.ile * catom}s.')
      sleep(d.czas_trwania.ile * catom)
    print('KONIEC')

  def do_pliku(self, nazwa=''):
    with open(nazwa, 'w', encoding='utf-8') as f:
      for d in self.nutki:
        f.write(f'{d.klawisz.value} {d.oktawa.value} {d.czas_trwania.ile}\n')

  def z_pliku(self, nazwa=''):
    self.nutki.clear()
    with open(nazwa, 'r', encoding='utf-8') as f:
      for ln in f:
        kl, ok, c = ln.strip().split(' ')
        self.nutki.append(Dzwiek(Klawisz(int(kl)), Oktawa(int(ok)), int(c)))

M = Melodia()
M.dodaj(Klawisz.C, Oktawa.O2, 32)
M.dodaj(Klawisz.D, Oktawa.O2, 32)
M.dodaj(Klawisz.E, Oktawa.O2, 32)
M.dodaj(Klawisz.F, Oktawa.O2, 32)

M.dodaj(Klawisz.Pauza, Oktawa.O2, 16)

M.dodaj(Klawisz.G, Oktawa.O2, 2)
M.dodaj(Klawisz.A, Oktawa.O2, 2)
M.dodaj(Klawisz.H, Oktawa.O2, 16)
M.dodaj(Klawisz.C, Oktawa.O3, 8)

M.do_pliku('168_melodia.txt')
M.z_pliku('168_melodia.txt')

M.graj()
