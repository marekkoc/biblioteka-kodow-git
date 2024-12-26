spadek = 1
start = 100
for i in range(1, 101):
  print(start, end=' ')
  start -= spadek  # kolejne liczby są mniejsze o 1,2,3...
  spadek += 1
print()
print('Ostatnia wartość', start + spadek - 1)
