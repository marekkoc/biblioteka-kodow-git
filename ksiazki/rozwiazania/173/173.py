from enum import Enum

class Paliwo(Enum):
  GAZ = 1
  ROPA = 2
  BENZYNA = 3

class Tankowanie:
  def __init__(self, data: str, litr: float, cena: float):
    self.data = data
    self.litry = litr
    self.cena = cena

class Samochod:
  def __init__(self, nr: str, mod: str, rok_p: str, data_k: str,
               licz_kup: float, paliwo: Paliwo):
    self.nr_rej = nr
    self.model = mod
    self.rok_prod = rok_p
    self.data_kupna = data_k
    self.licznik_kupno = licz_kup
    self.rodzaj = paliwo

    self.licznik = dict()  # { data : licznik } stan licznika na koniec dnia
    self.tankowania = []

  def tankuj(self, data: str, litr: float, zl: float):
    self.tankowania.append(Tankowanie(data, litr, zl))

  def wprowadzLicznik(self, data: str, stan: float):
    self.licznik[data] = stan

  def rodzajPaliwa(self):
    match self.rodzaj:
      case Paliwo.GAZ:
        return 'gaz'
      case Paliwo.ROPA:
        return 'ropa'
      case Paliwo.BENZYNA:
        return 'benzyna'
      case _:
        return 'woda z cukrem pudrem!'  # :)

  def paliwoSuma(self, rok: str):
    return sum([t.litry for t in
                list(filter(lambda i: i.data[0:4] == rok, self.tankowania))])

  def paliwoKoszt(self, rok: str):
    return sum([t.cena for t in
                list(filter(lambda i: i.data[0:4] == rok, self.tankowania))])

  def ileKm(self, rok: str):
    '''
    Liczy km na podstawie danych z wpisów stanu licznika. Pierwszy wpis z roku
    kończy przejazd, zatem trzeba uwzględnić ostatni wpis wcześniejszego roku
    (albo stan początkowy licznika). Gdy pytam o rok, z którego wpisy
    nie istnieją, zwraca 0.
    '''
    ostatnie_km = 0.
    start = self.licznik_kupno
    ostatni_rok_wczesniej = list(
      filter(lambda i: i[0][0:4] == str(int(rok) - 1), self.licznik.items()))
    if len(ostatni_rok_wczesniej) and ostatni_rok_wczesniej[-1] != \
        list(self.licznik.items())[-1]:
      start = ostatni_rok_wczesniej[-1][1]
    ostatni = list(
      filter(lambda i: i[0][0:4] == rok, self.licznik.items()))
    if not len(ostatni):
      ostatnie_km = start
    else:
      ostatnie_km = ostatni[-1][1]
    return ostatnie_km - start

  def spalanie(self, rok: str):
    km = self.ileKm(rok)
    p = self.paliwoSuma(rok)
    if km > 0.:
      return p * (100. / km)
    return 0

# testy i przykładowe wykorzystanie:
FLOTA = dict()  # {nr_rejestracyjny_samochodu:Samochod}
FLOTA['1'] = Samochod('1', 'Fiat 126p', rok_p='1980',
                      data_k='1984-02-02', licz_kup=74000.0,
                      paliwo=Paliwo.BENZYNA)
FLOTA['1'].tankuj('1984-02-03', 25, 100)
FLOTA['1'].tankuj('1984-02-12', 20, 86)
FLOTA['1'].tankuj('1985-02-01', 44, 112)
FLOTA['1'].tankuj('1985-02-10', 44, 112)
FLOTA['1'].wprowadzLicznik('1984-12-23', 75020)
FLOTA['1'].wprowadzLicznik('1985-02-03', 75900)
FLOTA['1'].wprowadzLicznik('1985-02-04', 76100)
FLOTA['1'].wprowadzLicznik('1985-02-06', 77456)

print(f'Paliwo w roku 1984: {FLOTA['1'].paliwoSuma('1984')}')
print(f'Paliwo w roku 1985: {FLOTA['1'].paliwoSuma('1985')}')
print(f'Koszt za paliwo w roku 1984: '
      f'{FLOTA['1'].paliwoKoszt('1984')}')
print(f'Koszt za paliwo w roku 1985: '
      f'{FLOTA['1'].paliwoKoszt('1985')}')
print(f'Ile km w roku 1984: {FLOTA['1'].ileKm('1984')}')
print(f'Ile km w roku 1985: {FLOTA['1'].ileKm('1985')}')

print(f'Przybliżone spalanie na 100km w roku 1984: '
      f'{FLOTA['1'].spalanie('1984')}')
print(f'Przybliżone spalanie na 100km w roku 1985: '
      f'{FLOTA['1'].spalanie('1985')}')

print(f'Koszt za paliwo w roku 1986: '
      f'{FLOTA['1'].paliwoKoszt('1986')}')
print(f'Ile km w roku 1986: '
      f'{FLOTA['1'].ileKm('1986')}')
