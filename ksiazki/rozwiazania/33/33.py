x = [2, 7, 1, 1, 4, 9, 3, 2, 1, 4, 1, 9, 6, 1, 3, 0, 1, 2, 3, 6, 8, 5, 6, 9, 3,
     0, 8, 1, 8, 8, 7, 0, 7, 8, 5, 0, 2, 2,
     3, 7, 1, 7, 2, 4, 7, 7, 5, 9, 0, 7, 7, 9, 2, 2, 2, 7, 0, 0, 5, 4, 6, 3, 9,
     3, 5, 1, 0, 0, 9, 2, 9, 2, 8, 5, 0, 8,
     5, 7, 0, 9, 6, 4, 9, 7, 8, 8, 6, 5, 4, 3, 2, 5, 8, 9, 4, 6, 8, 7, 9, 9]
# a)

# sposób 1 (kombinowany)
print('Sąsiednie liczby były identyczne:',
      len(list(
        filter(lambda x: x == True, map(lambda x, y: x == y, x[0:], x[1:])))),
      'razy.')

# sposób 2 (ręczny)
ile = 0
for poz in range(0, len(x) - 1):
  if x[poz] == x[poz + 1]:
    ile += 1
print('Sąsiednie liczby były identyczne:', ile, 'razy.')

# b)

# sposób 1
print('Sąsiednie liczby po zsumowaniu wyniosły 10:',
      len(list(filter(lambda x: x == True,
                      map(lambda x, y: x + y == 10, x[0:], x[1:])))), 'razy.')

# sposób 2
ile = 0
for poz in range(0, len(x) - 1):
  if x[poz] + x[poz + 1] == 10:
    ile += 1
print('Sąsiednie liczby po zsumowaniu wyniosły 10:', ile, 'razy.')
