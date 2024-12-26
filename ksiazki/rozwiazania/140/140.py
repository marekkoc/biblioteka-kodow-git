red = "\033[91m"
green = "\033[92m"
reset = "\033[0m"

class Blob:
  zdrowie_max = 10000000
  zdrowie = 10000000
  regeneracja_zdrowie_max = 300000
  regeneracja_zdrowie_min = 57000
  # ile sekund upłynęło od ostatniego zranienia bloba ?
  czas_od_zranienia = 0
  czas_do_ataku = 45
  czas_od_ostatniego_ataku = 0
  obrazenia = 20000
  ile_atakow = 0

  @staticmethod
  def sekunda(g, z, i):
    if Blob.zdrowie <= 0:
      print('Blob nie żyje.')
      return
    Blob.czas_od_ostatniego_ataku += 1
    Blob.czas_od_zranienia += 1
    # regeneracja co sekundę, więc zawsze
    if Blob.czas_od_zranienia > 1:
      Blob.zdrowie += Blob.regeneracja_zdrowie_max
    else:
      Blob.zdrowie += Blob.regeneracja_zdrowie_min
    if Blob.zdrowie > Blob.zdrowie_max: Blob.zdrowie = Blob.zdrowie_max
    print(green, 'Blob się leczy do wartości = [', Blob.zdrowie, ']', reset,
          sep='')
    if Blob.czas_do_ataku == Blob.czas_od_ostatniego_ataku:
      # atak
      Blob.ile_atakow += 1
      procent_obrazen = Blob.zdrowie / Blob.zdrowie_max
      print(procent_obrazen, '%', sep='')
      obrazenia = int(Blob.obrazenia * procent_obrazen)
      print(red, '>>>> Blob wściekle atakuje z siłą', obrazenia, '! <<<<',
            reset)
      g.zdrowie -= obrazenia
      z.zdrowie -= obrazenia
      i.zdrowie -= obrazenia
      print(g.bohater, ' zdrowie=[', g.zdrowie, ']', sep='')
      print(z.bohater, ' zdrowie=[', z.zdrowie, ']', sep='')
      print(i.bohater, ' zdrowie=[', i.zdrowie, ']', sep='')
      Blob.czas_od_ostatniego_ataku = 0

class SuperHero:
  def __init__(self, imie, zdrowie, czas_do_ataku, czas_ooa, obrazenia,
               lag=False, co_ile_lag=5):
    self.bohater = imie
    self.zdrowie = zdrowie
    self.czas_do_ataku = czas_do_ataku
    self.czas_od_ostatniego_ataku = czas_ooa
    self.obrazenia = obrazenia
    # dla Ignoratora
    self.lag = lag
    self.co_ile_atakow_lag = co_ile_lag
    self.ile_atakow = 0
    self.komunikat = False

  def sekunda(self):
    if self.zdrowie <= 0:
      if not self.komunikat:
        print(red, '>>>>>>', self.bohater, 'nie żyje.', reset)
        self.komunikat = True
      return  # nie żyje, nie ma co analizować
    # żyje
    self.czas_od_ostatniego_ataku += 1
    if self.czas_do_ataku == self.czas_od_ostatniego_ataku:
      # atak
      self.ile_atakow += 1
      print(self.bohater, 'atakuje!')
      Blob.zdrowie -= self.obrazenia
      print('Zdrowie Bloba = [', Blob.zdrowie, ']', sep='')
      # zapis zranienia po ataku
      Blob.czas_od_zranienia = 0
      self.czas_od_ostatniego_ataku = 0
      # lag dla Zgniotka!
      if self.lag and (self.ile_atakow % self.co_ile_atakow_lag == 0):
        self.czas_do_ataku += 1
        self.obrazenia += 20000

gilgotek = SuperHero("Gilgotek", 50000, 30, 0, 500000)
zgniotek = SuperHero("Zgniotek", 25000, 1, 0, 250000, True, 5)
ignorator = SuperHero("Ignorator", 75000, 10, 0, 2000000)

with open('zdrowie.csv', 'w', encoding='utf-8') as f:
  czas = 0
  while True:
    czas += 1
    print('Upłynęło', czas, 'sekund walki.')
    Blob.sekunda(gilgotek, zgniotek, ignorator)
    gilgotek.sekunda()
    zgniotek.sekunda()
    ignorator.sekunda()
    f.writelines([str(Blob.zdrowie) + '\n'])
    if (Blob.zdrowie <= 0 or
        (
            gilgotek.zdrowie <= 0 and zgniotek.zdrowie <= 0 and ignorator.zdrowie <= 0)): break

if Blob.zdrowie < 0:
  print(red, '\n\n>>>>>> !!!!! Blob NIE ŻYJE !!!!!! <<<<<<', reset)
  print('Blob zginął w', czas, 'sekundzie walki. Uf!')
if gilgotek.zdrowie <= 0:
  print(red, gilgotek.bohater, ' nie żyje! Poświęcenie, które zapamiętamy.',
        reset, sep='')
if zgniotek.zdrowie <= 0:
  print(red, zgniotek.bohater, ' nie żyje! Poświęcenie, które zapamiętamy.',
        reset, sep='')
if ignorator.zdrowie <= 0:
  print(red, ignorator.bohater, ' nie żyje! Poświęcenie, które zapamiętamy.',
        reset, sep='')
