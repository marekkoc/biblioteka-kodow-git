T = input('Podaj tekst=')

# sposób 1 (prostymi środkami)
dl = 0
for poz, znak in enumerate(T):
  if znak in '0123456789':
    dl += 1
  elif (dl > 0):
    print(T[poz - dl:poz])
    dl = 0

# sposób 2 (wyrażenia regularne)
import re

print(*list(map(lambda x: int(x), re.findall('[0-9]+', T))), sep='\n')
