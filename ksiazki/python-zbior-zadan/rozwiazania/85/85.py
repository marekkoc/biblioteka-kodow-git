def mCount(L, x: int):
  ile = 0
  for a in L:
    if x == a:
      ile += 1
  return ile

L = [1, 2, 3, 1, 3, 5, 4, 3, 1, 6, 100, 8, 7, 4, 8, 9, 9, 1]
print(mCount(L, 3))
