import operator

class Agent:
  def __init__(self, numer, um, wyn):
    wyn = [int(w) for w in wyn]
    self.numer = numer
    self.wyniki = dict(zip(um, wyn))

  def __str__(self):
    st = self.numer + ':\n'
    for u, w in self.wyniki.items():
      st += '\t' + u + ' := ' + str(w) + '\n'
    return st + '\n'

  def wynik(self, umiejetnosc):
    return self.wyniki[umiejetnosc]

  def intModyfikator(self):
    return self.wyniki['inteligencja'] // 10

  def zwieksz(self, u, ileLat=1):
    self.wyniki[u] += self.intModyfikator() * ileLat

dane = dict()
with open('114_wyniki.txt', 'r', encoding='utf-8') as f:
  naglowki = f.readline().strip().split(',')
  a, umiejetnosci = naglowki[0], naglowki[1:]
  for ln in f:
    agent = ln.strip().split(',')
    numer, wyniki = agent[0], agent[1:]
    dane[numer] = Agent(numer, umiejetnosci, wyniki)

# Podaj listę osób (nazwa/numer agenta) o 10 najlepszych wynikach z pływania.
najPływ = dict()
for k, ag in dane.items():
  najPływ[ag.numer] = ag.wynik('pływanie')
najPływ = dict(
  sorted(najPływ.items(), key=operator.itemgetter(1), reverse=True))

print('Najlepsi pływacy (10 wyników):')
naj = set()
for ag, um in najPływ.items():
  naj.add(um)
  if len(naj) > 10: break
  print(ag, um)

# Z którą umiejętnością agenci radzą sobie najlepiej
# (analizuj arytmetyczną średnią punktów wszystkich
# agentów dla każdej umiejętności)?
srednie = dict()
for k, ag in dane.items():
  for u in umiejetnosci:
    srednie.setdefault(u, 0)
    srednie[u] += ag.wynik(u)
maks = 0
for u in umiejetnosci:
  srednie[u] /= len(dane)
  if maks < srednie[u]: maks = srednie[u]

srednie = dict(
  sorted(srednie.items(), key=operator.itemgetter(1), reverse=True))
print('Uśredniając umiejętności wszystkich, agenci najlepiej radzą sobie z:')
for u, s in srednie.items():
  if s == maks:
    print(u, s)
  else:
    break

# Wyświetl listę osób, które uzyskały najgorszy wynik z zakresu
# danej umiejętności (najgorszą osobę w pływaniu, najgorszą osobę
# w strzelaniu itd.). Jeżeli najgorszy wynik w danej kategorii
# osiągnęło więcej osób, pokaż je wszystkie.
analiza = dict()  # {umiejętność: { wartość: ['agent1','agent2'] }, ... }
for k, ag in dane.items():
  for u in umiejetnosci:
    analiza.setdefault(u, dict())
    analiza[u].setdefault(ag.wynik(u), [])
    analiza[u][ag.wynik(u)].append(ag.numer)
for u in umiejetnosci:
  analiza[u] = dict(sorted(analiza[u].items()))
  print(u, 'wartość=', list(analiza[u].items())[0][0], '.\tAgenci:',
        *list(analiza[u].items())[0][1])

# Przedstaw uporządkowane listy agentów od najlepszego do najgorszego
# dla wspinaczki, hakowania i wiedzy.
for u in ['wspinaczka', 'hakowanie', 'wiedza']:
  analiza[u] = dict(sorted(analiza[u].items(), reverse=True))
  print()
  print('Lista agentów. Umiejętność: ', u, '.')
  for v, agenci in analiza[u].items():
    print(v, ' => ', agenci)

'''
Przyjmij, że inteligencja wpływa na tempo rozwoju takich umiejętności jak 
hakowanie i wiedza. Inteligencja jest niezmienna. Każde 10 punktów 
inteligencji powoduje rokroczny wzrost hakowania i wiedzy agenta o 1 punkt. 
Przykładowo, dla inteligencji wynoszącej 24 punkty, hakowanie i wiedza 
wzrosną po roku każda o 2 punkty. Ile wyniesie hakowanie każdego 
z agentów w 2030 roku? Na ile punktów zostanie obliczona wiedza 
agentów w 2040 roku?
'''
print('\nHakowanie w 2030:')
for a, ag in dane.items():
  ag.zwieksz('hakowanie', 10)
  print(a, 'Hakowanie:', ag.wynik('hakowanie'))

print('\nWiedza w 2040:')
for a, ag in dane.items():
  ag.zwieksz('wiedza', 20)
  print(a, 'Wiedza:', ag.wynik('wiedza'))
