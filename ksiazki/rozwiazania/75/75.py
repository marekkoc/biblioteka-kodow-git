# sposób 1
def czyPalindrom(s: str):
  return s[0::] == s[::-1]

print(czyPalindrom('kot'), czyPalindrom('kajak'), czyPalindrom('yyyYOYyyy'),
      czyPalindrom(''))

# sposób 2 (z własnym algorytmem sprawdzającym)
def czyPalindrom2(s: str):
  poczatek = 0
  koniec = len(s) - 1
  while (poczatek <= koniec):
    if (s[poczatek] != s[koniec]):
      return False
    poczatek += 1
    koniec -= 1
  return True

print(czyPalindrom2('kot'), czyPalindrom2('kajak'), czyPalindrom2('yyyYOYyyy'),
      czyPalindrom2(''))
