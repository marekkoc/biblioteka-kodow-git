import os, re

class Kontener:
  def __init__(self, t=''):
    self.liczby = []
    if os.path.isfile(t):
      with open(t, 'r', encoding='utf-8') as f:
        self.tekst = ''.join(f)
    else:
      self.tekst = t

  def szukajLiczb(self):
    for x in re.findall('[\\+\\-]{0,1}[0-9]+[\\.,]{0,1}[0-9]*', self.tekst):
      x = x.replace(',', '.')
      if '.' in x:
        self.liczby.append(float(x))
      else:
        self.liczby.append(int(x))

k = Kontener('Rok 1984, w którym średni poziom IQ wynosił 110.44.')
k.szukajLiczb()
print(k.liczby)

k = Kontener('153_liczby_w_tekscie.txt')
k.szukajLiczb()
print(k.liczby)
