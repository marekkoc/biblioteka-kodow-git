plik = '84_kod.txt'

def kodowanie(s: str):
  with open(plik, 'w', encoding='utf-8') as f:
    for znak in s:
      f.write(str(ord(znak)) + ';')

napis = input('Podaj napis:')
kodowanie(napis)

def dekodowanie():
  slowo = ''
  wynik = ''
  with open(plik, 'r', encoding='utf-8') as f:
    slowo = f.readline()
  for kod in slowo.strip().split(';'):
    if len(kod):
      wynik += chr(int(kod))
  return wynik

print(dekodowanie())
