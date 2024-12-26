x = [2, 7, 1, 1, 4, 9, 3, 2, 1, 4, 1, 9, 6, 1, 3, 0, 1, 2, 3, 6, 8, 5, 6, 9, 3,
     0, 8, 1, 8, 8, 7, 0, 7, 8, 5, 0, 2, 2,
     3, 7, 1, 7, 2, 4, 7, 7, 5, 9, 0, 7, 7, 9, 2, 2, 2, 7, 0, 0, 5, 4, 6, 3, 9,
     3, 5, 1, 0, 0, 9, 2, 9, 2, 8, 5, 0, 8,
     5, 7, 0, 9, 6, 4, 9, 7, 8, 8, 6, 5, 4, 3, 2, 5, 8, 9, 4, 6, 8, 7, 9, 9]

# sposób 1
odl = -1
for poz in range(len(x)):
  if x[poz] == 9:
    if odl != -1:
      print(odl, end=' ')
    odl = 0
  elif odl != -1:
    odl += 1

print()

# sposób 2
import re

for s in list(filter(lambda temp: len(temp) >= 0,
                     re.split(r'(9[0-8]*?)',
                              ''.join([str(c) for c in x]))))[1:-2]:
  if s != '9':
    print(len(s), end=' ')

print()
# Tak. Czary. Metoda split() dla wyrażeń regularnych wraz ze wzorcem:
# r'(9[0-8]*?)'
# dzieli ciąg cyfr na podciągi, które możesz podglądnąć, wywołując tę linię kodu:
# print(list(filter(lambda temp: len(temp) >= 0, re.split(r'(9[0-8]*?)', ''.join([str(c) for c in x]))))[1:-2])
# Podział następuje tak, iż cyfra '9' jest miejscem separacji. Podciągi między nimi, a ściślej ich długości, odpowiadają
# liczbom, które są oczekiwanym wynikiem zadania.
