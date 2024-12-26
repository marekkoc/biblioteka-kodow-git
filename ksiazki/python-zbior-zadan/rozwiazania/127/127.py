weryfikowane = set()  # wypełnimy palindromicznymi zweryfikowanymi
wygenerowane = set()  # wypełnimy generatorem

def czyPalindromiczna(n: int):
  return (str(n) == str(n)[::-1])

def wszystkiePalindromiczneZweryfikowane(od=10, do=99999):
  for n in range(od, do + 1):
    if czyPalindromiczna(n):
      weryfikowane.add(n)

def generatorPalindromicznych(prefix: str = '', od=2, do=5):
  if len(prefix) > 3: return
  for palindromiczna in [prefix + prefix[::-1], prefix + prefix[:-1:][::-1]]:
    if len(palindromiczna) <= do and len(palindromiczna) >= od:
      wygenerowane.add(int(palindromiczna))
  for cyfra in '0123456789':
    if prefix == '' and cyfra == '0': continue
    generatorPalindromicznych(prefix + cyfra, od, do)

wszystkiePalindromiczneZweryfikowane()
generatorPalindromicznych('', od=2, do=5)

# pokaż zbiory, posortuję (kopie) dla czytelności
print(sorted(weryfikowane))
print(sorted(wygenerowane))

if weryfikowane == wygenerowane:
  print('Uzyskano takie same zbiory.')

# dla pewności różnica zbiorów powie mi, czy aby się nie różnią ;)
print(weryfikowane.difference(wygenerowane))  # różnica zbiorów -> zbiór pusty.
print(wygenerowane.difference(weryfikowane))  # różnica zbiorów -> zbiór pusty.
