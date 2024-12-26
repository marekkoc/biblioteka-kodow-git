# sposób 1
a = b = c = -1
while (a < 0 or b < 0 or c < 0):
  a = int(input('Podaj liczbę a: '))
  b = int(input('Podaj liczbę b: '))
  c = int(input('Podaj liczbę c: '))
# szukam największej
if a > b:
  maks = a
else:
  maks = b
if maks < c:
  maks = c
# w tym miejscu maks jest największą z liczb...
suma = a + b + c - maks  # a to jest suma dwóch pozostałych
while maks:
  print(suma, end=' ')
  maks -= 1
print()

# sposób 2
a = b = c = -1
while (a < 0 or b < 0 or c < 0):
  a, b, c = [int(x) for x in input(
    'Podaj 3 liczby rozdzielone spacją, to jest = a b c: ').split()]
suma = a + b + c - max(a, b, c)
for i in range(max(a, b, c)):
  print(suma, end=' ')
