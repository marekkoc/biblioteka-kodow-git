ileznakow = 0
znak = ''
while znak != 'x':
  znak = input('Podaj znak = ')
  if len(znak) > 0:
    znak = znak[0]
    ileznakow += 1
    print('Wprowadzono znak = ', znak)
  else:
    print('Postaraj się wprowadzić chociaż jeden znak.')
print('Wprowadzono', ileznakow, 'znaków.')
