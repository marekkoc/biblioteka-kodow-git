import operator
import copy
from random import randint

class PPM:
  def __init__(self, Y, X):
    self.piksele = []  # dwuwymiarowa lista pikseli
    for i in range(X):
      self.piksele.append([])
      for j in range(Y):
        self.piksele[-1].append('{0:024b}'.format(0))

  def PPM(self, plik: str):
    with open(plik + '.ppm', 'w', encoding='utf-8') as f:
      f.write('P3\n')
      f.write('# PPM wygenerowany automatycznie przez <class PPM>\n')
      if len(self.piksele) > 0:
        f.write(f'{len(self.piksele[0])} {len(self.piksele)}\n')
        f.write('256\n')  # kolorowy PPM
        # rysujemy
        for x in self.piksele:
          for bit in x:
            f.write(f'{str(int(bit[0:8], 2))} ')
            f.write(f'{str(int(bit[8:16], 2))} ')
            f.write(f'{str(int(bit[16:24], 2))}\n')
      else:
        f.write('0 0\n256\n')

  def rgb2bit24(self, czerwony: int, zielony: int, niebieski: int):
    return '{0:08b}'.format(czerwony) + '{0:08b}'.format(
      zielony) + '{0:08b}'.format(niebieski)

  def wstaw(self, pozycja: int, czerwony: int, zielony: int, niebieski: int):
    self.piksele[pozycja].append(self.rgb2bit24(czerwony, zielony, niebieski))

class Kafelek:
  globalny_nr = 1

  def __init__(self, x: int, y: int, czerwony: int, zielony: int,
               niebieski: int):
    self.nr = Kafelek.globalny_nr
    Kafelek.globalny_nr += 1
    self.rx = x
    self.ry = y
    self.czerwony = czerwony
    self.zielony = zielony
    self.niebieski = niebieski

  def pole(self):
    return self.rx * self.ry

  def __lt__(self, inny):
    return self.pole() < inny.pole()

  def __gt__(self, inny):
    return self.pole() > inny.pole()

  def __hash__(self):
    return self.nr

  def __repr__(self):
    return f'\n({self.rx}:{self.ry}) ppow.={self.pole()}'

class Podloga:
  def __init__(self, rx=400, ry=250):
    self.x = rx
    self.y = ry  # cm
    # kafelki leżące na podłodze i ich położenie (lewy górny narożnik 1x1 cm
    self.kafelki = dict()  # {Kafelek:(x,y)}
    self.cm_nieprzykryte = set()  # ( (x,y) )
    self.cm_przykryte = set()
    for wys in range(0, self.y):
      for szer in range(0, self.x):
        self.cm_nieprzykryte.add((szer, wys))

  def czyMogePolozyc(self, k: Kafelek, px: int, py: int):
    '''
    Obliczam cm. kwadratowe, które przykryłby kafelek, gdybym mógł go położyć
    '''
    do_przykrycia = set()
    if py + k.ry > self.y: return False  # poza podłogą
    if px + k.rx > self.x: return False
    for w in range(py, py + k.ry):
      for s in range(px, px + k.rx):
        do_przykrycia.add((s, w))
    cz_wspolna = set()
    return not bool(len(do_przykrycia.intersection(self.cm_przykryte)))

  def poloz(self, k: Kafelek, px: int, py: int):
    '''
    Kładzie kafelek na Podłogę.
    '''
    for w in range(py, py + k.ry):
      for s in range(px, px + k.rx):
        self.cm_przykryte.add((s, w))
        self.cm_nieprzykryte.remove((s, w))
    self.kafelki[k] = (px, py)

  def pozycja_pierwszego_nieprzykrytego(self):
    '''
Szukaj pierwszego nieprzykrytego cm.kw. od lewej do prawej i od góry do dołu.
    '''
    if len(self.cm_nieprzykryte) == 0: return (self.x, self.y)
    for pozy in range(0, self.y):
      for pozx in range(0, self.x):
        if (pozx, pozy) in self.cm_nieprzykryte: return (pozx, pozy)
    return (-1, -1)

  def pozycja_pierwszego_nieprzykrytego_2(self):
    '''
Szukaj pierwszego nieprzykrytego cm.kw. od góry do dołu i od lewej do prawej.
    '''
    if len(self.cm_nieprzykryte) == 0: return (self.x, self.y)
    for pozx in range(0, self.x):
      for pozy in range(0, self.y):
        if (pozx, pozy) in self.cm_nieprzykryte: return (pozx, pozy)
    return (-1, -1)

  def wizualizacja(self, plik: str):
    '''
    Zamienia podłogę na plik PPM
    '''
    ppm = PPM(self.x, self.y)
    for k, pos in self.kafelki.items():
      kx = pos[0]
      ky = pos[1]
      for kroky in range(ky, k.ry + ky):
        for krokx in range(kx, k.rx + kx):
          ppm.piksele[kroky][krokx] = ppm.rgb2bit24(k.czerwony, k.zielony,
                                                    k.niebieski)
    ppm.PPM(plik)

# dostępne kafelki
piwnica = {Kafelek(25, 35, 20, 20, 20): 52,
           Kafelek(100, 50, 50, 50, 50): 8,
           Kafelek(15, 25, 90, 90, 90): 32,
           Kafelek(40, 40, 120, 120, 120): 19,
           Kafelek(5, 5, 200, 200, 200): 49,
           Kafelek(5, 10, 250, 100, 100): 89
           }
piwnica = dict(
  sorted(piwnica.items(), key=operator.itemgetter(0), reverse=True))

P = Podloga(400, 250)

# Algorytm kładzenia, zachłanny sposób poszukiwania pokrycia podłogi.
while len(P.cm_nieprzykryte) > 0:
  przed = len(P.cm_nieprzykryte)  # przed próbą pokrycia
  for kaf, ile in piwnica.items():
    while ile > 0:
      wolnaPozycja = P.pozycja_pierwszego_nieprzykrytego()
      wolnaPozycja2 = P.pozycja_pierwszego_nieprzykrytego_2()
      kc = copy.deepcopy(kaf)
      kcrev = Kafelek(kc.ry, kc.rx, kc.czerwony, kc.zielony, kc.niebieski)
      # czy mogę położyć kafelek kc/kcrev (na różne sposoby)
      if P.czyMogePolozyc(kc, wolnaPozycja[0], wolnaPozycja[1]):
        kc.czerwony = kc.zielony = randint(0, 255)
        kc.niebieski = randint(0, 255)
        P.poloz(kc, wolnaPozycja[0], wolnaPozycja[1])
        ile -= 1
        piwnica[kaf] -= 1
      elif P.czyMogePolozyc(kcrev, wolnaPozycja[0], wolnaPozycja[1]):
        kcrev.czerwony = kcrev.zielony = randint(0, 255)
        kcrev.niebieski = randint(0, 255)
        P.poloz(kcrev, wolnaPozycja[0], wolnaPozycja[1])
        ile -= 1
        piwnica[kaf] -= 1
      elif P.czyMogePolozyc(kc, wolnaPozycja2[0], wolnaPozycja2[1]):
        kc.czerwony = kc.zielony = randint(0, 255)
        kc.niebieski = randint(0, 255)
        P.poloz(kc, wolnaPozycja2[0], wolnaPozycja2[1])
        ile -= 1
        piwnica[kaf] -= 1
      elif P.czyMogePolozyc(kcrev, wolnaPozycja2[0], wolnaPozycja2[1]):
        kcrev.czerwony = kcrev.zielony = randint(0, 255)
        kcrev.niebieski = randint(0, 255)
        P.poloz(kcrev, wolnaPozycja2[0], wolnaPozycja2[1])
        ile -= 1
        piwnica[kaf] -= 1
      else:
        break  # nie da się nic położyć, przejdę do mniejszego kafelka
  # nie udało się położyć żadnego kafelka
  if przed == len(P.cm_nieprzykryte): break

print(f'Porkytce cm kwadratowe: {len(P.cm_przykryte)}')
print(f'Niepokrytce cm kwadratowe: {len(P.cm_nieprzykryte)}')
print(f'W piwnicy pozostało: \n')
print(piwnica)
P.wizualizacja('178')
