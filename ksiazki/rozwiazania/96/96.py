dni = [31, 28] + [31, 30] * 2 + [31, 31] + [30, 31] * 2
dnip = [31, 29] + [31, 30] * 2 + [31, 31] + [30, 31] * 2
mies = ["styczeń", "luty", "marzec", "kwiecień", "maj", "czerwiec", "lipiec",
        "sierpień", "wrzesień", "październik", "listopad", "grudzień"]
dzien = ["poniedziałek", "wtorek", "środa", "czwartek", "piątek",
         "sobota", "niedziela"]

STARTOWY = 5  # index soboty na liście dzien

# Zasada: kiedy rok jest przestępny?
# Gdy rok jest podzielny przez 4, ale nie przez 100,
# lub gdy jest podzielny przez 400.
def przestepny(rok):
  return ((rok % 4 == 0 and rok % 100 != 0) or (rok % 400 == 0))

# ile dni w roku?
def ileDniMaRok(rok):
  if przestepny(rok): return 366
  return 365

# funkcja obliczająca tylko rok 2022
def dzienRoku2022(N: int):
  if (N < 1 or N > 365):  # zły numer
    return "funkcja działa w zakresie N<1;365>"
  d = ""
  m = 0  # początkowy miesiąc to styczeń mies[m]
  # obliczam jaki to dzień tygodnia w roku: dzien[nrd]
  nrd = (STARTOWY + N - 1) % 7
  for ile in dni:
    if N <= ile:
      d += str(N) + " " + mies[m] + " 2022 " + "(" + dzien[nrd] + ")"
      break
    else:
      N -= ile
      m += 1
  return d

print(dzienRoku2022(1))
print(dzienRoku2022(3))
print(dzienRoku2022(11))
print(dzienRoku2022(54))
print(dzienRoku2022(250))
print(dzienRoku2022(365))
print(dzienRoku2022(366))

# funkcja dla dowolnego roku >= 2022
def dzienRoku(rok: int, N: int):
  if rok < 2022:
    return "Funkcja działa tylko od roku 2022 włącznie."
  if (N < 1):
    return "Funkcja działa w zakresie N<1;365/366>"
  if przestepny(rok) and N > 366:
    return "rok " + str(rok) + ", funkcja działa w zakresie N<1;366>"
  if not przestepny(rok) and N > 365:
    return "rok " + str(rok) + ", funkcja działa w zakresie N<1;365>"
  d = ""
  # dla roku 2022 wykorzystam funkcję dzien_roku_2022, bo mogę :)
  if (rok == 2022):
    return dzienRoku2022(N)
  # Dla dalszych lat > 2022 obliczę, ile dni minęło od 2022-01-01 do końca
  # roku poprzedzającego rok przekazany do funkcji.
  ile_dni = 0
  for r in range(rok - 1, 2021, -1):
    ile_dni += ileDniMaRok(r)
  # dzień tygodnia zwracany przez funkcję dzien[nrd]
  nrd = (STARTOWY + ile_dni + N - 1) % 7
  m = 0
  pom = []
  if przestepny(rok):
    pom = dnip.copy()
  else:
    pom = dni.copy()
  for ile in pom:
    if N <= ile:
      d += str(N) + " " + mies[m] + " " + str(rok) + " " + "(" + dzien[
        nrd] + ")"
      break
    else:
      N -= ile
      m += 1
  return d

print(20 * '-')
print(dzienRoku(2022, 1))
print(dzienRoku(2022, 365))
print(dzienRoku(2023, 1))
print(dzienRoku(2023, 365))
print(dzienRoku(2024, 1))
print(dzienRoku(2024, 60))  # 29 luty 2024, czwartek
print(dzienRoku(2024, 366))
print(dzienRoku(2037, 57))
