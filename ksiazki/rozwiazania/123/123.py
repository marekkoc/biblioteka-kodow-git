# zwraca wszystkie dzielniki liczby całkowitej
import math

def dzielniki(c: int):
  for dzielnik in range(1, c + 1):
    if c % dzielnik == 0:
      yield dzielnik

def wzgledniePierwsze(a: int, b: int):
  dzielnikia = list(dzielniki(a))
  dzielnikib = list(dzielniki(b))
  for da in dzielnikia:
    if da > 1 and da in dzielnikib:
      return False
  return True

zbior1 = {2, 6, 7, 8, 9}
zbior2 = {12, 21, 98, 101, 77, 231, 24, 10}

for z in [zbior1, zbior2]:
  print('\nDla zbioru', z, 'następujące pary są względnie pierwsze:')
  sprawdzone = set()
  for a in z:
    for b in z:
      if a == b: continue
      if (a, b) not in sprawdzone and (b, a) not in sprawdzone:
        if (wzgledniePierwsze(a, b)):
          print(f'<{a},{b}>', end=' ; ')
        sprawdzone.add((a, b))
