w = 54
k = 177

def zlicz(dane, wiersz, kolumna):
  wynik = 0
  for i in range(wiersz - 3, wiersz + 4):
    for j in range(kolumna - 3, kolumna + 4):
      if dane[i][j] == '#':
        wynik += 1
  return wynik - 1  # nie liczę znaku na pozycji wiersz x kolumna

with open('144_znaki.txt', 'r', encoding='utf-8') as f:
  dane = []
  for ln in f:
    dane.append([])
    for znak in ln.strip():
      dane[-1].append(znak)

for wiersz in range(3, w - 3):
  for kolumna in range(3, k - 3):
    if (dane[wiersz][kolumna] == '#'):
      x = zlicz(dane, wiersz, kolumna)
      if x >= 4:
        print(f'Istnieje obszar dla znaku # o pozycji {wiersz + 1} '
              f'x {kolumna + 1} zawierający {x} znaków #.')
