# Niebezpieczeństwo! BLOB tu jest!
# sposób 1
w1 = 1  # przy 1 okrążeniu
w2 = 1  # przy 2 okrążeniu
w = 0
print(w1, w2, end=' ')
for okrazenie in range(3, 14):
  w = w1 + w2
  print(w, end=' ')
  w1 = w2
  w2 = w
print()
print('Oto waga po 13 dniach:', w)

# sposób 2

# Tak. To ciąg Fibonacciego. Wcześniejsze rozwiązanie jest iteracyjne, przy pomocy pętli.
# Można jednak skorzystać z funkcji i stworzyć rozwiązanie rekurencyjne.

def BlobFibonacciego(okrazenia):
  if okrazenia in (1, 2): return 1
  return BlobFibonacciego(okrazenia - 1) + BlobFibonacciego(okrazenia - 2)

print()
print('Oto waga po 13 dniach:', BlobFibonacciego(13))
