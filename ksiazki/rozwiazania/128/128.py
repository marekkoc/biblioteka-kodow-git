def czyLustrzana(n1: int, n2: int):
  return (str(n1)[::-1] == str(n2))

pary = set()
for a in range(2, 1001):
  for b in range(a + 1, 1001):
    if czyLustrzana(a, b): pary.add((a, b))

print(pary)
print('Ilość', len(pary))
