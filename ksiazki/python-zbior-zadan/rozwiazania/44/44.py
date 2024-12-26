from random import randint

ile = 0
while True:
  n = randint(0, 100)
  print(n, end=' ')
  if n == 100: break  # break uniemożliwi zliczanie, gdy wypadnie 100
  ile += 1

print()
print('Liczba losowań, zanim wypadło 100:', ile)
