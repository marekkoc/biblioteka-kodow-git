L = []
with open('71_liczby.txt', encoding='utf-8') as f:
  for linia in f:
    if len(linia.strip()) == 0: continue
    a, b = linia.split(';')
    print(a, b.strip())
    L.append(int(a))
    L.append(int(b))

print(L)
