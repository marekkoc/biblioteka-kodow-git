# sposób 1
start = 1
ile = 0
while ile < 100:
  od = 1
  for i in range(1, start + 1):
    print(start, end=' ')
    ile += 1
    if ile == 100: break
  start += 1
print()

# sposób 2
start = 1
ile = 0
while ile < 100:
  for x in (f' {start}' * start).strip().split():
    print(x, end=' ')
    ile += 1
    if ile == 100: break
  start += 1
# Linia zawierająca kod,
# for x in (f' {start}' * start).strip().split():
# skleja start-razy napis ' start'.
# Przykładowo, dla start=3 powstanie napis ' 3 3 3'.
# Z tak sklejonego pozbywa się początkowej spacji (strip()), zostaje '3 3 3'.
# Następnie dzieli napis po spacjach wewnątrz napisu (split()),
# dając listę [3,3,3]. Zmienna x wyświetla kolejne elementy z tej listy,
# za każdym wyświetleniem zwiększając zmienną ile, aby
# nie przekroczyć stu elementów ciągu.
print()

# sposób 3
start = 1
n = []
while len(n) < 100:
  if (n.count(start) < start):
    n.append(start)
  else:
    start += 1
print(*n)

# Linia kodu
# if (n.count(start) < start): n.append(start)
# dodaje liczbę start do listy n, o ile nie wystąpiła ona tyle razy, ile sama wynosi.
# Metoda count() wywołana na liście informuje nas, ile razy wystąpiła w niej pewna wartość.
# Metoda append() dodaje wartość na koniec listy.
