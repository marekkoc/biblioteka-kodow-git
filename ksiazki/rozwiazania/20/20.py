l1 = [3, 5, 6, 7, 3, 22, 1, 5, 7, 12]
l2 = []

# sposób 1
for a in l1:
  if a % 2 == 0: l2.append(a)  # najpierw parzyste
for a in l1:
  if a % 2 == 1: l2.append(a)  # potem nieparzyste

print(l1)
print(l2)

# sposób 2
l2.clear()
l2 = list(filter(lambda x: x % 2 == 0, l1))  # te z l1, które są parzyste
l2 += list(filter(lambda x: x % 2 == 1, l1))  # te z l1, które są nieparzyste
print(l1)
print(l2)
