# kolorki do wyświetlania na konsoli
reset = "\033[0m"
kolory = ["\033[91m", "\033[92m", "\033[93m", "\033[94m", "\033[95m",
          "\033[101m", "\033[102m", "\033[103m"]

plecak = [[0] * 50].copy() * 50  # plecak 50x50
plecak = [x.copy() for x in plecak]
plecak_size = len(plecak) - 1
print(plecak)

class Zabawka:
  def __init__(self, nazwa: str, bok: int, grosze: int, ile: int,
               ile_start: int, kod_zabawki: int, kolor: str):
    self.nazwa = nazwa
    self.bok = bok
    self.grosze = grosze
    self.ile = ile
    self.ile_start = ile_start
    self.kod_zabawki = kod_zabawki
    self.kolor = kolor

  def cennosc(self):
    return self.grosze / self.bok

  def __str__(self):
    c = round(self.cennosc(), 2)
    return f'''
id={self.kolor}{self.kod_zabawki}{reset}:nazwa={self.nazwa}: rozmiar={self.bok}: wartość(gr)={self.grosze}:\
 cenność={c}: ilość_początkowa={self.ile_start}: ILOŚĆ POZOSTAŁA = {self.ile}'''

  def __lt__(self, other):  # operator < porównania zabawek
    return (self.cennosc() == other.cennosc() and self.bok >= other.bok) or (
        self.cennosc() < other.cennosc())

  # czy zabawka mieści się w plecaku, gdy jest zaczepiona w punkcie x;y ?
  def w_plecaku(self, x, y):
    if (y + self.bok - 1 > plecak_size) or (x - self.bok + 1 < 0):
      return False
    return True

  # czy zabawka wstawiona na pozycję x,y koliduje z czymś co już zajmuje plecak?
  def kolizja(self, x, y):
    for _x in range(x, x - self.bok, -1):
      for _y in range(y, y + self.bok):
        if plecak[_x][_y] != 0:
          return True;
    return False

sklep = []  # sklep z zabawkami

# przeliczam kwoty z pliku na złotówki (zl) i grosze (gr)
def grosze(kwota: str):
  zlpoz = kwota.find('zl')
  zl = 0
  gr = 0
  if (zlpoz != -1):
    zl = int(kwota[0:zlpoz])
    kwota = kwota[zlpoz + 2:]
  grpoz = kwota.find("gr")
  if (grpoz != -1):
    gr = int(kwota[0:grpoz])
  return (zl, gr)

# wgrywam dane sklepowe
def wgraj():
  temp = ''
  with open('131_zabawki.txt', 'r', encoding='utf-8') as f:
    f.readline()  # ignoruję wiersz z nazwami kolumn
    for ln in f:
      nazwa, bok, cena, ile = ln.split(';')
      bok = int(bok)
      ile = int(ile)
      zl, gr = grosze(cena)
      kod = len(sklep) + 1  # kod zabawki, nadaję z automatu
      kolor = kolory.pop()
      sklep.append(Zabawka(nazwa, bok, zl * 100 + gr, ile, ile, kod, kolor))
  print('Wgrano zabawki ze sklepu')

wgraj()
print(*sklep)  # zawartość sklepu

# Posortowane od najcenniejszych do najmniej cennych z uwzględnieniem
# wielkości w przypadku równej cenności.
sklep = sorted(sklep, reverse=True)
print(*sklep)  # zawartość sklepu, posortowana

def wkladanie(z: Zabawka):
  x = -1
  y = -1
  yplecak = plecak_size - z.bok + 1
  y = yplecak
  # wkładam od góry w dół (przy prawej krawędzi)
  for xplecak in range(z.bok - 1, plecak_size + 1):
    if not z.kolizja(xplecak, y):
      x = xplecak
    else:
      break
  if (x != -1):  # w lewo
    for yplecak in range(plecak_size - z.bok + 1, -1, -1):
      if not z.kolizja(x, yplecak):
        y = yplecak
      else:
        break
    # w dół
    for xplecak in range(z.bok - 1, plecak_size + 1):
      if z.w_plecaku(xplecak, y) and not z.kolizja(xplecak, y):
        x = xplecak
      else:
        break
    # mam x,y mogę włożyć tu przedmiot
    if z.w_plecaku(x, y):
      for xpoz in range(x, x - z.bok, -1):
        for ypoz in range(y, y + z.bok):
          plecak[xpoz][ypoz] = z.kolor + str(z.kod_zabawki) + reset
      return True
  return False

def pokaz_plecak():
  for w in plecak:
    for z in w:
      print(z, sep='', end='')
    print()

pokaz_plecak()  # plecak przed załadowaniem

def kradnij_zachlannie():
  for zabawka in sklep:
    while zabawka.ile > 0 and wkladanie(zabawka):
      zabawka.ile -= 1
      # usuń komentarz dla poniższego kodu, by odlągać wkładanie zabawek
      # pokaz_plecak(); print()

print('Zawartość sklepu')
print(*sklep)
kradnij_zachlannie()
pokaz_plecak()
print(*sklep)
