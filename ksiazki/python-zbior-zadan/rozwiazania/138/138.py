import random

ile_wydarzen = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0}
szanse = {'A': 5, 'B': 20, 'C': 50, 'D': 60, 'E': 90}
# odliczanie to
# {wydarzenie, [sekundy od ostatniego wydarzenia, co ile skund wydarzenie], }
odliczanie = {'A': [0, 1], 'B': [0, 3], 'C': [0, 4], 'D': [0, 7.5], 'E': [0, 8]}
ile_sek_od_D = -1  # ile upłynęło czasu od D
odD = 3  # type potrzeba po D, aby wydarzyło się E
czyD = False
krok_czasu = 0.5  # w sekundach
czas = 0  # czas trwania całej symulacji w sekundach
ileA = 10  # tyle razy potrzeba zdarzenia A, by zatrzymać symulację

def szansa(s):
  return random.randint(1, 100) <= s

# symulacja
while True:
  czyD = False  # czy w tej jednostce czasu wydarzyło się D?
  # A
  # jeżeli minął czas oczekiwania na zdarzenie
  if (odliczanie['A'][0] == odliczanie['A'][1]):
    if szansa(szanse['A']):
      # print('[A] w ', czas, 'sekundzie.')  # usuń komentarz, by widzieć
      ile_wydarzen['A'] += 1  # wydarzenie zaistniało
    odliczanie['A'][0] = 0  # zerowanie czasu oczekiwania
  odliczanie['A'][0] += krok_czasu
  if ile_wydarzen['A'] == ileA:
    print('A=', ileA, 'STOP!')
    break
  # B,C,D
  for c in ('B', 'C', 'D'):
    if (odliczanie[c][0] == odliczanie[c][1]):
      if szansa(szanse[c]):  # zaistniało wdarzenie
        ile_wydarzen[c] += 1
        # print(f'[{c}] w {czas} sekundzie.') # usuń komentarz, by widzieć
        if c == 'D':
          czyD = True
          ile_sek_od_D = 0
      odliczanie[c][0] = 0
    odliczanie[c][0] += krok_czasu
  if ile_sek_od_D >= 0 and not czyD:
    ile_sek_od_D += krok_czasu
  # E
  if ile_sek_od_D <= odD and ile_sek_od_D != -1:
    pass  # usuń komentarz dla print(), by widzieć
    # print(f'ile sekund od D: {ile_sek_od_D}')

  if odliczanie['E'][0] == odliczanie['E'][1] and ile_sek_od_D <= odD:
    if szansa(szanse['E']):
      ile_wydarzen['E'] += 1
      # print(f'[E] w {czas} sekundzie.') # usuń komentarz, by widzieć
    odliczanie['E'][0] = 0
  odliczanie['E'][0] += krok_czasu
  czas += krok_czasu
  # print(f'CZAS = {czas} sek.') # odkomentuj by widzieć upływ czasu

print('Ile razy wystąpiło każde wydarzenie?')
print(ile_wydarzen)
print('Symulacja trwała ', czas, 'sekund')
