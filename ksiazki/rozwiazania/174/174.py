class Plansza:
  def __init__(self):
    self.pola = []  # lista list, wiersz i kolumny
    for i in range(101):
      self.pola.append([0] * 101)
    self.pozycja_pionka = (50, 50)
    self.pola[50][50] += 1

  def ruch(self, kierunek: int):
    if kierunek not in [1, 2, 3, 4, 5, 6]:
      print('Ruch niemożliwy, błędny kierunek.')
      return (-1, -1)
    x, y = self.pozycja_pionka
    if y % 2 == 0:
      match kierunek:
        case 1:
          y -= 1
          x += 1
        case 2:
          x += 1
        case 3:
          y += 1
          x += 1
        case 4:
          y += 1
        case 5:
          x -= 1
        case 6:
          y -= 1
    elif y % 2 == 1:
      match kierunek:
        case 1:
          y -= 1
        case 2:
          x += 1
        case 3:
          y += 1
        case 4:
          y += 1
          x -= 1
        case 5:
          x -= 1
        case 6:
          y -= 1
          x -= 1
    if x < 0 or y < 0 or x > 100 or y > 100:
      # print(f'Ruch poza planszą!') # możesz odkomentować, by widzieć
      return (-1, -1)
    self.pozycja_pionka = (x, y)
    self.pola[x][y] += 1
    return (x, y)

  def seriaRuchow(self, L: list):
    return [self.ruch(kierunek) for kierunek in L]

p1 = Plansza()
p2 = Plansza()

ruchy = []

with open('174_ruch.txt', 'r', encoding='utf-8') as f:
  for ln in f:
    ruchy.extend(int(x) for x in ln.strip().split('\t'))

print(ruchy)
pozycje1 = p1.seriaRuchow(ruchy)
print(f'Pozycja pionka startującego z 50,50 to obecnie: {p1.pozycja_pionka}')
p2.pozycja_pionka = (87, 90)
p2.seriaRuchow(ruchy)
print(f'Pozycja pionka startującego z 87, 90 to obecnie: {p2.pozycja_pionka}')

m = 0  # maksymalna liczba odwiedzeń pola
pozx = -1
pozy = -1
for x in range(0, len(p1.pola)):
  for y in range(0, len(p1.pola)):
    if p1.pola[x][y] > 0 and m < p1.pola[x][y]:
      m = p1.pola[x][y]
      pozx = x
      pozy = y
print(f'Pole ({pozx},{pozy}) odwiedzono największą liczbę razy = {m}')

ile_w_wierszach = dict()  # {wiersz:ile}
mw = 0
ilosc = 0
for x, y in pozycje1:
  if y == -1: continue  # ruch nieudany
  ile_w_wierszach.setdefault(y, 0)
  ile_w_wierszach[y] += 1
  if ilosc < ile_w_wierszach[y]:
    ilosc = ile_w_wierszach[y]
    mw = y
print(f'Wiersz o maksymalnej liczbie odwiedzin = {ilosc} to wiersz = {mw}')
