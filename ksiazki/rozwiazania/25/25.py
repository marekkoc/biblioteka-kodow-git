V = []
while True:
  a = int(input('Podaj liczbę: '))  # krok 1
  V.append(a)
  a = int(input('Podaj liczbę: '))  # krok 2
  V.append(a)
  if (V[-1] * V[-2] < 1000):
    V.append(V[-1] * V[-2])
    print('Dodano iloczyn ', V[-1])
  else:
    print('Iloczyn przekroczył 1000.')
    break
print(V)
