a, b = 6, 2
step1, step2 = 2, 1
for i in range(1, 51):
  print(a, b, end=',', sep=',')
  a, b = a + step1, b + step2
