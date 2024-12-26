mapa_lasu = []  # linie znaków
with open('177_baba_jaga.txt', 'r', encoding='utf-8') as f:
  for ln in f:
    mapa_lasu.append(ln.strip())

# Ile jest obszarów 4x4 reprezentujących chatki (wg identycznych znaków, jakie
# je tworzą)?
obszary4 = dict()  # {'kod_znakowy_obszaru':ilość}
for w in range(0, 799):
  for k in range(0, 799):
    kod4 = ''
    kod4 += mapa_lasu[w][k:k + 2] + mapa_lasu[w + 1][k:k + 2]
    obszary4.setdefault(kod4, 0)
    obszary4[kod4] += 1

kandydaci = list(filter(lambda i: i[1] == 429, obszary4.items()))

# Ponieważ wiemy, że ilość chatek jest jednoznaczna,
# pierwszy element to odpowiedź.
print('Kod i ilość chatek:', kandydaci[0])
kod_chatki, ilosc = kandydaci[0]

numer = 1
for w in range(0, 799):
  for k in range(0, 799):
    kod4 = ''
    kod4 += mapa_lasu[w][k:k + 2] + mapa_lasu[w + 1][k:k + 2]
    if kod4 == kod_chatki:
      print('Chatka nr ', numer,
            f' położona w punkcie wiersz:kolumna = {w + 1}:{k + 1}')
      numer += 1
