ile = 0
pom = 0
for i in range(1, 121):
  if i % 55 != 0:
    ile += 1
    print(i, end=' ')
  else:
    pom += 1
print()
print('Wyświetlone', ile)
print('Pominięte', pom)
