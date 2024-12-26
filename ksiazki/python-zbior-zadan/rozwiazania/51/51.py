a = int(input('Podaj a='))
b = int(input('Podaj b='))

# sposób 1
def connect(a: int, b: int):
  return float(str(a) + '.' + str(min(abs(b), 100000)))

print(f'Dla {a} i {b}=', connect(a, b))

# sposób 2 bez sztuczek z zamianą na napis
def connect2(a: int, b: int):
  ten = 10
  b = min(abs(b), 100000)
  cyfry = []
  while b / 10 > 0:
    cyfry.append(b % 10)
    b //= 10
    ten *= 10
  # enumerate pozwala liczyć kroki pętli (i = 0, 1, 2, ...)
  for i, poz in enumerate(range(len(cyfry) - 1, -1, -1)):
    cyfry[poz] /= (10 ** (i + 1))
  if (a >= 0):
    return a + sum(cyfry)
  return -(-a + sum(cyfry))

print(f'Dla {a} i {b}=', connect2(a, b))
