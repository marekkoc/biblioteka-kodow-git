imiona = '92_imiona.txt'
nazwiska = '92_nazwiska.txt'

# wersja 1 (bez uwzględniania płci)
print('Wersja 1')
# wprawdzie pliki mogłyby zostać utworzone ręcznie, ale tutaj wygeneruje je kodem
with open(imiona, 'w', encoding='utf-8') as f:
  f.write('Paweł\n')
  f.write('Katarzyna\n')
  f.write('Radosław\n')
  f.write('Ambroży\n')
  f.write('Anna\n')
  f.write('Helena\n')
  f.write('Karolina\n')
  f.write('Zbyszek\n')
  f.write('Alicja\n')
  f.write('Filiżanka\n')

with open(nazwiska, 'w', encoding='utf-8') as f:
  f.write('Kowalski\n')
  f.write('Nowak\n')
  f.write('Pieczarkowski\n')
  f.write('Nowosielski\n')
  f.write('Bronowiecki\n')
  f.write('Pancogitian\n')
  f.write('Materacjański\n')
  f.write('Naleśnikowicz\n')
  f.write('Pytonowski\n')
  f.write('Pehapowiec\n')

def generatorVer1():
  with open(imiona, 'r', encoding='utf-8') as f_imiona:
    i = [im.strip() for im in f_imiona]
  with open(nazwiska, 'r', encoding='utf-8') as f_nazwiska:
    n = [na.strip() for na in f_nazwiska]
  import random
  random.shuffle(i)
  random.shuffle(n)
  return i[0] + ' ' + n[0]

print(generatorVer1())
print(generatorVer1())
print(generatorVer1())

# wprawdzie pliki mogłyby zostać utworzone ręcznie, ale tutaj wygeneruje je kodem
with open(imiona, 'w', encoding='utf-8') as f:
  f.write('Paweł;m\n')
  f.write('Katarzyna;k\n')
  f.write('Radosław;m\n')
  f.write('Ambroży;m\n')
  f.write('Anna;k\n')
  f.write('Helena;k\n')
  f.write('Karolina;k\n')
  f.write('Zbyszek;m\n')
  f.write('Alicja;k\n')
  f.write('Filiżanka;k\n')

with open(nazwiska, 'w', encoding='utf-8') as f:
  f.write('Kowalski;Kowalska\n')
  f.write('Nowak;Nowak\n')
  f.write('Pieczarkowski;Pieczarkowska\n')
  f.write('Nowosielski;Nowosielska\n')
  f.write('Bronowiecki;Bronowiecka\n')
  f.write('Pancogitian;Pancogitian\n')
  f.write('Materacjański;Materacjańska\n')
  f.write('Naleśnikowicz;Naleśnikowicz\n')
  f.write('Pytonowski;Pytonowska\n')
  f.write('Pehapowiec;Pehapowiczowa\n')

def generatorVer2():
  with open(imiona, 'r', encoding='utf-8') as f_imiona:
    i = [im.strip().split(';') for im in f_imiona]
  with open(nazwiska, 'r', encoding='utf-8') as f_nazwiska:
    n = [na.strip().split(';') for na in f_nazwiska]
  import random
  random.shuffle(i)
  random.shuffle(n)
  if (i[0][1] == 'm'):
    return i[0][0] + ' ' + n[0][0]
  return i[0][0] + ' ' + n[0][1]

print()
print('Wersja 2')
print(generatorVer2())
print(generatorVer2())
print(generatorVer2())
