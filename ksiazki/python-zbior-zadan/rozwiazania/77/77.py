def czyMozliwyInt(kandydat: str):
  if kandydat[0] in ['-', '+']:
    znak = kandydat[0]
    kandydat = kandydat[1::]
  for i in kandydat:
    if i not in '0123456789':
      return False
  return True

def Str2Int(n: str):
  znak = ''
  if n[0] in ['-', '+']:
    znak = n[0]
    n = n[1::]
  L = 0
  d = 0
  if czyMozliwyInt(n):
    for i in n[::-1]:
      L += (ord(i) - 48) * 10 ** d
      d += 1
    if znak == '-':
      return -L
    else:
      return L
  else:
    print('Konwersja nie jest możliwa.')

print(Str2Int('178'))  # przykład 1
print(Str2Int('0222'))  # przykład 2
print(Str2Int('-123'))  # przykład 3
print(Str2Int('-0981'))  # przykład 4
