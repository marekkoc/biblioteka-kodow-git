import math

czerwony = '\033[91m'
reset = '\033[0m'

planety = [('Ziemia', 9.8), ('Merkury', 3.7), ('Wenus', 8.9),
           ('Mars', 3.7), ('Jowisz', 25.9), ('Saturn', 11.2), ('Uran', 8.6),
           ('Neptun', 11.2)]

# droga w metrach, przyśpieszenie w m/s**2, czas w sekundach
def oblicz_czas(droga, przyspieszenie):
  return round(math.sqrt(2.0 * droga / przyspieszenie), 5)

def oblicz_droga(s, przyspieszenie):
  return round((przyspieszenie * s ** 2) / 2, 5)

class P:
  """Przedmiot"""

  def __init__(self):
    self.leci = True
    self.droga = 0
    self.czas = 0

przedmioty = dict()
for planeta, p in planety:
  przedmioty[planeta] = P()

import time as t

start = t.time()
odliczanie = t.time()
leca = True  # przedmioty jeszcze lecą

while leca:
  s = t.time() - start
  leca = False
  for planeta, p in planety:
    if przedmioty[planeta].leci:
      leca = True
      m = oblicz_droga(s, p)
      przedmioty[planeta].czas = s
      przedmioty[planeta].droga = m
      if m >= 1500:
        przedmioty[planeta].leci = False
        print()
        print(czerwony, 'Przedmiot upadł na', planeta, 'po czasie',
              przedmioty[planeta].czas, 'sek i przebył drogę',
              przedmioty[planeta].droga, reset)
  c = t.time() - odliczanie
  if c >= 3:
    print(round(s, 2), 's.', sep='', end='\t')
    for planeta, p in planety:
      if przedmioty[planeta].leci:
        # print(planeta,przedmioty[planeta].droga,'m')
        pass
    odliczanie = t.time()

# obliczenia bez symulacji:
print()
print('Obliczenia dokonane bez symulacji.')
for planeta, p in planety:
  print(planeta, '\t\tczas=', oblicz_czas(1500, p))
