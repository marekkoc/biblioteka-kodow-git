class Tusz:
  def __init__(self):
    self.kartka = 0
    self.CMYK = [0, 0, 0, 0]

  def czytajZLinii(self, wierszZPliku: str):
    self.kartka, *self.CMYK = [float(x) for x in
                               wierszZPliku.strip().split(' ')]

  def kosztKartki(self):
    '''
      kolor 100.00 zł/50.0 ml, czarny 40.00 zł/50.0 ml
      kolor 2.00 zł/1.0 ml, czarny 0.80 zł/1.0 ml
      50ml -> 72 kartki -> 7200% pokrycia
      1ml -> 144%
    '''
    koszt = 0.
    for a in [0, 1, 2]:  # kolory CMY
      koszt += 2 * (self.CMYK[a] / 144.)
    koszt += 0.8 * (self.CMYK[3] / 144.)  # czarny
    return koszt

  def procentPokryciaWielomaTuszami(self):
    suma_kolor = sum(self.CMYK)
    # tylko ten obszar, który pokrywają nakłądające się tusze
    return suma_kolor - self.kartka

kartki = []

with open('179_tusz.txt', 'r', encoding='utf-8') as f:
  f.readline()  # nagłówki
  for ln in f:
    kartki.append(Tusz())
    kartki[-1].czytajZLinii(ln)

print('Ilość kartek po przeczytaniu pliku:', len(kartki))

koszt = 0
for k in kartki:
  koszt += k.kosztKartki()
print(f'Koszt za tusz = {round(koszt, 2)}')

srednia = 0
for k in kartki:
  srednia += k.procentPokryciaWielomaTuszami()
print(f'Średnie pokrycie {round(srednia / len(kartki), 2)}')
