from random import uniform

# uniform losuje włącznie z
def symulacja(a=None, b=None, c=None):
  ''' Test losowego trójkąta prostokątnego '''
  if a is b is c is None:
    a, b, c = (round(uniform(0.00001, 100), 2),
               round(uniform(0.00001, 100), 2), round(uniform(0.00001, 100), 2))
  ak = round(a ** 2, 2)
  bk = round(b ** 2, 2)
  ck = round(c ** 2, 2)
  ab = round(ak + bk, 2)
  bc = round(bk + ck, 2)
  ac = round(ak + ck, 2)
  if ab == ck or ac == bk or bc == ak:
    print('\n\nIstnieje możliwość zbudowania trójkąta prostokątnego.')
    print('Tworzą je boki =', a, b, c, sep='   ')
    s = sorted([ak, bk, ck])
    print(f'Kolejne obliczenia a**2 + b**2 = c**2, i ich sumy: {s[0]} + {s[1]} = {s[2]}', )
    return True
  else:
    return False

symulacja(3, 4, 5)

sym = 0
while not symulacja():
  sym += 1
  pass
print('Ilość symulacji: ', sym)
