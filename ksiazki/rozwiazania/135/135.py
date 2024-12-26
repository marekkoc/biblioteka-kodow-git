def dzialanie(x: float, y: float, d: str):
  if d == '+':
    return x + y
  elif d == '-':
    return x - y
  elif d == '*':
    return x * y
  elif d == '/':
    if y != 0.0: return x / y
    print('Nie dzielimy przez 0!')
    return 0
  else:
    print('Operacja', d, 'nierozpoznana!')

elementy = []
operandy = []  # posłuży jako stos operandów
with open('135_wyrazenia_onp.txt', 'r', encoding='utf-8') as f:
  for wyr in f:
    if len(wyr) == 0: continue
    print('Obliczanie:', wyr, end='')
    elementy.clear()  # lista kolejnych elementów wyrażenia
    operandy.clear()
    elementy = [x.strip() for x in wyr.split(' ')]
    for e in elementy:
      try:
        x = float(e)  # liczba! o ile uda się konwersja
        operandy.append(x)
      except:
        # e to operator
        b = operandy.pop()
        a = operandy.pop()
        operandy.append(dzialanie(a, b, e))
    print('=>', operandy.pop())
