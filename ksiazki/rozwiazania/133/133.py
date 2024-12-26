kulki = [(nr + 1, x) for nr, x in
         enumerate(['czerwona'] * 7 + ['biała'] * 9 + ['czarna'] * 14)]
# kulki to lista krotek: (nr_kulki, kolor_kulki)
print(kulki)

co = 5  # co ile kasujemy
start = 0  # pierwsza pozycja
while len(kulki) > 1:
  poz = start + co - 1
  if poz >= len(kulki):
    poz = poz % len(kulki)
  del kulki[poz]
  if poz == len(kulki):
    start = 0
  else:
    start = poz

print('Została kulka:', *kulki)
