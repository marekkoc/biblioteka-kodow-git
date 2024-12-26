def ostatni(N, K):
  lista = list(range(1, N + 1))
  print('N=', N, 'K=', K)
  pozycja = 0
  while len(lista) > 1:
    pozycja = (pozycja + K) % len(lista)
    lista.pop(pozycja)
    if pozycja == len(lista):  # zachowuję cykliczność
      pozycja = 0
  return lista[0]

# z przykładów do zadania
print(ostatni(6, 3))
print(ostatni(8, 3))

# rozwiązania
print(ostatni(100, 3))
print(ostatni(200, 5))
print(ostatni(30, 17))
print(ostatni(25000, 89))
