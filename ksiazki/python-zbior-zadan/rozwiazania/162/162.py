class Obiekt:
  def __init__(self, dane: str):
    id, bity, ile = dane.split(' ')
    self.ID = id.strip()
    self.poprawny = True
    self.bity = bity.strip()  # 32-bitowa liczba jako str
    self.ile_w_zwiazku = int(ile.strip())
    # Lista obiektów w interakcji z self, obiekty między soba nie muszą być
    # interakcyjne (zgodnie z definicją z zadania).
    # Lista self.interakcyjni nie zawieraj obiektu self.
    self.interakcyjni = set()

  def mozliwe_zwiazki(self):
    if self.ile_w_zwiazku == 2:
      return len(self.interakcyjni)
    elif self.ile_w_zwiazku == 3:
      trojki = 0
      # sprawdzam, czy para dodatkowa jest ze sobą w interakcji
      pomoc = list(self.interakcyjni)
      for p1 in range(0, len(pomoc)):
        for p2 in range(p1 + 1, len(pomoc)):
          if pomoc[p1].czyIter(pomoc[p2]): trojki += 1
      return trojki
    return 0

  # Sprawdzanie interakcji, jeżeli a==b to przynajmniej
  # 24 bity są zgodne na tych samych pozycjach.
  def czyIter(self, other):
    i = 0
    for poz in range(0, 32):
      if (self.bity[poz] == other.bity[poz]): i += 1
    return (i >= 24)

  def __hash__(self):
    return 0

  def __str__(self):
    return f'[{self.ID}]'

dane = dict()  # { str(obiekt) : Obiekt() }
niepoprawne = set()  # niepoprawne obiekty

with open('162_dane_we.txt', 'r', encoding='utf-8') as f:
  for ln in f:
    obiekt = Obiekt(ln.strip())
    if obiekt.ID in dane.keys():
      dane[
        obiekt.ID].poprawny = False  # obiekt istnieje, więc jest niepoprawny!
      niepoprawne.add(obiekt.ID)
    else:
      dane[obiekt.ID] = obiekt

# niepoprawne !
print('Obiekty niepoprawne:')
print(*niepoprawne, sep='\n')
print()
# Usuwam z danych obiekty niepoprawne. Nie będę ich analizował.
print(len(dane))
dane = dict(
  sorted(dict(filter(lambda o: o[1].poprawny == True, dane.items())).items()))
print(len(dane))

# szukam interakcyjnych obiektów (dla każdego szukam innych)
print(f'... 0/{len(dane)} ...')
i = 0
l = list(dane.values())
for poz1 in range(0, len(l)):
  o = l[poz1]
  i += 1
  if i % 100 == 0:
    print(f'... {i}/{len(dane)} ...')
  for poz2 in range(poz1 + 1, len(l)):
    o2 = l[poz2]
    if o.ID == o2.ID: continue  # ten sam, omijam
    if o.czyIter(o2):  # Porównanie, czyli badanie interakcyjności.
      o.interakcyjni.add(o2)
      o2.interakcyjni.add(o)

with open('162_dane_wy.txt', 'w', encoding='utf-8') as f:
  for n in niepoprawne:
    f.write(n + '\n')
  for s, o in dane.items():
    f.write(f'{s} {len(o.interakcyjni)} {o.mozliwe_zwiazki()}\n')
