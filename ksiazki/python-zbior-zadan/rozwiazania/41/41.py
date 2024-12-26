from random import randint

L = []

def funkcja(li=[]):
  maks = 0
  for i in li:
    if maks < i:
      maks = i
  li.remove(maks)
  s = sum(li)
  for ile in range(maks):
    print(s, end=' ')
  print()
  return maks

for i in range(3):
  L.append(randint(1, 100))

print(L)  # przed
print(funkcja(L))  # rysuje sumy, zwraca maks
print(L)  # maks usunięty z L
