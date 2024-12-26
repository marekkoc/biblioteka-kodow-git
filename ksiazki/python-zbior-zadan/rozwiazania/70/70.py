L = []
with open('70_liczby.txt', encoding='utf-8') as f:
  for linia in f:
    print(linia.strip(), end=', ')
    if len(linia.strip()) == 0: continue
    L.append(int(linia.strip()))
print('\n', L)
