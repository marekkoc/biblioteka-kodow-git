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
    # modyfikacje względem zadań 136, 137
    self.koszty = dict()
    self.poprzednik = dict()
    self.ZbiorQ = []
    self.ZbiorS = []

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

# przygotowanie grafu do poszukiwań

def przygotowanie(graf: G):
  for nr, w in graf.wierzcholki.items():
    graf.koszty[nr] = -1
    graf.poprzednik[nr] = -1
    graf.ZbiorQ.append(nr)

# zwraca wierzchołek o najmniejszym koszcie dojścia
def min_koszt(graf: G):
  koszt = 1000
  for nr in graf.ZbiorQ:
    if graf.koszty[nr] != -1 and koszt > graf.koszty[nr]:
      koszt = graf.koszty[nr]
      m = nr
  return m

def dijkstra(graf: G, w_od, w_do):
  graf.koszty[w_od] = 0
  while len(graf.ZbiorQ):
    minkosztnr = min_koszt(graf)
    graf.ZbiorQ.remove(minkosztnr)
    graf.ZbiorS.append(minkosztnr)
    for sasiad, waga in graf.wierzcholki[minkosztnr].wyjscia.items():
      if sasiad in graf.ZbiorQ:
        if graf.koszty[sasiad] == -1 or graf.koszty[sasiad] > graf.koszty[
          minkosztnr] + waga:
          graf.koszty[sasiad] = graf.koszty[minkosztnr] + waga
          graf.poprzednik[sasiad] = minkosztnr
  sciezka = w_do
  s = []
  while True:
    s.append(str(sciezka))
    if graf.poprzednik[sciezka] == -1: break
    sciezka = graf.poprzednik[sciezka]
  print(' -> '.join(reversed(s)))

print('Odpowiedzi:')
przygotowanie(g)
dijkstra(g, 1, 6)

print('Odpowiedź:')
przygotowanie(g)
dijkstra(g, 5, 3)
