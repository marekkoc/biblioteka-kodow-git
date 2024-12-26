linia = ''
linie = []
# with open('167_dane_kontrolne.txt','r',encoding='utf-8') as f:
with open('167_dane.txt', 'r', encoding='utf-8') as f:
  for ln in f:
    linia += ln.strip()
    linie.append(ln.strip())

import re

ile = 0
pomoc = linia
while pomoc != '':
  wynik = re.search('R.(X|F)', pomoc)
  if wynik:
    # print(wynik[0]) # odkomentyj by je zobaczyć
    od, do = wynik.span()
    ile += 1
  pomoc = pomoc[od + 1:]
print('Podciągów R*X lub R*F znaleziono:', ile)

ile = 0
for ln in linie:
  if re.match('^[^EZ]*X[^EZ]*$', ln):
    # print(ln) # odkomentyj by je zobaczyć
    ile += 1
print('Wierszy bez E i Z, które zawierają X, jest ', ile)

ile = 0
wzorzec = ''
for znak in range(65, 91):
  wzorzec += chr(znak) + '{0,1}'
# print(wzorzec)  # odkomentuj, by zobaczyć wzorzec dla wyrażeń regularnych

for ln in linie:
  while ln != '' and len(ln) >= 5:
    wynik = re.search(wzorzec, ln)
    od, do = wynik.span()
    if len(wynik.group()) >= 5:
      # print(wynik.group())  # odkomentyj by je zobaczyć
      ile += 1
      break
    ln = ln[od + 1:]

print(f'Wierszy zawierających podciąg przynajmniej 5-u rosnących znaków:', ile)
