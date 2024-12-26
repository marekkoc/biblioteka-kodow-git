from copy import deepcopy

K = 250  # kolumn
W = 250  # wierszy
multiple = 4  # mnożnik grubości "bitów" przy tworzeniu obrazka

class Gra:
  def __init__(self):
    self.krok = 0  # krok iteracji
    # dwuwymiarowa lista list W x K, komórki żywe (True) i martwe (False)
    self.komorki = []
    for i in range(K):
      self.komorki.append([False] * W)
    # dwuwymiarowa lista list W x K, zmiana stanu komórki w następnej iteracji:
    # True - na żywą, False - na martwą.
    self.stan = []
    for i in range(K):
      self.stan.append([False] * W)

  def iluZywychSasiadow(self, w, k):
    ile = 0
    # warunek na krawędzi obszaru
    if k in [0, K - 1] or w in [0, W - 1]: return ile
    for kmod, wmod in [(-1, -1), (-1, 0), (-1, 1), (0, 1), (0, -1), (1, -1),
                       (1, 0), (1, 1)]:
      if self.komorki[w + wmod][k + kmod]: ile += 1
    return ile

  def start(self, ozywione):
    '''
    Ustawia komórki ożywione na star gry.
    :param ozywione [(wiersz,kolumna), (100,100), ...]
    '''
    # wszystkie czynię martwymi
    for wiersz in self.komorki:
      for poz in range(len(wiersz)):
        wiersz[poz] = False
    for w, k in ozywione:
      self.komorki[w][k] = True
    self.toPBM();

  def tik(self):
    '''
    Jeden krok algorytmu.
    '''
    # ustawiam stany przyszłe na: komórka martwa
    for wiersz in self.stan:
      for poz in range(len(wiersz)):
        wiersz[poz] = False
    # analiza obecnej sytuacji
    for w in range(W):
      for k in range(K):
        i = self.iluZywychSasiadow(w, k)
        if (not self.komorki[w][k] and i == 3) or (
            self.komorki[w][k] and i in [2, 3]):
          self.stan[w][k] = True  # ożywa (żyje dalej)
    self.krok += 1
    self.komorki = deepcopy(self.stan)
    self.toPBM()
    print(f'Krok nr = {self.krok} wygenerowany.')

  def toPBM(self):
    with open(f'165_{self.krok}.pbm', 'w', encoding='utf-8') as f:
      f.write(f'P1\n')
      f.write(f'# Krok {self.krok}\n')
      f.write(f'{W * multiple} {K * multiple}\n')
      for wiersz in self.komorki:
        for i in range(1, multiple + 1):
          for poz in range(len(wiersz)):
            f.write(f'{str(int(wiersz[poz]))}' * multiple)

g = Gra()
g.start([(120, 120), (119, 121), (119, 122), (120, 122), (121, 122)])
for i in range(10):
  g.tik()
