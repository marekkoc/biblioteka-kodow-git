def Bin2Dec(bin: str):
  wynik = 0
  pot = 0
  for i in bin[::-1]:
    wynik += (ord(i) - 48) * 2 ** pot  # ord(i)-48 zamienia '0' na 0, '1' na 1
    pot += 1
  return wynik

print(Bin2Dec('11110'))  # 30
print(Bin2Dec('011110'))  # 30
print(Bin2Dec('0'))  # 0

def Dec2Bin(i: int):
  if i == 0: return '0'
  wynik = ''
  while i > 0:
    r = i % 2
    i //= 2
    wynik = chr(r + 48) + wynik  # chr(r+48) zamienia r=0 na '0', r=1 na '1'
  return wynik

print(Dec2Bin(30))  # '11110'
print(Dec2Bin(7))  # '111'
print(Dec2Bin(12))  # '1100'
print(Dec2Bin(0))  # '0'

# uniwersalna funkcja zamienia liczby w postaci 'ff' na dziesiętne 255 itp.
def Any2Dec(n: str, podstawa: int = 2):
  alfabetCyfr = '0123456789abcdef'  # cyfry systemów od binarnego po szesnastkowy
  wynik = 0
  pot = 0
  for cyfra in n[::-1]:
    wynik += alfabetCyfr.find(cyfra) * podstawa ** pot
    pot += 1
  return wynik

print(Any2Dec('11110', 2))  # bin-> 30
print(Any2Dec('77', 8))  # oct-> 63
print(Any2Dec('c8', 16))  # hex-> 200
print(Any2Dec('44', 5))  # piątkowy -> 24

# uniwersalna funkcja zamieniająca liczbę dziesiętną na postać w innym systemie (jako str)
def Dec2Any(n: int, podstawa: int = 2):
  if n == 0: return '0'  # zero to '0' w każdym systemie
  alfabetCyfr = '0123456789abcdef'  # cyfry systemów od binarnego po szesnastkowy
  wynik = ''
  while n > 0:
    r = n % podstawa
    wynik = alfabetCyfr[r] + wynik
    n //= podstawa
  return wynik

print(Dec2Any(200, 16))
print(Dec2Any(63, 8))
print(Dec2Any(30, 2))
print(Dec2Any(24, 5))
# zero to nawet w sys. dziewiątkowym wygląda tak samo...
print(Dec2Any(0, 9))
