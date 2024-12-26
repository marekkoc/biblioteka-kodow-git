N = 22

K = list(range(1, N + 1))  # lista kulek zbioru K
print(K)  # liczby reprezentują kulkę i równocześnie różny kolor

# stworzę wszystkie możliwe kombinacje trójek dla zbioru K
wszystkie3dlaK = []
for poz1 in range(0, len(K)):
  for poz2 in range(poz1 + 1, len(K)):
    for poz3 in range(poz2 + 1, len(K)):
      wszystkie3dlaK.append(set((K[poz1], K[poz2], K[poz3])))
print(len(wszystkie3dlaK), wszystkie3dlaK)

wszystkie3dlaC = wszystkie3dlaK.copy()
print(len(wszystkie3dlaC), wszystkie3dlaC)

wszystkie_zdarzenia = 0
zdarzenia_z_powtorzonym_kolorem = 0

for k in wszystkie3dlaK:
  for c in wszystkie3dlaC:
    # Jeżeli część wspólna istnieje, to przynajmniej
    # jeden kolor musiał się powtórzyć (kulka o tym samym numerze/kolorze).
    if len(k.intersection(c)) > 0: zdarzenia_z_powtorzonym_kolorem += 1
    wszystkie_zdarzenia += 1

print(f'Zdarzenia z powtórzonym kolorem: {zdarzenia_z_powtorzonym_kolorem},'
      f' wszystkie zdarzenia {wszystkie_zdarzenia}')
print(
  f'Prawdopodobieństwo dla N=22 i x=3 '
  f'{zdarzenia_z_powtorzonym_kolorem / wszystkie_zdarzenia}')

"""
  Gdyby nie zabraniać korzystania ze wzorów, to:    
  Korzystając ze wzoru na kombinację, możliwych trójek jest 22!/3!*(22-3)!, 
  co daje 1540 kombinacji trzech kul.
  Ponieważ do worka mam wrzucić trzy dodatkowe kule z identycznego zbioru, ich też
  jest 1540, zatem wszystkich możliwych trójek kul z K i C w worku jest
  1540*1540. Spośród tych 2371600 przypadków sześciu kul trzeba wyłapać te,
  wśród których przynajmniej jedna para ma ten sam kolor. Rozwiązanie wyżej
  sprawdza wszystkie możliwe kombinacje i zlicza te, w których w worku 
  wystąpiły kulki o tych samych kolorach. (879340)
  
  Uwaga! Czy komputer policzyłby 22 silnia? (22!) Niektóre języki mogłyby
  mieć z tym problem. A Python? Sprawdźmy:
"""

def silnia_i(n):
  s = 1
  for i in range(2, n + 1):
    s *= i
  return s

print(silnia_i(22) / (silnia_i(3) * silnia_i(22 - 3)))  # 1540
