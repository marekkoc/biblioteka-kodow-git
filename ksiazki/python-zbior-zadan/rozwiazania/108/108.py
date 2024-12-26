from random import randint

# Zdarzenie: Opad. Zawiera zapis sekund od ostatniego opadu
# i ilość sztuk, która opadła.
class Opad:
  def __init__(self, sekunda, sztuk):
    self.sekunda = sekunda
    self.sztuk = sztuk

  # generuje losowe, jednostkowe zdarzenie opadu
  @staticmethod
  def opad():
    # ile sekund upłynęło od ostatniego opadu
    sek = randint(1, 10)
    szansa = randint(1, 100)
    sztuk = 0
    if szansa <= 50:
      sztuk = randint(0, 3)
    elif szansa <= 80:
      sztuk = randint(4, 7)
    else:
      sztuk = randint(8, 10)
    return Opad(sek, sztuk)

  def __str__(self):
    return 'Opad po ' + str(self.sekunda) + ' sekundach. Sztuk ' + str(
      self.sztuk)

class Drzewo:
  def __init__(self):
    self.sztuk = 3000
    self.czas_opadania = 0
    self.opadanie = []  # tu będą zdarzenia (opady), obiekty klasy Opad

  def zdarzenie(self):
    o = Opad.opad()
    if self.sztuk < o.sztuk:  # nie może spaść tyle liści
      o.sztuk = self.sztuk
    self.sztuk -= o.sztuk  # drzewo gubi liście
    self.czas_opadania += o.sekunda
    self.opadanie.append(o)

  def symulacja(self, show=True):
    while self.sztuk > 0:
      self.zdarzenie()
      if show:
        print(
          f'Po {self.czas_opadania} sekundach pozostało {self.sztuk} liści.')

# start symulacji, gromadzenie danych
drzewo = Drzewo()
drzewo.symulacja(False)  # daj True, by zobaczyć opadanie

# Po jakim czasie (podaj w godzinach, minutach i sekundach) drzewo straciło wszystkie liście?
print(drzewo.czas_opadania, ' -> w sekundach, czyli:')
g = drzewo.czas_opadania // 3600
m = (drzewo.czas_opadania - (g * 3600)) // 60
s = drzewo.czas_opadania - g * 3600 - m * 60
print(f'{g} godz., {m} min. i {s} sek.')

# Jaki procent opadania stanowiły opady zawierające od 0 do 3 liści?
maks = len(drzewo.opadanie)
ile0_3 = len(list(filter(lambda opad: opad.sztuk <= 3, drzewo.opadanie)))
# Jeżeli symulacja jest prawidłowa, procent powinien oscylować w granicach 50%
print('Procent zdarzeń opadania od 0 do 3 liści = ', ile0_3 / maks * 100, '%')

# Ile razy w krokach symulacji nie spadł ani jeden liść? (losowało się 0 liści)
# Powinna to być 1/4 z około 50%, czyli okolice 12,5% (uruchom symulację
# kilkukrotnie, by zobaczyć wyniki - powinny oscylować w podanych wartościach)
ile0 = len(list(filter(lambda opad: opad.sztuk == 0, drzewo.opadanie)))
print('Procent zdarzeń w których nie spadł ani jeden liść = ',
      ile0 / maks * 100, '%')

# Przyjmij, że ponumerowaliśmy kolejne kroki symulacji (zdarzenie opadania).
# Znajdź 10 kolejnych (następujących po sobie) kroków, dla których
# spadło najmniej liści. Podaj numery tych kroków.
zakres = 10
najmniej = 10 * 10;  # w 10 krokach nie mogło spaść więcej liści
start = 0
for poz in range(0, len(drzewo.opadanie) - zakres + 1):
  spadlo = 0
  for i in range(poz, zakres + poz):
    spadlo += drzewo.opadanie[i].sztuk
  if najmniej > spadlo:
    najmniej = spadlo
    start = poz
print('Najmniej liści w 10 krokach, bo', najmniej, 'spadło od kroku', start,
      'do kroku', start + zakres - 1)
print('Oto te dziesięć opadów:')
for i in range(start, start + zakres):
  print(drzewo.opadanie[i])
