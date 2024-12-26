def Palindrom(txt: str):
  return txt[0::] == txt[::-1]

kolumny = 20 * ['']
with open('83_dane.txt', 'r', encoding='utf-8') as f:
  print('Palindromy wierszowe:')
  for l in f:
    wiersz = l.strip()
    if Palindrom(wiersz):
      print(wiersz)
    for poz in range(0, len(wiersz)):
      kolumny[poz] += wiersz[poz]
  print('Palindromy kolumnowe (wyświetlone poziomo):')
  for k in kolumny:
    if Palindrom(k):
      print(k)
