N = []
suma = 0
with open('73_dane.txt', encoding='utf-8') as f:
  for linia in f:
    if len(linia) == 0: continue  # pomijamy pustą
    fragmenty = linia.split(';')
    for e in fragmenty:
      e = e.strip()
      # Można sprawdzać, czy e składa się tylko z cyfr i przecinka/kropki,
      # ale zastosuję inną sztuczkę.
      try:
        e = float(e)  # próba konwersji
        print(e, end=' ')  # wyświetlam wycięte liczby float
        suma += e
      except ValueError:
        N.append(
          '#' + e + '#')  # strip() usuwa białe znaki z początku i końca, zwraca kopię n
print()
print(N)
print('Suma', round(suma, 2))
