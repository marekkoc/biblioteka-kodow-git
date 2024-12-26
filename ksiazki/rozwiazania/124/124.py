def pierwszeZSita(N: int):
  liczby = list(range(2, N + 1))
  for poz in range(0, len(liczby)):
    if liczby[poz] != 0:  # 0 oznacza skreśloną liczbę
      yield liczby[poz]
      for skreslaj in range(poz + liczby[poz], len(liczby), liczby[poz]):
        liczby[skreslaj] = 0

# szuka par bliźniaczych i wyświetla
def pokazPary(pierwsze):
  ile = 0
  for poz in range(0, len(pierwsze) - 1):
    if (pierwsze[poz + 1] - pierwsze[poz] == 2):
      print('Para liczb bliźniaczych:', pierwsze[poz], pierwsze[poz + 1])
      ile += 1
  print('Par liczb bliźniaczych naliczono:', ile)

# test dla [2..50]
pokazPary(list(pierwszeZSita(50)))
print()
pokazPary(list(pierwszeZSita(1000)))
