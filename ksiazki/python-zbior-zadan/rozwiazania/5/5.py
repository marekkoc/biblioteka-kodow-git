a1, a2, a3, a4, a5 = [float(x) for x in
                      input('Podaj 5 wartości oddzielonych spacją: ').split()]
if (a5 == 0):
  print(f'To się nie uda, a5={a5} uniemożliwia dzielenie.')
else:
  print(f'Wynik to =>', (((a1 + a2) * a3) - a4) / a5)
