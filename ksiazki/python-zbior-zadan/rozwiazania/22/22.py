L = []
while True:
  L.append(float(input('Podaj liczbę: ')))
  if len(L) >= 2 and L[-1] == L[-2]: break

# Przypominam, że pozycje na listach można numerować od zera,
# idąc z lewej do prawej, oraz od -1 (zmniejszając) i idąc od prawej do lewej,
# gdzie indeks -1 to ostatnia pozycja ostatniego elementu.
'''
wartości:         [1, 5, 22]
pozycje z lewej:  [0, 1, 2 ]
pozycje z prawej: [-3,-2,-1]
'''
