from random import randint

def generatorImienia():
  ileSylab = randint(1, 5)
  srodek = 'eo'
  koniec = 'zwsdcrftgbhnjmklp'
  poczatek = 'srjcg'
  samo = randint(0, 1)
  gen = ''
  for i in range(ileSylab):
    if ileSylab % 2 == 0:  # parzysta ilość sylab
      gen += poczatek[randint(0, len(poczatek) - 1)] + srodek[samo] + koniec[
        randint(0, len(koniec) - 1)]
    else:
      gen += poczatek[randint(0, len(poczatek) - 1)] + srodek[samo] + koniec[
        randint(0, len(koniec) - 1)]
      samo = (samo + 1) % 2
  return gen[0].upper() + gen[1:]

for i in range(15):
  print(generatorImienia(), end=', ')
