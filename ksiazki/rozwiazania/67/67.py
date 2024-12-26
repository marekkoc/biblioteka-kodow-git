from random import uniform

def liniowAXplusB(a: float, b: float, x: float):
  return a * x + b

L = []
for i in range(100):
  L.append([round(uniform(-10, 10), 1),
            round(uniform(-10, 10), 1)])  # punkt losowy [x,y]
print(L)

def zliczaj(L: list):
  odp = {'na': 0, 'nad': 0, 'pod': 0}
  for (x, y) in L:
    if (liniowAXplusB(2, 3, x) == y):
      odp['na'] += 1
      print('Punkt na funkcji 2x+3!', x, ':', y)
    elif liniowAXplusB(2, 3, x) < y:
      odp['nad'] += 1
    else:
      odp['pod'] += 1
  print(odp)

zliczaj(L)
# test dla przykładowych danych z zadania
L = [[0, 1], [1, 10], [2, 7]]

zliczaj(L)
