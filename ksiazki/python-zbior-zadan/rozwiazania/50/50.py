# n: int podaje oczekiwany typ argumentu
# -> bool informuje o zwracanym typie
def czyParzysta(n: int) -> bool:
  return not n & 1  # ostatnia liczba

# test
for x in range(0, 7):
  print(x, czyParzysta(x), end=';  ')
print()

# można trochę udoskonalić informację o parzystości/nieparzystości
def Slownie(pnp):
  if pnp: return 'Parzysta'
  return 'Nieparzysta'

# test
for x in range(6, 13):
  print(x, Slownie(czyParzysta(x)), end=';  ')
print()
