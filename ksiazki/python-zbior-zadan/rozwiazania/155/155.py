from random import randint
from time import sleep

class Ork:
  # Poniższe literki posłużą do wygenerowania
  # imion brzmiących ewidedntnie jak imiona orków.
  sp = 'ggggggggrrrrrrrrrrrrhhhhhhhhkkssssbbzz'
  sa = 'oooooouuuuuuyyyaaee'

  def __init__(self):
    self.imie = ''
    self.zdrowie = self.zdrowie_max = randint(200, 300)
    self.sila = randint(5, 25)
    self.pancerz = randint(0, 4)
    print(f'Z brudu ziemi i złej woli Czerwonego Oka zrodził się ork: ', end='')
    for i in range(randint(2, 3), 0, -1):
      self.imie += Ork.sp[randint(0, len(Ork.sp) - 1)]
      if not randint(0, 2): self.imie += Ork.sp[
        randint(0, len(Ork.sp) - 1)]
      self.imie += Ork.sa[randint(0, len(Ork.sa) - 1)]
    self.imie = self.imie.capitalize()
    print(
      f'{self.imie}. [siła={self.sila} zdrowie={self.zdrowie_max} pancerz={self.pancerz}]')
    sleep(1)

  def zaprezentuj(self):
    print(f'Ork {self.imie} posiada: siłę wynoszącą {self.sila},'
          f' zdrowie w wysokości {self.zdrowie_max}'
          f' pancerz o wartości {self.pancerz}.\n')

  def __del__(self):
    print(f'Zwłoki orka {self.imie} magicznie wyparowały...')

  def cios(self, przeciwnik):
    komunikat = ''
    if randint(0, 1):
      opis = ['trafia', 'tnie po głowie', 'przebija nogę', 'rozcina brzuch',
              'miażdży ramię', 'rani pysk', 'okalecza ucho', 'wydłubuje oko',
              'rozcina skórę']
      komunikat += (f'{self.imie} {opis[randint(0, len(opis) - 1)]} '
                    f'{przeciwnik.imie}!')
      przeciwnik.zdrowie -= max(0, self.sila - przeciwnik.pancerz)
      komunikat += (f' ({przeciwnik.imie}={przeciwnik.zdrowie} '
                    f'zdrowia pozostało)\n')
    else:
      # komunikat += f'{self.imie} nie trafia w {przeciwnik.imie} ...\n'
      pass  # Możesz odkomentować wcześniejszą linię,
      # by obserwować nietrafione ciosy.
    return komunikat

# walka dwóch orków
def Walka(ork1: Ork, ork2: Ork):
  print(f'\n\n>>> {ork1.imie.upper()} VS {ork2.imie.upper()} <<<\n\n')
  ork1.zaprezentuj()
  ork2.zaprezentuj()
  komunikat = ''
  # losujemy, kto zada pierwszy cios
  orki = []
  if randint(0, 1):
    orki = [ork1, ork2]
  else:
    orki = [ork2, ork1]

  ten, tego = 0, 1
  while True:
    print(f'{orki[ten].cios(orki[tego])}', end='')
    if orki[tego].zdrowie <= 0:
      komunikat += (f'{orki[tego].imie} przegrywa i ginie! Zwycięski'
                    f' {orki[ten].imie} unosi łapę w geście zwycięstwa. '
                    f'Z jego pyska wydobywa się gromkie: Arrrggghhhhh!!!\n')
      komunikat += f'{orki[ten].imie} zyskuje siłę i zrowie (+1/+10).\n'
      orki[ten].sila += 1
      orki[ten].zdrowie_max += 10
      orki[ten].zdrowie = orki[ten].zdrowie_max
    # zamiana ten/tego (teraz drugi będzie bił)
    ten = (ten + 1) % len(orki)
    tego = (tego + 1) % len(orki)
    sleep(0.1)  # trochę przerwy dla zauważenia komunikatów
    if orki[ten].zdrowie <= 0 or orki[tego].zdrowie <= 0: break
  return komunikat

'''
Wymyślone zasady walk:
// SERIA 1: 12 orków, 6 par walczy, przeżywa 6 orków.
// SERIA 2: walczą ork 1-2 i 3-4 i 5-6, przeżywa 3 orków.
// SERIA 3: walczą 1-2, zwycięski ork walczy w ostatniej walce z orkiem 3.
// Dla zachowania szans, ork 3, który nie walczył, zyskuje bonus identyczny
// jak zwycięzca pary 1-2
'''

HORDA = []  # :)
for i in range(12): HORDA.append(Ork())
# SERIA 1, 6 par
for n in range(0, 12, 2):
  print(Walka(HORDA[n], HORDA[n + 1]))

# usuwam martwe orki z areny
HORDA = list(filter(lambda ork: ork.zdrowie > 0, HORDA))

# SERIA 2, 3 pary
for n in range(0, 6, 2):
  print(Walka(HORDA[n], HORDA[n + 1]))

# usuwam martwe orki z areny
HORDA = list(filter(lambda ork: ork.zdrowie > 0, HORDA))

# SERIA 3
Walka(HORDA[0], HORDA[1])
# bonus dla orka z HORDA[2]
HORDA[2].zdrowie += 10
HORDA[2].zdrowie_max += 10
HORDA[2].sila += 1

# usuwam martwe orki z areny (Seria 3)
HORDA = list(filter(lambda ork: ork.zdrowie > 0, HORDA))

# OSTATNIA FINAŁOWA WALKA
print('\n\n>>> PRZED NAMI FINAŁ!! <<<\n')
Walka(HORDA[0], HORDA[1])

# usuwam przegranego w finale
HORDA = list(filter(lambda ork: ork.zdrowie > 0, HORDA))

print(f'\n\nOrk --- {HORDA[0].imie} --- ZWYCIĘŻA W WIELKIM STYLU! '
      f'Garbage collection już czeka...')
HORDA[0].zaprezentuj()
print('KONIEC')
