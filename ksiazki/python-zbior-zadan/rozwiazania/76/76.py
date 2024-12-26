def ileAwB(A: str, B: str):
  ile = 0
  poz = -1
  while True:
    poz = B.find(A, poz + 1)
    if poz > -1:
      ile += 1
    else:
      break
  return ile

print(ileAwB('jo', 'jojowanie jest fajowe'))
# Nie wiesz, co to jojowanie? Ja też.
