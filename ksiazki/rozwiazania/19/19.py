ile = 0
ile7 = 0
siodemki = []
for x in range(0, 1001):
  if x % 6 == 0:
    print(x, end=' ')
    ile += 1
    if '7' in str(x):
      ile7 += 1
      siodemki.append(x)
print()
print('Liczb podzielnych: ', ile)
print('Liczb z 7-ką wewnątrz: ', ile7, siodemki)
