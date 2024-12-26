a = float(input('Podaj liczbę a='))
b = float(input('Podaj liczbę b='))
znak = input('Podaj znak działania [+ - * /] : ')

# sposób 1
match znak:
  case '+':
    print(f'{a}{znak}{b} =', a + b)
  case '-' if (a - b != b - a):
    print(f'{a}{znak}{b} =', a - b)
    print(f'{b}{znak}{a} =', b - a)
  case '-' if (a - b == b - a):
    print(f'{a}{znak}{b} =', a - b)
  case '*':
    print(f'{a}{znak}{b} =', a * b)
  case '/' if a != 0 and b != 0 and a / b != b / a:
    print(f'{a}{znak}{b} =', a / b)
    print(f'{b}{znak}{a} =', b / a)
  case '/' if (a != 0 and b != 0 and a / b == b / a):
    print(f'{a}{znak}{b} =', a / b)
  case '/' if a == 0:
    print(f'{a}{znak}{b} =', a / b)
  case '/' if b == 0:
    print(f'{b}{znak}{a} =', b / a)
  case _:
    print('coś poszło nie tak!')  # np. wprowadzono głupi znak

# sposób 2

# Wykorzystuję funkcję eval() która interpretuje
# napis jak kod python'a do wykonania.
# Przykładowo eval('1+2') zwróci wartość 3.

def show(a, b, znak, double=False):
  print(f'{a}{znak}{b} =', eval(f'{a}{znak}{b}'))
  if double: print(f'{b}{znak}{a} =', eval(f'{b}{znak}{a}'))

match znak:
  case '+':
    show(a, b, znak)
  case '-' if (a - b != b - a):
    show(a, b, znak, True)
  case '-' if (a - b == b - a):
    show(a, b, znak)
  case '*':
    show(a, b, znak)
  case '/' if a != 0 and b != 0 and a / b != b / a:
    show(a, b, znak, True)
  case '/' if (a != 0 and b != 0 and a / b == b / a):
    show(a, b, znak)
  case '/' if a == 0:
    show(a, b, znak)
  case '/' if b == 0:
    show(b, a, znak)
  case _:
    print('coś poszło nie tak!')  # np. wprowadzono głupi znak
