znaki = []
for i in range(5):
  znak = ''
  while len(znak) != 1 or znak not in '0123456789':
    znak = input('Podaj znak: ')
  znaki.append(znak)

# sposób 1 (matematyczny)
a = 0
b = 0
# i to krok pętli licząc od 0, c to element ze znaki
for i, c in enumerate(znaki):
  b += int(
    c) * 10 ** i  # cyfra * 10 do potęgi i (jedności, dziesiątki, setki...)
  a += int(c) * 10 ** (
      len(znaki) - i - 1)  # podobnie, ale (dz.tyś., tyś, setki...)
print('Liczby', a, b)
print('Suma', a + b)

# sposób 2 (z konwersją napisu na liczbę)
a = int(''.join(znaki))
b = int(''.join(reversed(znaki)))
print('Liczby', a, b)
print('Suma', a + b)
