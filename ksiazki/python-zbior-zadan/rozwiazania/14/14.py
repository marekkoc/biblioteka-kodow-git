stale = [3, 1, 2, 1]
wynik = []
for sto in range(0, 100):
  wynik.append(str(stale[sto % 4]))
print('Elementów', len(wynik))  # len zwraca ilość elementów listy, napisu itp.
print(' '.join(wynik))
