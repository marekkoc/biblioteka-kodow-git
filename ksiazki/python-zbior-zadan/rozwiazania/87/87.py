def czescWsp(L1, L2):
  test = []
  for l1 in L1:
    for l2 in L2:
      if l1 == l2 and l1 not in test:
        test.append(l1)
        yield l1

print(*czescWsp([-8, 1, 2, 3, 4, 5, 6, 7, 8], [3, 4, 5, 3, 4, 5, 10, 12]))
print(*czescWsp([1, 2, 3], [4, 5, 6]))
print(*czescWsp([1, 2, 2, 3], [1, 2, 3]))
