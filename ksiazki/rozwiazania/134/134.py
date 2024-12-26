class Czas:
  def __init__(self, s, k, nrp):
    self.start = s
    self.koniec = k
    self.nr_papugi = nrp

  def __str__(self):
    return 'Papuga nr ' + str(self.nr_papugi) + '. Czas od ' + str(
      self.start) + ' do ' + str(self.koniec)

  def ile(self):
    return self.koniec - self.start

  def czy_gada(self, sekunda, other):
    return (self.start <= sekunda and self.koniec > sekunda) or (
        other.start <= sekunda and other.koniec > sekunda)

papugi = []  # papugę będzie reprezentować krotka (Czas,Czas)
with open('134_papugi.txt', 'r', encoding='utf-8') as f:
  f.readline()  # ignoruję pierwszy wiersz
  temp = ''
  ostatnia_sekunda = 0
  najdluzsze_gderanie = 0
  for ln in f:
    numer, s1, k1, s2, k2 = [int(x.strip()) for x in ln.split(' ')]
    papugi.append(
      (Czas(s1, k1, len(papugi) + 1), Czas(s2, k2, len(papugi) + 1)))
    if k2 > ostatnia_sekunda:
      ostatnia_sekunda = k2
    gderanie = papugi[-1][0].ile() + papugi[-1][1].ile()
    if najdluzsze_gderanie < gderanie:
      najdluzsze_gderanie = gderanie

# Która papuga gderała łącznie najdłuższą ilość sekund?
# (może być ich więcej, więc szukam wielu)
nr_papugi = []
for c1, c2 in papugi:
  if (c1.ile() + c2.ile() == najdluzsze_gderanie):
    nr_papugi.append(c1.nr_papugi)
print('Najdłużej, bo aż', najdluzsze_gderanie, 'sekund darła się papuga nr:',
      nr_papugi)

# Ile papug wydawało nieprzerwanie dźwięk od 120. do 130.
# sekundy badań (włącznie ze 130. sekundą) ?

ile_120130 = 0
for c1, c2 in papugi:
  if c1.start <= 120 and c1.koniec > 130 or c2.start <= 120 and c2.koniec > 130:
    ile_120130 += 1
print(ile_120130,
      'papug wydawało nieprzerwanie głos między 120. a 130. sekundą.')

# Podaj sekundy pomiaru, podczas których największa liczba papug wydawała dźwięki równocześnie?
# (zrobię to dla ćwiczenia umysłu metodą Baby Yody, poprzez symulację upływu
# sekund i sprawdzanie, ile papug śpiewa w tym momencie)
ile_papug = 0
ile_w_sekundzie = []
for sekunda in range(1, ostatnia_sekunda + 1):
  ile_papug_w_sekundzie = 0
  for c1, c2 in papugi:
    if c1.czy_gada(sekunda, c2):
      ile_papug_w_sekundzie += 1
  if ile_papug_w_sekundzie > ile_papug:
    ile_papug = ile_papug_w_sekundzie
  ile_w_sekundzie.append(ile_papug_w_sekundzie)

for sek in range(0, len(ile_w_sekundzie)):
  if ile_w_sekundzie[sek] == ile_papug:
    print(sek + 1, 's.', ile_w_sekundzie[sek], 'papug.')

# Ile papug skrzeczało krócej za drugim wydanym głosem?
ilek = 0
for c1, c2 in papugi:
  if c1.ile() > c2.ile():
    ilek += 1
print('Krócej za drugim skrzeczeniem darło się ', ilek, 'papug.')
