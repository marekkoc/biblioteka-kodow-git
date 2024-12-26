import re

c = 'xfac8*1101011*1110100xc8x32xff*1010o7311o1212xabcd*101*1*0x1o0xd*11111'

liczby = list(filter(lambda e: e != '', re.split(r'[x\\*o]', c)))
system = list(filter(lambda e: e != '', re.split(r'[^x\\*o]+', c)))

def znakNaSystem(znak):
  if znak == 'x':
    return 16
  elif znak == '*':
    return 2
  elif znak == 'o':
    return 8
  else:
    return 10

system = list(map(znakNaSystem, system))

# pięknie podzielone, liczby i ich system liczbowy
print(liczby)
print(system)

# sposób 1 (z gotowymi konwersjami)
for poz in range(0, len(liczby)):
  print(liczby[poz], '=>', int(liczby[poz], system[poz]))

# sposób 2 (bez konwersji int(str, baza systemu)
def str2dec(s: str, podstawa: int):
  cyfrySystemu = '0123456789abcdef'
  dec = 0
  potega = len(s) - 1
  for cyfra in s:
    vpoz = cyfrySystemu.find(cyfra)
    dec += vpoz * podstawa ** potega
    potega -= 1
  return dec

print('')
for poz in range(0, len(liczby)):
  print(liczby[poz], '=>', str2dec(liczby[poz], system[poz]))
