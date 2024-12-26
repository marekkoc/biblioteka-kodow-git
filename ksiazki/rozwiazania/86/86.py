# funkcja sprawdza, czy liczby w L na pozycjach od pocz do kon włącznie są takie same?
def takie_same(L, pocz, kon):
  if len(L[pocz:kon + 1]) == L[pocz:kon + 1].count(L[pocz]):
    return True
  return False

# funkcja szukająca i wyświetlająca podciągi wraz z pozycjami
def szukaj(L):
  for dlugosc in range(len(L), 1, -1):
    for i in range(0, len(L) - dlugosc + 1):
      if takie_same(L, i, i + dlugosc - 1):
        for s in range(i, i + dlugosc):
          print(L[s], end=' ')
        print('od pozycji', i, 'do pozycji', i + dlugosc - 1)

L = [3, 2, 1, 1, 4, 2, 4, 4, 4]
szukaj(L)
L = [0, 0, 0]
szukaj(L)
