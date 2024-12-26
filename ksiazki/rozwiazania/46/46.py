from random import randint

L = []
while len(L) < 20:
  L.append(randint(0, 1000))
print(L)

# sposób 1
print(*sorted(L, reverse=True)[:3])  # rozpakowanie * można pominąć

# sposób 2 (bez posortowania, z funkcją max)
Copy = L.copy()  # kopia dla 3 sposobu (w 2 sposobie zmieniam L)
for i in range(3):
  print(max(L), end=' ')
  L.remove(max(L))
print()

# sposób 3 (bez pomocniczych funkcji jak sort czy max oraz remove
L = Copy  # przywracam oryginalną zawartość
poz = 0
mp = 0
for i in range(3):
  maks = L[poz]
  for p in range(poz, len(L)):
    if maks < L[p]:
      maks = L[p]
      mp = p
  L[mp], L[poz] = L[poz], L[mp]
  poz += 1
print(*L[:3])
