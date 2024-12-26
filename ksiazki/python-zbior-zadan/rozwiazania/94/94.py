from random import randint

def specjalnaLiczba():
  cyfry = '0123456789'
  gen = [''] * 10  # przyszła liczba, 10 cyfr
  while True:
    # pierwsza cyfra nie może być zerem
    gen[0] = cyfry[randint(1, 9)]
    # trzecia cyfra nie może być parzysta
    gen[2] = str([1, 3, 5, 7, 9][randint(0, 4)])
    # druga cyfra nie może być jak pierwsza i trzecia (już wylosowana)
    gen[1] = cyfry.replace(gen[0], '').replace(gen[2], '')[randint(0, 7)]
    # Poniższa pętla losuje cyfry poza pozycjami 0,1,2 i 9. Losuje tak,
    # by nie wylosować identycznej, jak cyfra wcześniej wylosowana
    for poz in [3, 4, 5, 6, 7, 8]:
      gen[poz] = cyfry.replace(gen[poz - 1], '')[randint(0, 8)]
    # ostatnia dowolna, bo 2 ostatnie mogą się powtórzyć
    gen[9] = cyfry[randint(0, 9)]
    # jeżeli suma cyfr jest mniejsza, zaczynamy od nowa
    if sum([int(c) for c in gen]) >= 30:
      return ''.join(gen)

# przykłądowe liczby
print(specjalnaLiczba(), specjalnaLiczba(), specjalnaLiczba())

# Wykonamy sobie testy dla 10000 liczb i spróbuję wykryć błąd, czyli niezgodność
# z treścią zadnia. Jeżeli poniższy kod nie wygeneruje komunikatu o błędzie,
# to znaczy, że reguły wymagane w zadaniu nie zostały naruszone.
for i in range(10000):
  n = specjalnaLiczba()
  if n[2] in [0, 2, 4, 6, 8]:
    print('Błąd! Trzecia cyfra jest parzysta.')
  if n[0] == 0:
    print('Błąd! Pierwsza cyfra jest zerem.')
  for poz in range(0, 8):
    if n[poz] == n[poz + 1]:
      print('Błąd! Znalazłem dwie sąsiednie identyczne cyfry (nie na końcu).', n)
  if sum([int(c) for c in n]) < 30:
    print('Błąd! Suma cyfr mniejsza od 30!')
