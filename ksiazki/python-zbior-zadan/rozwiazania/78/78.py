def Int2Str(n: int):
  plus = True
  if n < 0: plus = False
  n = abs(n)
  cyfry = '0123456789'
  wynik = ''
  while n > 0:
    r = n % 10
    wynik = cyfry[r] + wynik
    n //= 10
  if wynik == '': return 0
  if plus:
    return wynik
  else:
    return '-' + wynik
  return wynik

print(Int2Str(10))
print(Int2Str(214))
print(Int2Str(0))
print(Int2Str(-990))
