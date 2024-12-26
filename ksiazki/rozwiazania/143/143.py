Li = []
ile_wierszy = 0
ile_kolumn = 0
with open('143_litery.txt', 'r', encoding='utf-8') as f:
  for ln in f:
    ile_kolumn = len(ln.strip())
    for znak in ln.strip():
      Li.append(znak)
ile_wierszy = int(len(Li) / ile_kolumn)

print(Li)
print(f'W pliku wykryto {ile_kolumn} kolumn i {ile_wierszy} wierszy.')

def wiersz(lista, nr: int):
  if nr > ile_wierszy: return []
  fragment = []
  for poz in range((nr - 1) * ile_kolumn, (nr - 1) * ile_kolumn + ile_kolumn):
    fragment.append(lista[poz])
  return fragment

def kolumna(lista, nr: int):
  if nr > ile_kolumn: return []
  fragment = []
  poz = nr - 1
  step = 1
  while True:
    if step > ile_wierszy: break
    fragment.append(lista[poz])
    step += 1
    poz += ile_kolumn
  return fragment

def podaj(lista, typ: str = 'w', nr: int = 0):
  if typ == 'w':
    return wiersz(lista, nr)
  else:
    return kolumna(lista, nr)

def dwie_podobne(f1: list, f2: list):
  """
  Sprawdza, czy listy znaków f1 i f2 są podobne, ale nie identyczne

  """
  if (f1 == f2): return False  # identyczne!
  if (len(f1) != len(f2)): return False  # nie mogą być podobne w podanym sensie
  f1c = f1.copy()
  f2c = f2.copy()
  for znak in f1c:
    if znak in f2c:
      f2c.remove(znak)
  return not len(f2c)  # pusty f2c oznacza podobieństwo

# przykład wyciągania wiersza/kolumny
print(podaj(Li, 'w', 4))  # podaj 4-ty wiersz licząc od 1
print(podaj(Li, 'k', 1))  # podaj 1-ą kolumnę licząc od 1
print()

# rozwiązania:
# Czy istnieją dwie identyczne kolumny? (takie same znaki na odpowiednich pozycjach)
for kol1 in range(1, ile_kolumn + 1):
  for kol2 in range(kol1 + 1, ile_kolumn + 1):
    if podaj(Li, 'k', kol1) == podaj(Li, 'k', kol2):
      print(f'Znaleziono identyczne kolumny {kol1} i {kol2}:\n',
            podaj(Li, 'k', kol1), '\noraz\n', podaj(Li, 'k', kol2))

print()

# Czy istnieją dwa identyczne wiersze?
for wie1 in range(1, ile_wierszy + 1):
  for wie2 in range(wie1 + 1, ile_wierszy + 1):
    if podaj(Li, 'w', wie1) == podaj(Li, 'w', wie2):
      print(f'Znaleziono identyczne wiersze {wie1} i {wie2}:\n',
            podaj(Li, 'w', wie1), '\noraz\n', podaj(Li, 'w', wie2))

print()

"""
Czy istnieją dwie kolumny składające się z tych samych znaków i 
takiej samej liczby wystąpień każdego znaku, 
bez zachowania zgodności na odpowiednich pozycjach (nie mogą być identyczne)?
"""
for kol1 in range(1, ile_kolumn + 1):
  for kol2 in range(kol1 + 1, ile_kolumn + 1):
    if dwie_podobne(podaj(Li, 'k', kol1), podaj(Li, 'k', kol2)):
      print(f'Znaleziono dwie podobne (nie identyczne) kolumny {kol1} i {kol2}')
      print(podaj(Li, 'k', kol1), podaj(Li, 'k', kol2), sep='\n')
