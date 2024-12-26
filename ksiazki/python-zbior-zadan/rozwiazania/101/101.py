import operator

dane = dict()
with open('101_dane.txt', 'r', encoding='utf-8') as f:
  for ln in f:
    d = ln.split('\t')
    # { dzień : ('osoba', pomiar) ... }
    dane[int(d[2])] = (d[0], int(d[1]))

pomiary = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0}
suma = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0}

for k, v in dane.items():
  pomiary[v[0]] += 1
  suma[v[0]] += v[1]
# sortowanie po wartościach słownika, a nie po kluczu
pomiary = sorted(pomiary.items(), key=operator.itemgetter(1), reverse=True)
print('Osobą, która wykonała najwięcej pomiarów, jest: ', pomiary[0][0],
      ' (ilość=', pomiary[0][1], ')')

pomiary = dict(pomiary)
for kto, ile in pomiary.items():
  print('Osoba', kto, 'wykonała ', ile, 'pomiarów o sumie', suma[kto],
        'a średnia wynosi', suma[kto] / ile)

# Zakładam, że poniedziałek to 0, wtorek to 1 itd. Pierwszy dzień (d=1) to wtorek
sumaWeWtorki = 0
for d, (kto, pomiar) in dane.items():
  if d % 7 == 1: sumaWeWtorki += pomiar
print('Suma pomiarów z wtorków: ', sumaWeWtorki)
