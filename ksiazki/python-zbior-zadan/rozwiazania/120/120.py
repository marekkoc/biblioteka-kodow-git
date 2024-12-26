import time

# informacje zgromadzone na podstawie treści z zadania:
klasy = {
  '1A': {'ile': 18, 'piętro': 2}, '1B': {'ile': 21, 'piętro': 2},
  '1C': {'ile': 24, 'piętro': 2}, '1D': {'ile': 22, 'piętro': 1},
  '2A': {'ile': 20, 'piętro': 1}, '2B': {'ile': 20, 'piętro': 1},
  '2C': {'ile': 26, 'piętro': 1}, '3A': {'ile': 17, 'piętro': 0},
  '3B': {'ile': 19, 'piętro': 0}, '3C': {'ile': 21, 'piętro': 0}
}
# ile metrów do przejścia
odleglosci = {2: 28, 1: 18, 'E1': 12, 'E2': 12, 'E3': 23}
drzwiPrzepustowosc = {'E1': {'ile': 1, 'co': 2}, 'E2': {'ile': 1, 'co': 2.5},
                      'E3': {'ile': 3, 'co': 1}}
wyjscia = {
  '1A': 'E1', '1B': 'E2', '1C': 'E1', '1D': 'E3', '2A': 'E3', '2B': 'E2',
  '2C': 'E2', '3A': 'E3', '3B': 'E3', '3C': 'E3'
}

class Sala:
  def __init__(self):
    self.osoby = []
    self.wypusc = 1  # ilu wypuszcza
    self.co = 1  # na sekundę
    self.odliczanie = 0  # wewnętrzny upływ czasu do wypuszczenia osób

  def __str__(self):
    return 'Osób w sali:' + str(len(self.osoby)) + ' ' + self.osoby[0].klasa

class Osoba:
  def __init__(self, kategoria: str = 'uczeń'):
    self.czas = 0  # wewnętrzny upływ czasu
    self.metryDoWyjscia = 0  # ile metrów
    self.metry_na_s = (2, 1)  # prędkość poruszania
    self.klasa = ''
    self.kategoria = kategoria
    self.cel = ''  # drzwi E1-3

  def __str__(self):
    return ('Osoba z klasy:' + self.klasa + ' do wyjścia ' + self.cel
            + ' zostało ' + str(self.metryDoWyjscia))

# wkładam uczniów i nauczycieli do sal
sale = []
for klasa in klasy.keys():
  sala = Sala()
  # wkładam do sali uczniów
  for i in range(klasy[klasa]['ile']):
    osoba = Osoba('uczeń')  # uczniowie
    # obliczam drogę do przejścia dla ucznia
    d = 0
    if klasy[klasa]['piętro'] == 2:
      d += odleglosci[2] + odleglosci[1] + odleglosci[wyjscia[klasa]]
    elif klasy[klasa]['piętro'] == 1:
      d += odleglosci[1] + odleglosci[wyjscia[klasa]]
    else:
      d += odleglosci[wyjscia[klasa]]
    osoba.metryDoWyjscia = d  # ile musi przejść korytarzami do wyjścia
    osoba.klasa = klasa  # osoba z klasy
    osoba.cel = wyjscia[klasa]  # do którego wyjścia idzie
    sala.osoby.append(osoba)  # na listę do klasy
  # nauczyciel
  osoba = Osoba('nauczyciel')
  osoba.metryDoWyjscia = sala.osoby[
    0].metryDoWyjscia  # tyle co uczniowie z klasy
  osoba.klasa = sala.osoby[0].klasa  # przypisany do klasy z uczniami
  osoba.cel = sala.osoby[0].cel  # idzie tam gdzie uczniowie z klasy
  sala.osoby.append(osoba)  # + nauczyciel do sali
  sale.append(sala)  # plus sala do sal

print(*sale, sep='\n')

# Tutaj (Korytarze) siedzą uczniowie i nauczyciele po wyjściu.
# Każdy musi przejść korytarzem ileś-tam metrów, aby dostać się do kolejki
# przed drzwiami ewakuacyjnymi
class Korytarze:
  osoby = []

# kolejki przed drzwiami ewakuacyjnymi
class Drzwi:
  def __init__(self, nr):
    self.odliczanie = 0
    self.osoby = []
    self.nr = nr
    self.ileOsob = drzwiPrzepustowosc[nr]['ile']
    self.coIleSekund = drzwiPrzepustowosc[nr]['co']

drzwiWyjsciowe = {'E1': Drzwi('E1'), 'E2': Drzwi('E2'), 'E3': Drzwi('E3')}

KROK = 0.5  # sekundy, atom czasu (o tyle zmienia się czas w symulacji co krok)
CZAS = 0  # globalny upływ czasu

uratowani = []

while True:
  # time.sleep(0.5)
  CZAS += KROK
  print('CZAS GLOBALNY: ', CZAS)

  # opuszczamy wyjścia ewakuacyjne
  for wyjscie, e in drzwiWyjsciowe.items():
    if (len(e.osoby)):
      e.odliczanie += KROK
      if e.odliczanie >= e.coIleSekund:
        e.odliczanie = 0
        for i in range(e.ileOsob):
          if (len(e.osoby)):
            e.osoby[0].czasOpuszczenia = CZAS
            print('Wyjściem', wyjscie, 'wychodzi osoba z klasy',
                  e.osoby[0].klasa)
            uratowani.append(e.osoby[0])
            e.osoby.pop(0)

  # koniec symulacji, wszyscy poza szkołą
  if (len(uratowani) == 218):
    print('Ewakuacja udana. Czas ewakuacji: ', CZAS,
          '. Wszystkie osoby uratowane: ', len(uratowani))
    print('Nauczyciele wychodzili w kolejności:')
    ostatni = None
    for o in uratowani:
      if o.kategoria == 'nauczyciel':
        ostatni = o
        print('Nauczyciel z klasy', o.klasa, 'wyszedł po', o.czasOpuszczenia,
              'sekundach.')
    print('Ostatnim nauczycielem był nauczyciel z klasy', ostatni.klasa)
    break

  # analiza Korytarzy i ruch osób na korytarzu
  print('Osób w korytarzach: ', len(Korytarze.osoby))
  if (len(Korytarze.osoby)):
    for osoba in Korytarze.osoby:
      osoba.czas += KROK
      if osoba.czas >= osoba.metry_na_s[1]:
        osoba.czas = 0
        osoba.metryDoWyjscia -= osoba.metry_na_s[0]  # skraca
      # osoba trafia do kolejki przed wyjściem
      if osoba.metryDoWyjscia <= 0:
        print('Osoba z klasy', osoba.klasa, 'trafiła do wyjścia', osoba.cel)
        drzwiWyjsciowe[osoba.cel].osoby.append(osoba)  # dodana do wyjścia
    Korytarze.osoby = list(
      filter(lambda o: o.metryDoWyjscia > 0, Korytarze.osoby))

  # wychodzenie z sal (o ile są w nich osoby)
  for sala in sale:
    if len(sala.osoby):
      sala.odliczanie += KROK
      if sala.odliczanie >= sala.co:
        sala.odliczanie = 0  # zerowanie odliczania do nast. wypuszczenia
        # wypuść osobę na korytarz i nic już nie rób w tym kroku czasu
        for i in range(1, sala.wypusc + 1):
          if len(sala.osoby):  # wychodzą osoby, o ile są
            Korytarze.osoby.append(sala.osoby.pop(0))
          else:
            break

  # opuszczanie sal
