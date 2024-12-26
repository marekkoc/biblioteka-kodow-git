from random import randint

def sgen(minL: int, maxL: int, dictionary: str):
  if not 0 < minL < maxL:
    print('Błąd założeń')
    return None
  dl = randint(minL, maxL)
  return ''.join([dictionary[randint(0, len(dictionary) - 1)] for x in range(dl)])

slowa = []
for n in range(25000):
  slowa.append(sgen(5, 10, 'qazwsxedcrfvtgby'))

# szukanie, algorytm szybszy, porównuje tylko napisy o tej samej długości
def ver1():
  for dl in range(5, 11):
    temp = list(filter(lambda s: len(s) == dl, slowa))
    for poz in range(0, len(temp)):
      for dalej in range(poz + 1, len(temp)):
        if temp[poz] == temp[dalej]:
          print('Powtórzyło się słowo', temp[poz])

# szukanie, algorytm prymitywny, sprawdza każdy wyraz z każdym
def ver2():
  for poz in range(0, len(slowa)):
    for dalej in range(poz + 1, len(slowa)):
      if slowa[poz] == slowa[dalej]:
        print('Powtórzyło się słowo', slowa[poz])

import time

start = time.time()
ver1()
koniec = time.time()
print('Czas działania : ', float(koniec) - float(start), 'sekund')
print()
print()

start = time.time()
ver2()
koniec = time.time()
print('Czas działania : ', float(koniec) - float(start), 'sekund')
