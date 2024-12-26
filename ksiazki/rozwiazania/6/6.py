# sposób 1
ilep = 0
ilenp = 0
for a in [int(x) for x in
          input('Podaj 5 wartości oddzielonych spacją: ').split()]:
  if a % 2 == 0:
    ilep += 1
  else:
    ilenp += 1
print('Parzystych ', ilep, '\nNieparzystych', ilenp)

# sposób 2
n = [int(x) for x in input('Podaj 5 wartości oddzielonych spacją: ').split()]
ilenp = sum(map(lambda x: x % 2, n))  # czary!
print('Nieparzystych', ilenp, '\nParzystych', 5 - ilenp)

# Drugi sposób najpierw wkłada do n listę 5-ciu liczb.
# Następnie funkcja map() stosuje lambdę (funkcję anonimową)
# lambda x : x%2
# na elementach listy n, reprezentowanych po kolei przez zmienną x.
# map(lambda x: x%2, n)
# Funkcja map() zwraca zbiór wyników, którymi są kolejno albo jedynki, albo zera.
# Jedynki są wtedy, gdy liczba x
# jest nieparzysta. Następnie zbiór ten podany jest jako argument do funkcji sum(),
# sum(map(lambda x: x%2,n))
# która sumuje jego elementy. W praktyce sumuje ilość jedynek, czyli liczb nieparzystych.
# A tę sumę zapamiętujemy w ilenp. Reszta jest już oczywista ;)
