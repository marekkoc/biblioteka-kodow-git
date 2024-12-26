# zwraca liczbę bitową bez zer na początku
def czyscZera(bit: str):
  return bit.lstrip('0')

# przy dodawaniu w słupkach przekazujemy cyfry 'dalej'
# 0+0 = 0, dalej nic nie przekazujemy
# 0+1 = 1 oraz 1+0 to 1, dalej nic nie przekazujemy
# 1+1 = 0 i 1 dalej
# 1+1+1 to 1 i 1 dalej
# zwraca krotkę
def dalej(i, dodaj):
  i += dodaj
  match i:
    case 0:
      return (0, 0)
    case 1:
      return (0, 1)
    case 2:
      return (1, 0)
    case 3:
      return (1, 1)
    case _:
      print('Jakiś dramatyczny błąd komiczny!')
      return (9, 9)

# dodawanie
def dodawanie(bit1: str, bit2: str):
  bit1 = czyscZera(bit1)
  bit2 = czyscZera(bit2)
  print(bit1, '+', bit2)
  suma = ''
  d = 0
  poz1 = len(bit1) - 1
  poz2 = len(bit2) - 1
  while poz1 >= 0 and poz2 >= 0:
    d, x = dalej(d, int(bit1[poz1]) + int(bit2[poz2]))
    suma = suma + str(x)
    if poz1 >= 0: poz1 -= 1
    if poz2 >= 0: poz2 -= 1
  while poz1 >= 0:
    d, x = dalej(d, int(bit1[poz1]))
    suma = str(x) + suma
    poz1 -= 1
  while poz2 >= 0:
    d, x = dalej(d, int(bit2[poz2]))
    suma = str(x) + suma
    poz2 -= 1
  while d > 0:
    d, x = dalej(d, 0)
    suma = str(x) + suma
  return suma

print('Suma=', dodawanie('101', '111'))
print('Suma=', dodawanie('101010111111', '1111111'))

def negacja(bit: str):
  return ''.join([str((int(znak) + 1) % 2) for znak in bit])

print('Negacja: 000111000', '->', negacja('000111000'))

def czyNegacja(bit1, bit2):
  return (bit1 == negacja(bit2))

print(czyNegacja('1110', '0001'))
print(czyNegacja('01110', '10001'))
print(czyNegacja('01110', '101'))

def wieksza(bit1, bit2):
  bit1 = czyscZera(bit1)
  bit2 = czyscZera(bit2)
  if len(bit1) > len(bit2):
    return bit1
  if len(bit2) > len(bit1):
    return bit2
  if bit1 == bit2: return bit1
  for poz in range(0, len(bit1)):
    if bit1[poz] > bit2[poz]: return bit1
    if bit2[poz] > bit1[poz]: return bit2

print('Większa: ', wieksza('101', '111'))
print('Większa: ', wieksza('1000', '111'))
print('Większa: ', wieksza('11', '11'))
print('Większa: ', wieksza('11', '11'))
