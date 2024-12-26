# Nie korzystamy z set() ale z list()
v1 = [1, 3, 5, 7, 9]
v2 = [1, 4, 7, 11, 15]
v3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 20]

# a)
a = []
for x in v1:
  for y in v2:
    if x == y and x not in a:
      a.append(x)
print('Część wspólna v1 i v2', a)

# b)
s = v1
for x in v2:
  if x not in s:
    s.append(x)  # s to suma v1+v2
b = []
for x in v3:
  if x not in s:
    b.append(x)
print('Różnica v3-(v1+v2)', b)

# c)
c = s
for x in v3:
  if x not in c:
    c.append(x)
print('Suma wszystkich v1+v2+v3', c)

# A teraz wersja ze zbiorami set().
v1 = {1, 3, 5, 7, 9}
v2 = {1, 4, 7, 11, 15}
v3 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 20}

# a)
print('Część wspólna v1 i v2', v1.intersection(v2))
# b)
print('Różnica v3-(v1+v2)', v3.difference(v1.union(v2)))
# c)
print('Suma wszystkich v1+v2+v3', v1.union(v2).union(v3))
