class Uczen:
  def __init__(self):
    self.imie = ''
    self.nazwisko = ''
    self.rokUr = 0
    self.m: bool  # mężczyzna (True), kobieta (False)
    self.zespol = ''
    self.nr = -1  # nr w dzienniku, -1 brak numeru

  def zTekstu(self, tekst):
    self.imie, self.nazwisko, self.rokUr, self.m, self.zespol = (
      tekst.strip().split(' '))

  def __lt__(self, other):
    alfabet = 'AaĄąBbCcĆćDdEeĘęFfGgHhIiJjKkLlŁłMmNnOoÓóPpRrSsŚśTtUuWwXxYyZzŹźŻż'
    for a, b in zip(self.kto, other.kto):
      if alfabet.find(a) < alfabet.find(b):
        return True
      elif alfabet.find(a) > alfabet.find(b):
        return False
    return len(a) < len(b)

  @property
  def kto(self):
    return self.nazwisko + self.imie

  def __repr__(self):
    plec = ''
    if self.m:
      plec = 'mężczyzna'
    else:
      plec = 'kobieta'
    return f'\n{self.nr}. {self.nazwisko} {self.imie} ({plec}), rok urodz. {self.rokUr}, klasa {self.zespol}'

  def __str__(self):
    return self.__repr__()

class Klasa:
  def __init__(self):
    self.uczniowie = []

  def __repr__(self):
    return ''.join(str(self.uczniowie)) + '\n\n'

  def __str__(self):
    return self.__repr__()

  def sortowanie(self):
    """
    Nadaje numer uczniom w klasie, sortuje ich po nazwisku i imieniu.
    Uwzględnia przy sortowaniu polską czcionkę.
    """
    self.uczniowie = sorted(self.uczniowie)
    for nr, u in enumerate(self.uczniowie):
      u.nr = nr + 1

  @staticmethod
  def zPliku(nazwaPliku):
    klasy = dict()  # {'1A':Klasa()}
    with open(nazwaPliku, 'r', encoding='utf-8') as f:
      for ln in f:
        u = Uczen()
        u.zTekstu(ln)
        klasy.setdefault(u.zespol, Klasa())
        klasy[u.zespol].uczniowie.append(u)
    return klasy

  def __iter__(self):
    for i in self.uczniowie:
      yield i

klasy = Klasa.zPliku('151_klasy.txt')
for kod, klasa in klasy.items():
  klasa.sortowanie()
  # prezentacja
  print('\n\nKlasa', kod)
  print(*klasa)
