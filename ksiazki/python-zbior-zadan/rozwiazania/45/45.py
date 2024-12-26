from random import randint

L = []
for i in range(10):
  L.append(randint(-10, 10))
print(L)

# sposób 1
print('Ujemnych = ', len(list(filter(lambda x: x < 0, L))))
print('Dodatnich = ', len(list(filter(lambda x: x > 0, L))))
print('Nieparzystych = ', len(list(filter(lambda x: x % 2, L))))
print('Parzystych = ', len(list(filter(lambda x: not x % 2, L))))

# sposób 2
iled = ileu = ilep = ilenp = 0
for i in L:
  if i < 0:
    ileu += 1
  elif i > 0:
    iled += 1
  if i % 2:
    ilenp += 1
  else:
    ilep += 1
print()
print('Ujemnych =', ileu, '\nDodatnich =', iled, '\nNieparzystych =', ilenp,
      '\nParzystych =', ilep)
