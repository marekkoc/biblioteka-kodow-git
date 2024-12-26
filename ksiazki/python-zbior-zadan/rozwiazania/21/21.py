a, b, c, d, e = [int(x) for x in input('Podaj 5 liczb po spacji : ').split()]
# sposób 1
if a < b and b < c and c < d and d < e:
  print('Ok, ciąg jest rosnący.')
# sposób 2
if a < b < c < d < e:
  print('Ok, ciąg jest rosnący.')
