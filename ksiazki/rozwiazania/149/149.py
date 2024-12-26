import random

# do kolorowania
blue = "\033[94m"
reset = "\033[0m"
dark = "\033[7m"
znaki = {'góry': '#', 'równiny': ' ', 'wyżyny': '*', 'rzeki': '='}

mapa = dict()  # { (x,y) : znak }
x = 50  # kolumny na mapie
y = 20  # wiersze na mapie

for i in range(1, y + 1):
  for j in range(1, x + 1):
    if (i == 1 or j == 1 or i == y or j == x):
      mapa[(j, i)] = znaki['góry']  # krawędzie
    else:  # a teraz losowo pola i równiny w proporcji około 3:1
      if random.randint(1, 100) <= 75:
        mapa[(j, i)] = znaki['równiny']
      else:
        mapa[(j, i)] = znaki['wyżyny']

# generuję rzekę
x_start = 2  # od krawędzi zachodu (2) do wschodu (x-1)
y_start = random.randint(2, y - 2)
mod = 0  # czynnik losowości 'skręcający' rzekę
while x_start <= x - 1:
  mod_szansa = random.randint(1, 100)
  if mod_szansa < 34:
    mod += 1
  elif mod_szansa < 67:
    mod -= 1
  szerokosc: int = random.randint(1, 3)
  for i in range(0, szerokosc):
    if y_start + i + mod <= y - 1 and y_start + i + mod > 1:
      mapa[(x_start, y_start + i + mod)] = znaki['rzeki']
    else:
      x_start -= 1
      break
  x_start += 1

# pokaż na ekranie, zapis do pliku
with open('149_mapa.txt', 'w', encoding='utf-8') as f:
  for i in range(1, y + 1):
    for j in range(1, x + 1):
      f.write(mapa[(j, i)])
      if mapa[(j, i)] == znaki['rzeki']:
        print(dark, blue, mapa[(j, i)], reset, sep='', end='')
      else:
        print(dark, mapa[(j, i)], reset, sep='', end='')
    f.write('\n')
    print()
