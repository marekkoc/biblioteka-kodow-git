import time

kolory = {'reset': "\033[0m", 'bgred': "\033[101m", 'bggreen': "\033[102m",
          'bgyellow': "\033[103m"}
paliki = {'A': [], 'B': [], 'C': []}  # {'A':[stos krążków], ... }

def start(ile_krazkow: int = 3):
  # górny krążek to 1, dolny to ile_krazkow
  # koniec listy to jakby wierzchołek palika
  for i in range(ile_krazkow, 0, -1):
    paliki['A'].append(i)

def pokaz():
  poziom = max(len(paliki['A']), len(paliki['B']), len(paliki['C']))
  for i in range(poziom, 0, -1):
    for p in ('A', 'B', 'C'):
      if len(paliki[p]) >= i:
        print(paliki[p][i - 1], '\t', sep='', end='')
      else:
        print(' \t', end='')
    print()
  print(kolory['bgred'], 'A\tB\tC', kolory['reset'], sep='')

def hanoi(n, A='A', B='B', C='C'):
  if n > 0:
    hanoi(n - 1, A, C, B)
    # ruch z A na C
    time.sleep(1)
    paliki[C].append(paliki[A][-1])
    paliki[A].pop()
    print(kolory['bggreen'], 'KROK ', hanoi.i, kolory['reset'], sep='')
    hanoi.i += 1
    pokaz()
    hanoi(n - 1, B, A, C)

start(4)
pokaz()
hanoi.i = 1
hanoi(4, 'A', 'B', 'C')
