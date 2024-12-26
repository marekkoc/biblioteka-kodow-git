spisy = []

with open('176_gustaw.txt', 'r', encoding='utf-8') as f:
  for ln in f:
    spisy.append(int(ln.strip()))
print(spisy)
print('Wpisów w pliku: ', len(spisy))

poz = len(spisy) - 1
while poz >= 1:
  if spisy[poz] - 50 < spisy[poz - 1]:
    break
  poz -= 1
print(f'Od dnia {poz + 2} każdy wzrost względem dnia poprzedniego'
      f' przekraczał 50 wyświetleń.')

ile = 0
for poz in range(0, len(spisy) - 2):
  if spisy[poz + 2] - spisy[poz + 1] < spisy[poz + 1] - spisy[poz]: ile += 1

print('Dni, w których wzrost był mniejszy niż wzrost dzień wcześniej = ', ile)
