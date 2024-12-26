class Kolejka:
  def __init__(self):
    self.kolejka = []  # niby kolejka, a lista
    self.ile = 0  # ile w kolejce
    self.ile_opuscilo = 0
    self.ile_dodano = 0
    self.maks = 0
    self.aktualny_maks = 0
    self.dane_maks_kategoria = []
    self.dane_maks_kategoria_aktualne = []

  def dodaj(self, kat: int):  # dodaj kategorię do kolejki
    self.kolejka.append(kat)
    self.ile += 1
    self.ile_dodano += 1
    print(
      f'{self.ile_dodano}. Dane kategorii {kat} dotarły na koniec kolejki ({self.ile}).')
    # testy opuszczania kolejki po dodaniu danych
    przed = self.ile
    self.zasady()
    # analiza procesu dodawania danych bez usuwania
    if przed == self.ile:
      self.maks += 1
      self.dane_maks_kategoria.append(kat)
    else:
      self.maks = 0
      self.dane_maks_kategoria.clear()
    if self.maks > self.aktualny_maks:
      self.aktualny_maks = self.maks
      self.dane_maks_kategoria_aktualne = self.dane_maks_kategoria.copy()

  def opuscRaz(self):
    if self.ile:
      print(f'\tDane kategorii {self.kolejka[0]} opuściły kolejkę.')
      self.kolejka.pop(0)
      self.ile -= 1
      self.ile_opuscilo += 1

  def opusc(self, kat: list):
    while self.ile > 0 and self.kolejka[0] in kat: self.opuscRaz()

  def zasady(self):
    kat = self.kolejka[-1]
    match kat:
      case 1:
        self.opusc([5])
      case 2:
        self.opusc([1])
      case 3:
        self.opusc([2])
      case default:  # 4 lub 5
        i = 0
        while True:
          i = self.ile
          self.opusc([3, 4])
          if i == self.ile: break

K = Kolejka()
info = ''
with open('180_kolejka.txt', 'r', encoding='utf-8') as f:
  for ln in f:
    K.dodaj(int(ln.strip()))
    if K.ile_dodano == 40:
      info = f'Przed dodaniem 41. danej kolejkę opuściło {K.ile_opuscilo} danych.'

print(
  f'{K.aktualny_maks} -> największa liczba dodanych danych z rzędu niewywołująca opuszczania kolejki.')
print(K.dane_maks_kategoria_aktualne)
print(info)
print(f'W kolejce zostało {K.ile}.')
print(K.kolejka)
