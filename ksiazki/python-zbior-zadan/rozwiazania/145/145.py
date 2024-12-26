import operator
import re

slowa = dict()
wiersze = []
with open('145_opowiadanie.txt', 'r', encoding='utf-8') as f:
  for ln in f:
    # wersja, gdzie wielkość liter ma znaczenie
    wiersze.append(ln)
    # wersja, gdzie wielkość liter nie ma znaczenia
    # odkomentuj poniższe polecenie, zakomentuj wcześniejsze
    # wiersze.append(ln.lower())

wiersze = ''.join(wiersze)

for slowo in re.split(r'[\n \.,!\?;:\-\(\)0-9]+', wiersze):
  if len(slowo):
    slowa.setdefault(slowo, 0)
    slowa[slowo] += 1

slowa = dict(sorted(slowa.items(), key=operator.itemgetter(1), reverse=True))
for slowo, ile in slowa.items():
  print(f'[{slowo}] => {ile}')

print('Przynajmniej dwuznakowe słowo, które wystąpiło największą ilość razy:')
for slowo, ile in slowa.items():
  if len(slowo) >= 2:
    print(f'[{slowo}] => {ile}')
    break
print(f'Słów bez powtórzeń jest = ', len(slowa))
print(f'Wszystkich słów z powtórzeniami jest = ', sum(slowa.values()))
