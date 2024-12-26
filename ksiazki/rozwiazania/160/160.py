# ładuję domeny
import operator

domeny = dict()  # { domena : nazwa }
with open('160_domeny_krajowe.txt', 'r', encoding='utf-8') as f:
  for ln in f:
    domena, strona = ln.strip().split('\t')
    domeny[domena] = strona

# ładuję strony
stronyProt = dict()  # { strona : [protokoły] }
protStrony = dict()  # { protokół : [strony] }
with open('160_strony.txt', 'r', encoding='utf-8') as f:
  for ln in f:
    strona, prot = ln.strip().split(' ')
    stronyProt.setdefault(strona, [])
    protStrony.setdefault(prot, [])

    stronyProt[strona].append(prot)
    protStrony[prot].append(strona)

# Ile jest stron w domenie .pl? Podaj je z podziałem na oba protokoły.

s1 = set(filter(lambda e: e[-3::] == '.pl', protStrony['http']))
s2 = set(filter(lambda e: e[-3::] == '.pl', protStrony['https']))

print('Stron w domenie .pl = ', end='')
print(len(s1.union(s2)))

print('Protokół http, stron .pl = ', end='')
print(len(s1), s1, sep='\n')
print()

print('Protokół https, stron .pl = ', end='')
print(len(s2), s2, sep='\n')

# Zwróć uwagę, że istnieją strony równocześnie w protokołach http i https
print()
print(
  f'Strony, które mają swoje wersje w obu protokołach {s1.intersection(s2)}')
print()

# Oblicz, ile jest stron w każdej domenie, i wymień wraz z nazwą
# kraju/regionu te domeny, które pod kątem liczby stron osiągnęły
# pierwszą, drugą i trzecią pozycję. Uwaga! Jeżeli adres strony dostępny
# jest w domenie dla dwóch protokołów, licz ją jako jedną stronę.
zlicz_domeny = dict()  # { domena : [lista_stron] }
for strona in stronyProt.keys():
  zlicz_domeny.setdefault(strona[-3::], set())
  zlicz_domeny[strona[-3::]].add(strona)

def filtr(item):
  return len(item[1])

zlicz_domeny = dict(sorted(zlicz_domeny.items(), key=filtr, reverse=True))
s = set()
for domena, ile in zlicz_domeny.items():
  s.add(len(ile))
  if (len(s) >= 4): break
  print(domena, domeny[domena], ':', len(ile), 'stron.')
print()

# Ile jest stron obsługiwanych przez protokół HTTP, a ile przez HTTPS?
for prot, strona in protStrony.items():
  print(prot, len(strona))
print()

# Ile jest wszystkich stron?
print(len(stronyProt.keys()))
