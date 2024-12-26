from random import uniform

L = []
for i in range(20):
  L.append(round(uniform(-1, 1), 3))
print(L)
print('Średnia:', round(sum(L) / 20, 5))
