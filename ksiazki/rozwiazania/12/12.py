# sposób 1
for i in range(-25, 26):
  if i != 0:
    print(i, end=', ')

print()

# sposób 2 z napisem
wynik = []
for i in range(-25, 26):
  if i != 0:
    wynik.append(str(i))
print(', '.join(wynik))  # sklejam napisy z listy wynik przy pomocy ', '
