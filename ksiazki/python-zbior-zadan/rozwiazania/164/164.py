import sys
from random import randint

# W zmiennej globalnej *kodowanie* przechowam TAJNE przypisanie pozycji piksela
# dla znaku z alfabetu.
kodowanie = dict()  # { 'znak' : (wiersz, kolumna) }

def pozycjaNaWK(poz: int):
  """
  Zwraca krotkę (wiersz,kolumna) dla pozycji bitu w napisie. Liczymy pozycje
  od 1. Np. dla 23 to 1x23, a dla 29 to 2x4, dla 1 to 1x1 a dla 625 to 25x25.
  :param poz: pozycja w napisie kodującym obrazek 25x25
  :return: krotka (wiersz, kolumna)
  """
  return (int(poz / 25) + int(bool(poz % 25)), (poz % 25) if (poz % 25) else 25)

def WKnaPozycje(wk: tuple):
  """
  Zwraca pozycję w ciągu 625 bitów, która odpowiada pikselowi
  w obrazku na pozycji (wiersz, kolumna).
  """
  return (wk[0] - 1) * 25 + wk[1]

# Każdej literce alfabetu zostanie przypisana
# niepowtarzalna para (wiersz, kolumna).
def losowe_kody():
  alfabet = 'qwertyuiopasdfghjklzxcvbnm'
  kody = set()  # zbiór gwarantujący niepowtarzalność par (w,k):tuple
  while len(kody) < len(alfabet):
    kody.add(pozycjaNaWK(randint(1, 625)))
  iterator = iter(kody)
  for znak in alfabet:
    kodowanie[znak] = next(iterator)
  # pokaż co się wylosowało
  for znak, paraWK in kodowanie.items():
    print(znak, paraWK, ' => ', WKnaPozycje(paraWK))

class Kryptotron:
  @staticmethod
  def koduj(znak: str):
    bity = []  # 625 wartości bool
    pozycja = kodowanie[znak]
    # 1) losowy ciąg bitów
    while len(bity) < 625: bity.append(randint(0, 1))
    # 2) pozycja niepowtarzalna dla znaku: czarna
    bity[WKnaPozycje(pozycja) - 1] = 1
    # 3) pozycje pozostałych znaków: białe
    for z, wk in kodowanie.items():
      if z == znak: continue
      bity[WKnaPozycje(wk) - 1] = 0
    return bity

  @staticmethod
  def pokaz(sysstdout, znak, linia=True, enter=''):
    original_stdout = sys.stdout
    sys.stdout = sysstdout
    bity = Kryptotron.koduj(znak)
    poz = 1
    for e in bity:
      print(e, sep='', end='')
      poz += 1
      if not linia and poz % 25 == 1:
        print()
    print(enter, sep='', end='')
    sys.stdout = original_stdout

  @staticmethod
  def pokazSlowo(sysstdout, slowo: str):
    for z in slowo:
      Kryptotron.pokaz(sysstdout, z, enter='\n')

  @staticmethod
  def dekoduj(plik: str):
    with open(plik, 'r', encoding='utf-8') as f:
      bity = ''
      wynik = ''
      for ln in f:
        bity = ln.strip()
        for znak, wk in kodowanie.items():
          if bity[WKnaPozycje(wk) - 1] == '1':
            wynik += znak
            break
    return wynik

  @staticmethod
  def kodujDoPBM(znak: str):
    with open(f'{znak}.pbm', 'w', encoding='utf-8') as f:
      f.write('P1\n')
      f.write(f'# To jest bitmapa 25x25 z literką {znak}\n')
      f.write('25 25\n')
      Kryptotron.pokaz(f, znak, False)

# START
losowe_kody()  # ustalam na stałe kodowanie
# Bity znaku 'a' w 25 werszach po 25 kolumn. Zwróć uwagę, że tylko jeden bit
# na pewno się nie zmieni.
Kryptotron.pokaz(sys.stdout, 'a', False)
print()
# wersja jednoliniowa
Kryptotron.pokaz(sys.stdout, 'a')
print()

with open('164_kodowanie.txt', 'w', encoding='utf-8') as f:
  Kryptotron.pokazSlowo(f, "rabarbar")

print(Kryptotron.dekoduj('164_kodowanie.txt'))

# Tworzę plik PBM, który pozwala wyświetlić plik jako bitmapę czarno-białą,
# bazując na pliku tekstowym o ustalonym formacie
Kryptotron.kodujDoPBM('a')
Kryptotron.kodujDoPBM('b')
Kryptotron.kodujDoPBM('c')
# itd.


'''
Do sugestii z zadania:
Gdybym znał metodę szyfrowania, ale nie wiedział, jaki piksel
przypisany jest do literki, mógłbym wygenerować odpowiednią liczbę obrazków dla jednej i tej
samej literki. Piksel, który jest zawsze czarny, byłby kandydatem dla tej literki.
Piksele, które nigdy nie byłyby czarne, byłyby kandydatami na kody dla pozostałych liter. Tworząc
dla każdej literki taki zbiór, mógłbym z dużym prawdopodobieństwem odszyfrować, jaki piksel
przypisany jest literce.
'''
