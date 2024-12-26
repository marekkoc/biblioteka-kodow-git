class wgr:
  """
  Wierzchołek grafu
  """

  def __init__(self):
    self.nr = 0
    self.wyjscia = dict()  # { nr : waga połączenia }

  def __str__(self):
    return f'[nr={self.nr}]'

class G:
  def __init__(self):
    self.N = 0  # liczba wierzchołków
    self.wierzcholki = dict()  # wierzchołki => nr : wierzchołek

  def raport(self, nr):
    """
    Funkcja pokazuje połączenia wierzchołka o podanym numerze.
    """
    if nr > self.N: return False
    wgrroot = self.wierzcholki[nr]
    print(f'Polaczenia z wierzchołka nr {nr}:')
    for doWgrNr, waga in wgrroot.wyjscia.items():
      print(f'\twierzchołek nr={doWgrNr} połączenie waga={waga}.')
    return True

  def dodaj(self, ile=1):
    """
    Dodaje wierzchołki do grafu, jeszcze nie ustanawia połączeń między nimi.
    """
    while ile:
      nr = len(self.wierzcholki) + 1
      self.wierzcholki[nr] = wgr()
      self.wierzcholki[nr].nr = nr
      self.N += 1
      ile -= 1

  def polacz(self, w1, w2, waga):
    """
    Połącz wierzchołek w1 z w2 i nadaj wagę połączeniu
    """
    if w1 > self.N or w2 > self.N: return False
    self.wierzcholki[w1].wyjscia[w2] = waga
    self.wierzcholki[w2].wyjscia[w1] = waga
    return True

  def rozlacz(self, w1, w2):
    """
    Rozłącz wierzchołek numer w1 z w2
    """
    if w1 > self.N or w2 > self.N: return False
    del self.wierzcholki[w1].wyjscia[w2]
    del self.wierzcholki[w2].wyjscia[w1]

# buduję graf zgodnie z zadaniem
graf = G()
graf.dodaj(6)
graf.polacz(1, 2, 7)
graf.polacz(1, 5, 10)
graf.polacz(2, 3, 2)
graf.polacz(3, 6, 8)
graf.polacz(4, 2, 4)
graf.polacz(4, 6, 1)
graf.polacz(4, 5, 1)

# raport połączeń
print(graf.N)
for i in range(1, 7):
  graf.raport(i)

graf.rozlacz(2, 4)

print(graf.N)
for i in range(1, 7):
  graf.raport(i)
