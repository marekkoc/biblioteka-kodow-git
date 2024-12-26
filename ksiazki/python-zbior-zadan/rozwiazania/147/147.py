class wgr:
  """
  Wierzchołek grafu
  """

  def __init__(self):
    self.nr = 0
    self.wyjscia = dict()  # { nr : waga polaczenia }

  def __str__(self):
    return f'[nr={self.nr}]'

class G:
  def __init__(self):
    self.N = 0  # liczba wierzchołków
    self.wierzcholki = dict()  # wierzchołki => nr : wierzchołek

  def raport(self, nr):
    """
    Funkcja pokazuje polaczenia wierzchołka o podanym numerze.
    """
    if nr > self.N: return False
    wgrroot = self.wierzcholki[nr]
    print(f'Polaczenia z wierzchołka nr {nr}:')
    for doWgrNr, waga in wgrroot.wyjscia.items():
      print(f'\twierzchołek nr={doWgrNr} polaczenie waga={waga}.')
    return True

  def dodaj(self, ile=1):
    """
    Dodaje wierzchołki do grafu, jeszcze nie ustanawia polaczeń między nimi.
    """
    while ile:
      nr = len(self.wierzcholki) + 1
      self.wierzcholki[nr] = wgr()
      self.wierzcholki[nr].nr = nr
      self.N += 1
      ile -= 1

  def polacz(self, w1, w2, waga):
    """
    Polacz wierzchołek w1 z w2 i nadaj wagę polaczeniu
    """
    if w1 > self.N or w2 > self.N: return False
    self.wierzcholki[w1].wyjscia[w2] = waga
    self.wierzcholki[w2].wyjscia[w1] = waga
    return True

  def rozlacz(self, w1, w2):
    """
    Rozlacz wierzchołek numer w1 z w2
    """
    if w1 > self.N or w2 > self.N: return False
    del self.wierzcholki[w1].wyjscia[w2]
    del self.wierzcholki[w2].wyjscia[w1]

# buduję graf zgodnie z zadaniem
g = G()
g.dodaj(6)
g.polacz(1, 2, 7)
g.polacz(1, 5, 10)
g.polacz(2, 3, 2)
g.polacz(3, 6, 8)
g.polacz(4, 2, 4)
g.polacz(4, 6, 1)
g.polacz(4, 5, 1)

# zastosuję do zadania swój pomysł (rekurencyjny)
wszystkie = dict()

# znajdzie ścieżki
def przeszukiwanie(graf: G, w_od, w_do, sciezka: list, wagaRazem=0):
  sciezka.append(w_od)  # start
  if w_od == w_do:
    wszystkie[tuple(sciezka)] = wagaRazem
    return
  for sasiad, waga in graf.wierzcholki[w_od].wyjscia.items():
    if not sasiad in sciezka:
      nowa = sciezka.copy()
      przeszukiwanie(graf, sasiad, w_do, nowa, wagaRazem + waga)

przeszukiwanie(g, 1, 6, [])

for s, w in wszystkie.items():
  print(*s, sep='->', end=' ')
  print('=', w)

print()
wszystkie.clear()
przeszukiwanie(g, 3, 5, [])
for s, w in wszystkie.items():
  print(*s, sep='->', end=' ')
  print('=', w)
