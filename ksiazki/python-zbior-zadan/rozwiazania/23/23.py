L = []
# sposób 1

while len(L) < 10:
  x = float(input('Podaj liczbę: '))
  jest = False
  for i in L:
    if x == i:
      jest = True
      break
  if not jest:
    L.append(x)
  print('Ilość elementów =', len(L))
print(L, 'ilość=', len(L))

# sposób 2
L.clear()
while len(L) < 10:
  x = float(input('Podaj liczbę: '))
  if x not in L:
    L.append(x)
  print('Ilość elementów =', len(L))
print(L, 'ilość=', len(L))

# Wspólne dla obu sposobów użycie zbioru.
L = set()  # Pusty zbiór. Zbiory nie zawierają powtórzeń elementów.
while len(L) < 10:
  x = float(input('Podaj liczbę dla zbioru: '))
  L.add(x)  # Dodaję bez lęku. I tak zbiór nie pozwoli na duplikat.
  print('Ilość elementów =', len(L))
print(L, 'ilość=', len(L))
