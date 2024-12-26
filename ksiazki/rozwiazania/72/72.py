L = []
N = ''
with open('72_dane.txt', encoding='utf-8') as f:
  for linia in f:
    if len(linia.strip()) == 0: continue  # pomijamy pustą
    x1, x2, x3, n = linia.split(';')
    print(x1, x2, x3)
    L.append(int(x1))
    L.append(int(x2))
    L.append(int(x3))
    N += n.strip()  # strip() usuwa białe znaki z początku i końca, zwraca kopię n
print(L, N, sep='\n')
