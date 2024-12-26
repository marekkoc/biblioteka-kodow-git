def bez0(b: str):
  '''Usuwam zera z początku napisu'''
  b = b.strip()
  b = b.lstrip('0')
  return b

def mojaKonwersja(b: str):
  if b == '0': return 0
  if b == '1': return 1
  print('My tutaj konwertujemy tylko bity.')
  return -1

def dalej(i: int, dodaj: int):
  i += dodaj
  if i == 0:
    return (i, '0')
  elif i == 1:
    i = 0
    return (i, '1')
  elif i == 2:
    i = 1
    return (i, '0')
  elif i == 3:
    i = 1
    return (i, '1')
  else:
    print('Jakiś dramat, źle dodajemy?')
    return (0, '!')

def dodaj(b1, b2):
  b1 = bez0(b1)
  b2 = bez0(b2)
  suma = ''
  d = 0
  s = 0
  poz1 = len(b1) - 1
  poz2 = len(b2) - 1
  while poz1 >= 0 and poz2 >= 0:
    d, bit = dalej(d, mojaKonwersja(b1[poz1]) + mojaKonwersja(b2[poz2]))
    suma = bit + suma
    if poz1 >= 0: poz1 -= 1
    if poz2 >= 0: poz2 -= 1
  while poz1 >= 0:
    d, bit = dalej(d, mojaKonwersja(b1[poz1]))
    suma = bit + suma
    poz1 -= 1
  while poz2 >= 0:
    d, bit = dalej(d, mojaKonwersja(b2[poz2]))
    suma = bit + suma
    poz2 -= 1
  while d:
    d, bit = dalej(d, 0)
    suma = bit + suma
  return suma

def binarne_mnozenie(b1: str, b2: str):
  # tylko dla informacji, co mnożę
  print(b1, '*', b2, end='')
  print('[', int(b1, 2), '*', int(b2, 2), ']', end=' = ')
  dododania = []
  for bit2 in b2[::-1]:
    dododania.append('')
    for bit1 in b1[::-1]:
      cyfra = mojaKonwersja(bit1) * mojaKonwersja(bit2)
      dododania[-1] = str(cyfra) + dododania[-1]
    if len(dododania) > 1:
      dododania[-1] += (len(dododania) - 1) * '0'
  while len(dododania) > 1:
    a = dododania.pop()
    b = dododania[-1]
    dododania[-1] = dodaj(a, b)
  return dododania[-1]

# testy
m1 = binarne_mnozenie('101', '111')
print(m1, int(m1, 2))
m2 = binarne_mnozenie('101111', '1')
print(m2, int(m2, 2))
m3 = binarne_mnozenie('10001011', '10001010111')
print(m3, int(m3, 2))
