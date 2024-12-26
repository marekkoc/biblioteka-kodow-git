def dzielnikiWlasciwe(n: int):
  for dzielnik in range(1, n):
    if n % dzielnik == 0:
      yield dzielnik

def szukajDoskonale(do=20000):
  for i in range(2, do + 1):
    dzielniki = list(dzielnikiWlasciwe(i))
    if i == sum(dzielniki):
      yield i

# doskonałe można poszukać, albo ustawić ręcznie, gdyż jest ich tylko kilka w podanym zakresie:
# doskonale = list(szukajDoskonale()) # wyszukuję
doskonale = [6, 28, 496, 8128]  # ustawiam ręcznie, bo wiemy jakie to liczby
print('Doskonałe:', doskonale)

def zaprzyjaznione(od=2, do=20000):
  # obliczę sobie sumy dzielników wszystkich dla kolejnych liczb
  sumy = dict()
  for liczba in range(2, do + 1):
    if liczba in doskonale: continue
    sumy[liczba] = sum(dzielnikiWlasciwe(liczba))

  for n1, sn1 in sumy.items():
    for n2, sn2 in sumy.items():
      if n1 == sn2 and sn1 == n2:
        print('Zaprzyjaźniona para:', (n1, n2), 'Sumy ich dzielników:',
              (sn1, sn2))

zaprzyjaznione()
