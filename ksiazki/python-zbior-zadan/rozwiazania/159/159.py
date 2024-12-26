from random import random

LIMIT = 250000
dodajProcent = .53  # szansa na dodanie do kolejki

class Klient:
  licznik = 0

  def __init__(self):
    Klient.licznik += 1

kolejka = []  # lista wystarczy, by symulować kolejkę

# PRZYPADEK 1
print(f'Szansa na dodanie klienta do kolejki |'
      f' stosunek osób, które opuściły kolejkę do tych, które zostały:')
while round(dodajProcent, 2) <= .95:
  Klient.licznik = 0
  kolejka.clear()
  wejsc_do_petli_symulacji = 0
  opuscilo = 0
  while len(kolejka) < LIMIT:
    if random() <= dodajProcent:
      kolejka.append(Klient())
      wejsc_do_petli_symulacji += 1
    elif len(kolejka) > 0:
      kolejka.pop()
      opuscilo += 1
      wejsc_do_petli_symulacji += 1
    # Jeżeli szansa wskazała na opuszczenie kolejki, ale kolejka jest
    # pusta - nic się nie dzieje.
  print(f' {round(dodajProcent, 2)}|{round(opuscilo / len(kolejka), 2)}')
  dodajProcent += 0.01
