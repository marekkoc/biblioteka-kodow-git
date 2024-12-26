m1 = [[5, 9, -1], [7, 4, 0], [-3, 5, 2]]
m2 = [[4, 8, 2], [11, -2, 0], [3, 5, 3]]
m3 = [[2, 4, 9, 4], [3, 0, 2, 2], [7, 3, 1, 8], [1, 2, 3, 4], [9, 6, 3, 1]]

# niepotrzebne dla algorytmu, tylko dla wyświetlania.
colors = {'reset': '\033[0m', 'blade': '\033[107m', 'dark': '\033[7m',
          'red': '\033[91m', 'green': '\033[92m', 'yellow': '\033[93m',
          'blue': '\033[94m', 'magenta': '\033[95m', 'bgred': '\033[101m',
          'bggreen': '\033[102m', 'bgyellow': '\033[103m'}

def pokaz(macierz, color='blue'):
  import time
  time.sleep(0.1)
  print(colors[color], end='')
  for l in macierz:
    print('|', *l, '|', sep='\t')
    time.sleep(0.1)
  print(colors['reset'])

def mnozenie(a, b):
  if isinstance(a, list) and isinstance(b, list):
    print('Mnożenie macierzy:')
    pokaz(a, 'blue')
    print('*')
    pokaz(b, 'red')
    print('=')
    if len(a[0]) != len(b):
      print('Błąd. Przy mnożeniu macierzy A*B ilość kolumn macierzy '
            'A musi być równa ilości wierszy macierzy B.')
      return None
    transb = [*zip(*m2)]
    wynik = []
    for wiersz in a:
      obliczone = []
      for transWiersz in transb:
        obliczone.append(
          sum([a * b for a, b in list(zip(wiersz, transWiersz))]))
      wynik.append(obliczone)
    pokaz(wynik, 'green')
    return wynik
  elif isinstance(a, list) and isinstance(b, int):  # macierz razy liczba
    mnozenie(b, a)
  elif isinstance(a, int) and isinstance(b, list):
    print('Mnożenie liczby i macierzy:')
    wynik = []
    print(colors['red'], a, colors['reset'])
    print('*')
    pokaz(b, 'blue')
    print('=')
    for poz in range(0, len(b)):
      wynik.append(list(map(lambda e: a * e, b[poz])))
    pokaz(wynik, 'green')
    return wynik

# należy wymnożyć m1 * m2 oraz m3 * 7

w1 = mnozenie(m1, m2)
w2 = mnozenie(7, m3)
print(w1, w2)
