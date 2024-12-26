# sposób 1 (funkcja wersja 1)
def sklejanieNaPrzemian(L1, L2):
  L = []
  while len(L1) and len(L2):
    L.append(L1.pop(0))
    L.append(L2.pop(0))
  L.extend(L1)
  L.extend(L2)
  return L

# sposób 2 (funkcja wersja 2)
def sklejanieNaPrzemian2(L1, L2):
  L = []
  L = list(sum(zip(L1, L2), ()))
  L.extend(L2[len(L1):])
  L.extend(L1[len(L2):])
  return L

# przykład dla dwóch list L1 i L2
L1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
L2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]

print(sklejanieNaPrzemian(L1.copy(), L2.copy()))
print(sklejanieNaPrzemian2(L1.copy(), L2.copy()))
