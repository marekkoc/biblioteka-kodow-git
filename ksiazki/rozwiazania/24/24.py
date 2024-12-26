L = []
while True:
  znak = input('Podaj znak:')[0]
  if znak in 'aeyuio':
    L.insert(0, znak)  # na przód
  elif znak not in ('!#*'):
    L.append(znak)  # na koniec
  elif znak == '*' and len(L) > 0:
    L.pop(0)  # usuń z przodu, można del L[0]
  elif znak == '#' and len(L) > 0:
    L.pop()  # usuń z początku
  elif znak == '!':
    break
  print('Całe słowo: ', *L, sep='')
