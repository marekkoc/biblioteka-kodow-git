# Ciągi niemalejące.
v = [1, 2, 4, 3, 6, 8, 7, 7, 8, 3, 4, 5, 6, 7, 1, 3, 9, 1, 0, 4, 2, 3, 6, 9]
for i in range(0, len(v) - 2):
  if (v[i] <= v[i + 1] <= v[i + 2]):
    print('Ciąg niemalejący:', v[i:i + 3])

print()

# Najdłuższy podciąg niemalejący.
for dlugosc in range(len(v), 0, -1):
  stop = False
  for od in range(0, len(v) - dlugosc):
    badany = v[od:od + dlugosc + 1]
    print('Badam ciąg:', badany)
    if all(map(lambda lewy, prawy: lewy <= prawy, badany[0::], badany[1::])):
      stop = True
      print('Znaleziony!', badany)
      break
  if stop: break
# W tym rozwiązaniu szukam najdłuższego ciągu spełniającego warunek, zaczynając od możliwie najdłuższego
# (cały v) i sprawdzając coraz krótsze podciągi. (Monitoruj wyświetlany wynik, by to zobaczyć).
# Fragment kodu
# if all(map(lambda lewy,prawy: lewy<=prawy, badany[0::], badany[1::])):
# jest kluczowy, gdyż wykorzystuję funkcję all(), map() oraz lambdę wg następującego pomysłu:
# Weź kolejne 2 sąsiednie elementy z badanego podciągu (badany) i sprawdź, czy dla
# wszystkich tych par, spełniony jest warunek, że lewy <= prawy. Jeżeli dla wszystkich,
# to jest to poszukiwany podciąg.
# Przykład. Mam podciąg [3, 4, 5, 6, 7]. Biorę więc 2 jego wersje, jedna identyczna (temp[0::])
# a druga zaczynająca się od następnego elementu [4, 5, 6, 7] (temp[1::]). Funkcja map()
# porównuje 3 i 4 (lewy i prawy) czy zachowują porządek <=. Następnie sprawdza pary: (4,5),
# (5,6), (6,7). Jeżeli za każdym razem zwrócona zostanie prawda, mapa zwróci zbiór prawd.
# Funkcja all() zwraca prawdę, gdy wszystkie elementy w przekazanym jej w argumencie zbiorze to prawda.
# Zatem ciąg prawd, to ciąg kolejnych oczekiwanych porządków pomiędzy sąsiednimi elementami.

# Ilość wystąpień każdej cyfry w wektorze.

# sposób 1
ilosci = [0] * 10  # 10 pozycji od 0 do 9, z wartością 0
for x in v:
  ilosci[x] += 1  # zliczam wystąpienia (+1) dla cyfry (x)
for i in range(0, len(ilosci)):
  print(f'Cyfra {i} wystąpiła {ilosci[i]} razy.')  # tylko prezentacja wyniku

print()
# sposób 2
for i in range(10):
  print(f'Cyfra {i} wystąpiła ', v.count(i), 'razy.')  # count() zlicza za mnie
