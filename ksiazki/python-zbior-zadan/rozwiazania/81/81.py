T = input('Podaj tekst=')
# T = 'dfgnqeiut98tna1223v0w3r123334asdsh' # odkomentuj, by sprawdzić przykład z zadania

# 1 sposób (wyrażenia regularne)
import re

kandydaci = [[len(x), x] for x in list(
  filter(lambda x: len(x) > 0, re.findall('0*1*2*3*4*5*6*7*8*9*', T)))]
kandydaci.sort(reverse=True)
if (len(kandydaci)):
  print(kandydaci[0][1], 'o największej długości', kandydaci[0][0])

# 2 sposób (prostymi środkami)
cyfry = '0123456789'
poczatek = 0
dlugosc = 0
maxdl = 1
maxpocz = 0
for i in range(0, len(T)):
  znak = T[i]
  cyfra = True
  if znak not in cyfry:
    cyfra = False
  else:
    cyfra = True
  if cyfra and dlugosc == 0:
    poczatek = i
    dlugosc = 1
  elif cyfra and dlugosc > 0:
    if ord(T[i - 1]) - 48 <= ord(T[i]) - 48:
      dlugosc += 1
      if maxdl < dlugosc:
        maxdl = dlugosc
        maxpocz = poczatek
    else:
      poczatek = i
      dlugosc = 1
  else:
    dlugosc = 0
    poczatek = i
print(T[maxpocz:maxpocz + maxdl], 'o największej długości', maxdl)
