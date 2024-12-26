def potegaIt(x: float, p: int):
  if x == 0 and p == 0:  # 0 do zerowej to symbol nieoznaczony, ale zwrócę 0
    print('Symbol nieoznaczony.')
    return 0;
  if p == 0:
    return 1;  # z definicji, cokolwiek niezerowego do zerowej potęgi to 1
  if x == 0:
    return 0;  # z definicji, zero do niezerowej potęgi to 0
  if p > 0:
    w = x
    for i in range(p - 1):
      x = x * w
    return x
  else:
    w = x
    for i in range(-p - 1):
      x = x * w
    return 1 / x

print(potegaIt(2, 8))
print(potegaIt(2, -8))

def potegaRek(x: float, p: int):
  if x == 0 and p == 0:  # 0 do zerowej to symbol nieoznaczony, ale zwrócę 0
    print('Symbol nieoznaczony.')
    return 0;
  if p == 0:
    return 1;  # z definicji, cokolwiek niezerowego do zerowej potęgi to 1
  if x == 0:
    return 0;  # z definicji, zero do niezerowej potęgi to 0
  if p > 0:
    return x * potegaRek(x, p - 1)
  else:
    return 1 / potegaRek(x, -p)

print(potegaRek(2, 8))
print(potegaRek(2, -8))
