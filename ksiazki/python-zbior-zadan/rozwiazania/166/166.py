# dwuwymiarowa lista list z napisami (wiersze/kolumny odpowiadają plikom .csv)
Teryt = []

with open('166_teryt.csv', 'r', encoding='utf-8') as f:
  for ln in f:
    Teryt.append([])
    wynik = ln.strip().split(';')
    Teryt[-1].extend(wynik)

wojewodztwa = list(filter(lambda L: L[1] == '' and L[2] == '', Teryt))
ilosc = len(wojewodztwa)
print('Liczba województw: ', ilosc)
for w in wojewodztwa:
  print('\t', w[4], w[0])

powiaty = list(filter(lambda L: L[2] == '' and L[5] == 'powiat', Teryt))
ilosc = len(powiaty)
print('Liczba powiatów:', ilosc)

gmiwm = list(filter(
  lambda L: L[5] in ['gmina wiejska', 'gmina miejska', 'gmina miejsko-wiejska'],
  Teryt))
ilosc = len(gmiwm)
# nie uwzględniam: gmina miejsca miasto stołeczne!
print('Liczba gmin wiejskich, miejskich i wiejsko-miejskich', ilosc)

Miejscowosci = []
with open('166_miejscowosci.csv', 'r', encoding='utf-8') as f:
  for ln in f:
    Miejscowosci.append([])
    wynik = ln.strip().split(';')
    Miejscowosci[-1].extend(wynik)

wmrag = list(filter(lambda L: L[0] == '28' and L[1] == '10', Miejscowosci))
ilosc = len(wmrag)
print('Liczba miejscowości w powiecie mrągowskim:', ilosc)

piecki = list(
  filter(lambda L: L[3].find('piecki') >= 0 or L[3].find('Piecki') >= 0,
         Miejscowosci))
ilosc = len(piecki)
print('Liczba miejscowości z podciągiem [piecki] lub [Piecki]:', ilosc)
