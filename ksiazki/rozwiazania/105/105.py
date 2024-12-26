def podzielna(N, p):
  while N >= p:
    N -= p
  return N == 0

for N, p in ((100, 7), (100, 10), (777, 111), (321, 11), (24, 6)):
  if podzielna(N, p):
    print(f'p={p} dzieli N={N}.')
  else:
    print(f'p={p} nie dzieli N={N}.')
