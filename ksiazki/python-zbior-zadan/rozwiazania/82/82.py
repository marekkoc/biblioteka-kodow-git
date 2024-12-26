import random as r

W = [
  ['ebb', 'cbe', 'beb', 'bdd', 'fcf', 'eed', 'bdd', 'cfd', 'cec', 'fee', 'ebf', 'cba', 'bff',
   'acf', 'aee'],
  ['ddc', 'eee', 'cac', 'cca', 'daa', 'cce', 'cbd', 'cad', 'afa', 'ced', 'fcc', 'cdd', 'cca',
   'cfc', 'afd'],
  ['dad', 'afb', 'bae', 'ffd', 'dba', 'efd', 'bac', 'dda', 'cca', 'beb', 'add', 'fba', 'bbe',
   'fbd', 'fab'],
  ['dfd', 'bcd', 'ecc', 'bfb', 'efb', 'cbb', 'dcf', 'afb', 'aaf', 'fcd', 'dee', 'dba', 'dca',
   'baa', 'cee'],
  ['fab', 'fba', 'efc', 'dad', 'caf', 'bad', 'dba', 'afa', 'fbd', 'cbf', 'ccb', 'fda', 'cff',
   'eac', 'bde'],
  ['efa', 'eac', 'ada', 'edd', 'fcd', 'fae', 'dff', 'cab', 'eab', 'dcc', 'dbd', 'bac', 'bfe',
   'efe', 'eec'],
  ['ccc', 'bcc', 'fbf', 'afa', 'abc', 'cde', 'fec', 'faa', 'bfe', 'cac', 'acd', 'dad', 'eca',
   'bbe', 'afd'],
  ['eba', 'abb', 'cfd', 'ccb', 'abc', 'def', 'ffc', 'ead', 'cdd', 'baf', 'bef', 'fbd', 'afb',
   'bae', 'bfe'],
  ['fcf', 'acf', 'bdc', 'baa', 'cdf', 'adf', 'edb', 'cab', 'ebe', 'faf', 'dee', 'ddc', 'ebd',
   'aad', 'eaa'],
  ['eee', 'aec', 'cbc', 'edd', 'bcf', 'fbb', 'acc', 'abf', 'dbc', 'cab', 'bcd', 'bbc', 'ebc',
   'fee', 'fcd'],
  ['cdc', 'cef', 'bfe', 'def', 'ede', 'ade', 'ade', 'dea', 'cbc', 'bce', 'bce', 'cad', 'fbb',
   'dbb', 'ccb'],
  ['feb', 'dba', 'afe', 'efa', 'add', 'aeb', 'bfc', 'bee', 'aca', 'acc', 'ebe', 'ead', 'ffa',
   'baa', 'eca'],
  ['eea', 'fcd', 'bdf', 'baf', 'fdb', 'fdb', 'ddd', 'bce', 'eed', 'edf', 'efc', 'fca', 'dff',
   'def', 'abc'],
  ['ebc', 'fcd', 'fad', 'cde', 'daf', 'eee', 'dfd', 'aaf', 'cff', 'dcc', 'aff', 'cfb', 'afc',
   'bcd', 'cde'],
  ['cca', 'afe', 'daf', 'ecf', 'cfd', 'cdb', 'bfe', 'aea', 'ffe', 'dae', 'bae', 'fce', 'ade',
   'bbc', 'fcd']]

SIZE = 15  # rozmiar

def trzyGenerator():
  znaki = 'abcdef'
  wynik = ''
  for ile in range(3):
    wynik += znaki[r.randint(0, len(znaki) - 1)]
  return wynik

def odpowiedni(s: str):
  if s in ['abc', 'bcd', 'cde', 'def']: return True
  return False

def testNaObszar(W, wiersz, kolumna):
  if (odpowiedni(W[wiersz][kolumna]) and odpowiedni(W[wiersz + 1][kolumna]) and
      odpowiedni(W[wiersz][kolumna + 1]) and
      odpowiedni(W[wiersz + 1][kolumna + 1])): return True
  return False

def szukajObszary(W):
  znaleziono = False
  for wiersz in range(0, SIZE - 1):
    for kolumna in range(0, SIZE - 1):
      if testNaObszar(W, wiersz, kolumna):
        print('Znaleziono dla w=', wiersz, 'k=', kolumna)
        print(W[wiersz][kolumna], W[wiersz][kolumna + 1])
        print(W[wiersz + 1][kolumna], W[wiersz + 1][kolumna + 1])
        znaleziono = True
  return znaleziono

print('Rozwiązania dla gotowego W:')
for w in W:
  print(w)

szukajObszary(W)

print('Szukam Rozwiązania dla losowego W:')
nieudane = 0
while True:
  W.clear()
  W = []
  for w in range(SIZE):
    n = []
    for k in range(SIZE):
      n.append(trzyGenerator())
    W.append(n.copy())
  if szukajObszary(W):
    for w in W:
      print(w)
    break
  else:
    nieudane += 1
print('Wykonano', nieudane,
      'losowań listy dwuwymiarowej W, zanim udało się odszukać w niej oczekiwanego obszaru.')
