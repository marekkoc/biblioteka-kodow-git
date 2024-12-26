dni = [1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0,
       0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0,
       0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0,
       1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1,
       1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1,
       1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0,
       1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0,
       1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0,
       1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1,
       0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0,
       0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0,
       1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1,
       1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0,
       0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0,
       0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0,
       0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1,
       1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1,
       1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0,
       0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1]

# a)
print(dni.count(1), ' - tyle dni Kasia odnosiła sukcesy dietetyczne.')
# Takie rozwiązanie było zbyt łatwe. Policzmy to samodzielnie!
ileSukcesow = 0
for co in dni:
  if co == 1:
    ileSukcesow += 1
print(ileSukcesow, ' - tyle dni Kasia odnosiła sukcesy dietetyczne.')

# b) Sposób 1. Tak. Korzystam z wyrażeń regularnych.
import re

for x in list(re.finditer('0{5,}', ''.join([str(x) for x in dni]))):
  print('Dnia nr', x.start() + 1,
        'znaleziono ciąg porażek trwających dokładnie', len(x.group()), 'dni.')

# Powyższy kod wymaga wyjaśnienia.
# Sklejam wszystkie jedynki i zera w jeden wielki ciąg tekstowy.
''' ''.join([str(x) for x in dni]) '''
# Za pomocą wyrażenia regularnego szukam ciągów składających się z zer, których jest przynajmniej 5.
''' re.finditer('0{5,}', ... '''
# Funkcja re.findinter zwraca iterowalny kontener, który zamieniam sobie na listę. Zawiera ona specjalne obiekty
# z wszystkimi znaleziskami. W pętli wstawiam je do x. Następnie tworze rapot:
''' print('Dnia nr',x.start()+1,'znaleziono ciąg porażek trwających dokładnie',len(x.group()),'dni.') '''
# gdzie x.start() zawiera pozycję znalezionego podciągu (licząc od 0). x.group() to znaleziony podciąg.

print()
# b) Sposób 2. Spróbujmy zrobić to jeszcze raz, nie korzystając z wyrażeń regularnych.
dl, od = 0, 1
for poz, znak in enumerate(dni):
  if znak == 0:
    dl += 1
  else:
    dl = 0
    od = poz + 1
  if dl >= 5:
    print('Dnia nr ', str(od + 1),
          ' znaleziono ciąg porażek trwających przynajmniej',
          len(dni[od:poz + 1]), 'dni.')
