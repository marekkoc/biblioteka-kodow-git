# sposób 1
import re

suma = 0
while suma <= 550:
  znak = input('Podaj znak:')
  if re.match('^[a-zA-Z0-9]{1}$', znak):
    print('Znak odpowiedni.')
    print('Kod znaku=', ord(znak))
    suma += ord(znak)
    print('Aktualna suma =', suma)
  else:
    print('Znak nie spełnia wymagań. Popraw.')

# Kod:
# if re.match('^[a-zA-Z0-9]{1}$', znak):
# sprawdza, czy znak pasuje do wzorca: dokładnie jeden znak z podanego zakresu znaków,
# zgodnych z wymaganiami zadania.

# sposób 2
suma = 0
# definuję zakres znaków dla cyfr, dużych i małych liter angielskich
znaki = list(range(48, 48 + 10)) + list(range(65, 65 + 26)) + list(
  range(97, 97 + 26))
while suma <= 550:
  znak = input('Podaj znak:')
  if ord(znak) in znaki:
    print('Znak odpowiedni.')
    print('Kod znaku=', ord(znak))
    suma += ord(znak)
    print('Aktualna suma =', suma)
  else:
    print('Znak nie spełnia wymagań. Popraw.')
