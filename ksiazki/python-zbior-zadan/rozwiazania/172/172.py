import operator
import re

class Obiekt:
  def __init__(self, wiersz: str):
    self.dane = wiersz

  def __eq__(self, inny):
    i1, s1 = self.info()
    i2, s2 = inny.info()
    return s1 == s2 and i1 == i2

  def info(self):
    '''
    :return: (suma cyfr, ilość cyfr)
    '''
    ile = 0
    suma = 0
    for z in self.dane:
      if z in '0123456789':
        ile += 1
        suma += int(z)
    return (ile, suma)

wiersze = []
with open('172_dane_znaki_litery.txt', 'r', encoding='utf-8') as f:
  wiersze = [ln.strip() for ln in f]

print(f'Ile jest podciągów w pierwszym wierszu przynajmniej '
      f'pięcioelementowych, nie dłuższych niż dziesięcioelementowych, '
      f'które kończą się i zaczynają cyfrą? ', end='')
ilosci = dict()  # { 'ciąg': ilość }
for dl in range(3, 9):
  txt = wiersze[0]
  while txt != '':
    wynik = re.search('[0-9].{' + str(dl) + '}[0-9]', txt)
    if wynik is None: break
    ilosci.setdefault(wynik.group(), 0)
    ilosci[wynik.group()] += 1
    txt = txt[wynik.span()[0] + 1:]

print(sum(ilosci.values()))
print('Ciągi w pierwszym wierszu, które się powtarzają:', end=' ')
powtarzane = dict(filter(lambda i: i[1] >= 2, ilosci.items()))
print(*powtarzane.keys())

print('Podciągi z pierwszego wiersza powtarzające się w pozostałym tekście:')
ilosci = dict(sorted(ilosci.items(), key=operator.itemgetter(0)))
wszystko = ''.join(wiersze[1:])
for podciag, ile in ilosci.items():
  if wszystko.find(podciag) >= 0: print(podciag)

obiekty = [Obiekt(o) for o in wiersze]
rowne = []
for poz in range(0, len(obiekty)):
  if poz == 2: continue  # nie porównuję samego ze sobą
  if obiekty[poz] == obiekty[2]:
    rowne.append(obiekty[poz].dane)
print(f'Obiektów równych obiektowi trzeciemu '
      f'(pozycja 2 na liście) = {len(rowne)}.')
print(rowne)
