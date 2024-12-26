import operator

wszystko = ''
with open('169_liczby.txt', 'r', encoding='utf-8') as f:
  for ln in f:
    wszystko += ln.strip()

zliczacz = dict()  # { ciąg: ile }

for poz in range(0, len(wszystko) - 5):
  zliczacz.setdefault(wszystko[poz:poz + 6], 0)
  zliczacz[wszystko[poz:poz + 6]] += 1

zliczacz = sorted(zliczacz.items(), key=operator.itemgetter(1), reverse=True)
pierwszy = next(iter(zliczacz))
print(f'Podciąg o największej ilości powtórzeń '
      f'[{pierwszy[0]}] = {pierwszy[1]} razy.')
