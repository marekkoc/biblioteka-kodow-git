dane = ['to tylko fantastyczna historia', 'nic tak nie cieszy jak upadek pychy',
        'error i rabarbar zawieraja 3 razy r']

class CezarMutant:
  alfabet = 'qwertyuiopasdfghjklzxcvbnm0123456789 '

  def __init__(self, tekst, klucz, modyfikator):
    self.tekst = tekst
    self.szyfrowany = ''
    self.klucz = klucz
    self.modyfikator = modyfikator
    self.szyfruj()

  def szyfruj(self):
    klucz_pomoc = self.klucz
    self.szyfrowany = self.tekst
    nowy = ''
    for znak in self.szyfrowany:
      poz = CezarMutant.alfabet.find(znak)
      if poz < 0:
        print('Niedopuszczalny znak', znak, 'spoza alfabetu.')
        return
      # szyfrowanie
      nowy += CezarMutant.alfabet[
        (poz + klucz_pomoc) % len(CezarMutant.alfabet)]
      klucz_pomoc += self.modyfikator
      klucz_pomoc %= len(CezarMutant.alfabet)
    self.szyfrowany = nowy

  def deszyfruj(self):
    klucz_pomoc = self.klucz
    odwrotny = CezarMutant.alfabet[::-1]
    nowy = ''
    for znak in self.szyfrowany:
      poz = odwrotny.find(znak)
      if poz < 0:
        print('Niedopuszczalny znak', znak, 'spoza alfabetu.')
        return
      # deszyfrowanie
      nowy += odwrotny[(poz + klucz_pomoc) % len(odwrotny)]
      klucz_pomoc += self.modyfikator
      klucz_pomoc %= len(odwrotny)
    self.szyfrowany = nowy
    return self.szyfrowany

for tekst in dane:
  print()
  print('-----------------SZYFROWANIE------------------')
  s = CezarMutant(tekst, 3, 1)
  print(f'k=3, m=1\n[{tekst}] => [{s.szyfrowany}]')
  s2 = CezarMutant(tekst, 5, 2)
  print(f'k=5, m=2\n[{tekst}] => [{s2.szyfrowany}]')
  print('-----------------DESZYFRACJA------------------')
  print(s.deszyfruj())
  print(s2.deszyfruj())
