with open('161.bin', 'r', encoding='utf-8') as f:
  for ln in f:
    print(ln.strip(), end='= ')
    suma = 0
    for znak in ln.strip():
      a = '{0:08b}'.format(ord(znak))
      suma += sum(map(lambda e: int(e, 2), (a[0:2], a[2:4], a[4:6], a[6:8])))
    print(suma)
