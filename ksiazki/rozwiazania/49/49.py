from random import randint

L = randint(20, 30)
print('L=', L)
Z = ''
while len(Z) == 0 or len(Z) > 1:
  Z = input('Podaj znak: ')
for i in range(L):
  print(Z, end='')
print()
print(Z * L)  # można i tak
