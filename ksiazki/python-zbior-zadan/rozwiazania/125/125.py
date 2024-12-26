def dzielnikiWlasciwe(n: int):
  for dzielnik in range(1, n):
    if n % dzielnik == 0:
      yield dzielnik

print('Liczby doskonałe:')
for i in range(1, 10001):
  dzielniki = list(dzielnikiWlasciwe(i))
  if i == sum(dzielniki):
    print(i, '=', end=' ')
    print(*dzielniki, sep='+')
