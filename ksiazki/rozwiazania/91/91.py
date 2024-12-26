import re

# Pomysł algorytmu polega na redukowaniu części poprawnych
# do innych poprawnych, ale krótszych, np.: 1+1 redukuje do 1
# a+b do a, (1) do 1 itd.
# Uwaga! Wydaje mi się, że poniższy algorytm jest prawidłowy. Nie znalazłem
# jeszcze kontrprzykładu, który by go obalił.
def poprawny(wyr: str):
  print('Badam', wyr, end=' -> ')
  # redukuję każdy ciąg cyfr na 1: nie zmienia to poprawności 123*b 1*b itd.
  wyr = re.sub(r'[0-9]+', r'1', wyr)
  # zamieniam wszystkie litery na a: nie zmienia to poprawności a+c to a+a
  wyr = re.sub(r'[a-z]{1}', r'a', wyr)
  # zmieniam 1 na a
  wyr = re.sub(r'1{1}', r'a', wyr)
  # zmieniam działania na działanie '-', nie ruszam znaku =
  wyr = re.sub(r'[\+\-\*\/\^\%]{1}', r'-', wyr)
  # redukuję do oporu (a) oraz (-a) do a, oraz a-a do a
  while True:
    temp = wyr
    wyr = re.sub(r'\(a\)', r'a', wyr)
    wyr = re.sub(r'\(\-a\)', r'a', wyr)
    wyr = re.sub(r'a\-a', r'a', wyr)
    if temp == wyr: break
  # redukuję a=a do a
  while True:
    temp = wyr
    wyr = re.sub(r'a=a', r'a', wyr)
    if temp == wyr: break
  print(wyr, end=' ')
  if (wyr == 'a' or wyr == '-a' or wyr == ''): return True
  return False

print(poprawny('(12*x+3*(3*d-a)^3)/11=z'))
print(poprawny('-3*x+781/a=2+(1*a)-3/b%10+(1)-(-a)/100'))
print(poprawny('a+b-c('))
print(poprawny('a+b-c=d*(-1123)'))
print(poprawny(''))  # napis pusty uznajemy za poprawny
print(poprawny('-a-a-xx'))  # napis pusty uznajemy za poprawny
print(poprawny('--10'))  # uznajemy za niepoprawny (nagromadzenie znaków)
print(poprawny('-(-10)'))  # ale -(-10) byłby poprawny
print(poprawny('1+(=a=a)'))
print(poprawny('10^((a+b+43587*4)+(-10/a*b)+(u+i+g%10)/(-7-1/10))'))
print(poprawny('a/(a=b)'))
print(poprawny('))a+b(('))  # statek X-Wing na 2 osoby
print(poprawny('a==b'))
