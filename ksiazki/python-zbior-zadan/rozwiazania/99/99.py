# wersja 1 z wykorzystaniem konwersji
def odwracanie(N):
  if N <= 0:
    return 'N>0!'
  return int(str(int(str(N)[::-1])))

# testy
print(123, odwracanie(123))
print(300, odwracanie(300))
print(3520, odwracanie(3520))
print(999, odwracanie(999))
print(0, odwracanie(0))

# wersja 2 bez zamiany na napisy
def odwracanie2(N):
  if N <= 0:
    return 'N>0!'
  zwracana = 0
  cyfry = []
  while N > 0:
    r = N % 10
    cyfry.append(r)
    N //= 10
  t = 0
  for c in cyfry[::-1]:
    if c == 0: continue
    zwracana += c * 10 ** t
    t += 1
  return zwracana

# testy
print()
print(123, odwracanie2(123))
print(300, odwracanie2(300))
print(3520, odwracanie2(3520))
print(999, odwracanie2(999))
print(0, odwracanie2(0))
