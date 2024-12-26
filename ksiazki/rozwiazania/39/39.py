znaki = ['x', 'P', 'Q', '4', '\n', '%', 'u', '@', 'e', 'T', 'B', '$', '!', ':', '"', '1', '<',
         'd', 'k', 'L', '$', ')', '$', 'B', 'x', 'w', 'q', 'P', 'c', 'X', 'B', '>', '?', '[',
         'r', 'x', '$', '#', '}', '|', 'd', 'l', 'n', 'b', 'V', '!']
di = dict()
for znak in znaki:
  if not znak in di:
    di[znak] = 1
  else:
    di[znak] += 1  # znaki zliczone!
suma = 0
for z, ile in di.items():
  if z in '1234567890': suma += int(z)
  if ile > 1 and z != znaki[0] and z != znaki[-1]:
    print(z)  # te się powtarzają, ale nie wystąpiły na początku i na końcu.
print('Suma znaków będących cyframi:', suma)
