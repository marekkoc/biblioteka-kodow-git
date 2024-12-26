import json
from json import *

def load():
  """Ładowanie obiektów z pliku. Zwraca Listę obiektów klasy C."""
  L = []
  print('Rozpoczynam ładowanie:')
  with open(C.file, 'r', encoding='utf-8') as f:
    for ln in f:
      ln = ln.strip()
      L.append(C(*ln.split(':', 3)))  # maxsplit=3 pozwoli na ':' w C.s
  return L

def jsonLoad():
  """Ładowanie obiektów z pliku. Zwraca Listę obiektów klasy C."""
  L = []
  print('Rozpoczynam ładowanie:')
  with open(C.jsonFile, 'r', encoding='utf-8') as f:
    for ln in f:
      ln = ln.strip()
      L.append(C(*json.loads(ln)))
  return L

class C:
  # Klasa C
  file = 'obiektyKlasyC.txt'  # dane mojego pomysłu będą w tym pliku
  jsonFile = 'obiektyKlasyC.json'  # dane będą w tym pliku, jeżeli to będzie format JSON

  def __init__(self, seti: int = 0, setf: float = 0.0, setb: bool = True,
               sets: str = ''):
    """Konstruktor z 4 własnościami"""
    self.i = seti
    self.f = setf
    self.b = setb
    self.s = sets

  def save(self, type='w'):
    """Zapis obiektu do pliku. Domyślnie nowy plik."""
    with open(self.file, type, encoding='utf-8') as f:
      f.write(str(self.i) + ':')
      f.write(str(self.f) + ':')
      f.write(str(self.b) + ':')
      f.write(self.s + '\n')
    print('Zapis wykonany.')

  def append(self):
    """Dopisanie do pliku."""
    self.save(type='a')
    print('Dopisek wykonany')

  def __str__(self):
    """Pozwoli wyświetlać nasz obiekt klasy C"""
    return ('###' +
            str(self.i) + ' ' + str(self.f) + ' ' + str(self.b) + ' ' +
            str(self.s) + ' ' + '###')

  loadList = load  # w klasie C.loadList() uruchomi funkcję load
  loadJsonList = jsonLoad  # w klasie C.loadJsonList() uruchomi jsonLoad

  def jsonSave(self, type='w'):
    """Zapis obiektu do pliku. Domyślnie nowy plik."""
    temp = json.dumps([self.i, self.f, self.b, self.s])
    print(temp)
    with open(self.jsonFile, type, encoding='utf-8') as f:
      f.write(temp + '\n')
    print('Zapis wykonany.')

  def jsonAppend(self):
    """Dopisanie do pliku."""
    self.jsonSave(type='a')
    print('Dopisek wykonany')

o1 = C(10, 2.5, True, 'rabarbar:na:rowerze')
o2 = C(4, -5.5, False, 'marynowana rozwielitka')
o1.save()  # utworzy nowy plik, zapisze o1
o2.append()  # dopisze do pliku o2
print(*C.loadList(), sep='\n')  # załadunek i prezentacja dzięki __str__()

# wersje JSON

o3 = C(4, -2.0, True, 'kropla piasku')
o4 = C(-2, 200.01, False, 'błysk zimna')
o3.jsonSave()  # zapis
o4.jsonAppend()  # dopisanie
print(*C.loadJsonList(), sep='\n')  # załadunek i prezentacja dzięki __str__()
