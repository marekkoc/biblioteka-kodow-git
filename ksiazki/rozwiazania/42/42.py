from random import randint

napis = ''
litera = ''
while litera not in ['z', 'A']:
  if randint(0, 1):  # 50% szansy na dużą lub małą
    litera = chr(randint(65, 65 + 25))  # duża
  else:
    litera = chr(randint(97, 97 + 25))  # mała
  napis += litera

print('napis=\n', napis, '\nIlość losowań to ilość liter: ', len(napis))
