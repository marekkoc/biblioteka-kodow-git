def palindrom(a):
  return a == a[::-1]

def szukajPalindromaSzukaj(s: str):
  wyniki = []
  for dlugosc in range(2, len(s) + 1):
    for start in range(0, len(s) - dlugosc + 1):
      testowany = s[start:start + dlugosc]
      if palindrom(testowany):
        wyniki.append(testowany)
  return wyniki

print(szukajPalindromaSzukaj('kajak'))
print(szukajPalindromaSzukaj('rabarbar'))
print(szukajPalindromaSzukaj('kukurydza'))
print(szukajPalindromaSzukaj('parapet'))
print(szukajPalindromaSzukaj('piszczel'))
