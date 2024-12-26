from random import randint

znak = input('Podaj znak:')
A = randint(5, 10)
B = randint(5, 10)
print('A=', A, 'B=', B)

# sposób 1
def prostokat(znak, a, b):
  for i in range(a):
    for j in range(b):
      print(znak, sep='', end='')
    print()

# sposób 2
def prostokat2(znak, a, b):
  for i in range(a):
    print(znak * b)

# sposób 3 (taki pythonowy!)
def prostokat3(znak, a, b):
  print('\n'.join(a * [znak * b]))

prostokat(znak, A, B)
print('\n')
prostokat2(znak, A, B)
print('\n')
prostokat3(znak, A, B)
