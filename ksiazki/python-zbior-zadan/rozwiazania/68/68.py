from random import randint

L = []
o = []  # ostatnie 3 wylosowane
ileLosowan = 0;

def ok(ostatnie):
  if len(ostatnie) < 3: return False
  return (80 <= sum(ostatnie) <= 90)

while not ok(o):
  n = randint(1, 300)
  ileLosowan += 1
  if len(o) == 3: o.pop()
  o.insert(0, n)
  if len(L) == 0 or (n >= L[-1]):
    L.append(n)

print('Ostatnie 3 wylosowane spełniające warunek: ', o, 'Suma=', sum(o))
print('Lista:', L)
print('Długość listy:', len(L))
print('Wylosowanych liczb:', ileLosowan)
