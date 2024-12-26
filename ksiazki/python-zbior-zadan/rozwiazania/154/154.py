# kolorki do ładnego wyświetlania
dark = "\033[7m"
reset = "\033[0m"

from enum import Enum

class Bierki(Enum):
  bPionek = 'P'
  cPionek = 'p'
  bKrol = 'K'
  cKrol = 'k'
  bHetman = 'H'
  cHetman = 'h'
  bGoniec = 'G'
  cGoniec = 'g'
  bSkoczek = 'S'
  cSkoczek = 's'
  bWieza = 'W'
  cWieza = 'w'
  pusto = '.'

class Kolumny(Enum):
  A = 1
  B = 2
  C = 3
  D = 4
  E = 5
  F = 6
  G = 7
  H = 8

class Wiersze(Enum):
  w1 = 1
  w2 = 2
  w3 = 3
  w4 = 4
  w5 = 5
  w6 = 6
  w7 = 7
  w8 = 8

class Pole:
  def __init__(self):
    self.biale = True
    self.bierka: Bierki = Bierki.pusto

  def __str__(self):
    if self.biale:
      return dark + self.bierka.value + reset
    else:
      return self.bierka.value

  def __repr__(self):
    return self.__str__()

class Ruch:
  def __init__(self, zk=Kolumny.A, zw=Wiersze.w1, nk=Kolumny.A, nw=Wiersze.w1):
    self.ruch_z = []
    self.ruch_na = []
    self.ustaw(zk, zw, nk, nw)

  def ustaw(self, zk, zw, nk, nw):
    self.ruch_z = [zk, zw]
    self.ruch_na = [nk, nw]

class Szachownica:
  def __init__(self):
    self.szachownica = dict()  # { (Kolumna,Wiersz) : Pole }
    self.gra = []  # lista Ruch'ów
    self.restart()

  def restart(self):
    # początkowe ustawienie pionków na planszy
    for wiersz in Wiersze:
      for kolumna in Kolumny:
        p = Pole()
        if (int(wiersz.value) + kolumna.value) % 2 == 0:
          p.biale = False
        else:
          p.biale = True
        if wiersz == Wiersze.w1 and (kolumna in (Kolumny.A, Kolumny.H)):
          p.bierka = Bierki.bWieza
        elif wiersz == Wiersze.w8 and (kolumna in (Kolumny.A, Kolumny.H)):
          p.bierka = Bierki.cWieza
        elif wiersz == Wiersze.w1 and (kolumna in (Kolumny.B, Kolumny.G)):
          p.bierka = Bierki.bSkoczek
        elif wiersz == Wiersze.w8 and (kolumna in (Kolumny.B, Kolumny.G)):
          p.bierka = Bierki.cSkoczek
        elif wiersz == Wiersze.w1 and (kolumna in (Kolumny.C, Kolumny.F)):
          p.bierka = Bierki.bGoniec
        elif wiersz == Wiersze.w8 and (kolumna in (Kolumny.C, Kolumny.F)):
          p.bierka = Bierki.cGoniec
        elif wiersz == Wiersze.w1 and (kolumna == Kolumny.D):
          p.bierka = Bierki.bHetman
        elif wiersz == Wiersze.w8 and (kolumna == Kolumny.D):
          p.bierka = Bierki.cHetman
        elif wiersz == Wiersze.w1 and (kolumna == Kolumny.E):
          p.bierka = Bierki.bKrol
        elif wiersz == Wiersze.w8 and (kolumna == Kolumny.E):
          p.bierka = Bierki.cKrol
        elif wiersz == Wiersze.w2:
          p.bierka = Bierki.bPionek
        elif wiersz == Wiersze.w7:
          p.bierka = Bierki.cPionek
        else:
          p.bierka = Bierki.pusto
        self.szachownica[(kolumna, wiersz)] = p

  # dodaje ruch do listy ruchów gry, wykonuje ruch na szachownicy w obecnym stanie
  def rusz(self, r: Ruch, pokazywanie: bool = True):
    self.odtwarzaj(r)
    self.gra.append(r);
    if pokazywanie: self.pokaz()

  def odtwarzaj(self, r: Ruch):
    bierka = self.szachownica[(r.ruch_z[0], r.ruch_z[1])].bierka
    self.szachownica[(r.ruch_z[0], r.ruch_z[1])].bierka = Bierki.pusto
    self.szachownica[(r.ruch_na[0], r.ruch_na[1])].bierka = bierka

  # ustawia szachownicę na konkretny ruch z historii gry, 0 - początek.
  def pokaz_nty(self, i):
    tymczasowa = Szachownica()
    for j in range(0, i):
      tymczasowa.rusz(self.gra[j], False)
    tymczasowa.pokaz()

  # pokaż obecny stan szachownicy
  def pokaz(self):
    if (len(self.gra)):
      r = self.gra[-1]
      print(
        f'RUCH nr= {len(self.gra)} z {r.ruch_z[0].name}{r.ruch_z[1].value} na pozycję {r.ruch_na[0].name}{r.ruch_na[1].value}.')
    else:
      print('START GRY')
    for w in reversed(Wiersze):
      for k in Kolumny:
        print(self.szachownica[(k, w)], sep='', end='')
      print()
    print()

  def zapisz(self):
    with open('154_zapis_gry.txt', 'w', encoding='utf-8') as f:
      for r in self.gra:
        f.write(
          f'{r.ruch_z[0].value} {r.ruch_z[1].value} {r.ruch_na[0].value} {r.ruch_na[1].value}\n')

  def zapisz_nty(self, nty: int):
    with open('154_zapis_gry_ruch_nr' + str(nty) + '.txt', 'w',
              encoding='utf-8') as f:
      tymczasowa = Szachownica()
      for j in range(0, nty):
        tymczasowa.rusz(self.gra[j], False)
      for w in reversed(Wiersze):
        for k in Kolumny:
          f.write(f'{tymczasowa.szachownica[(k, w)].bierka.value}')
        f.write('\n')

  def odczyt(self):
    self.gra.clear()
    self.restart()
    with open('154_zapis_gry.txt', 'r', encoding='utf-8') as f:
      for ln in f:
        zk, zw, nak, naw = [int(x.strip()) for x in ln.split(' ')]
        r = Ruch()
        r.ruch_z = [Kolumny(zk), Wiersze(zw)]
        r.ruch_na = [Kolumny(nak), Wiersze(naw)]
        self.rusz(r, False)

s = Szachownica()
s.pokaz()

s.rusz(Ruch(Kolumny.A, Wiersze.w2, Kolumny.A,
            Wiersze.w4))  # biały pionek z A2 na A4 itd.
s.rusz(Ruch(Kolumny.A, Wiersze.w7, Kolumny.A, Wiersze.w5))
s.rusz(Ruch(Kolumny.H, Wiersze.w2, Kolumny.H, Wiersze.w4))
s.rusz(Ruch(Kolumny.E, Wiersze.w7, Kolumny.E, Wiersze.w5))
s.rusz(Ruch(Kolumny.G, Wiersze.w1, Kolumny.H, Wiersze.w3))
s.rusz(Ruch(Kolumny.B, Wiersze.w8, Kolumny.C, Wiersze.w6))

s.pokaz_nty(3)  # historyczny trzeci ruch
s.pokaz()  # ostatni ruch (szósty)
s.zapisz()
s.zapisz_nty(3)  # zapis kroku nr 3

s2 = Szachownica()
s2.odczyt()  # test odczytu, inna szachownica
s2.pokaz()
s2.pokaz_nty(4)
