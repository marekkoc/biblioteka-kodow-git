plik = '88_dane.txt'

# sposób 1
def reduktor(s: str, ile=2):
  """Usuwa metodą 1) dla ile=2, metodą 2) dla ile=1"""
  if len(s) <= 1: return s  # za krótki, by usuwać
  for poz in range(0, len(s) - 1):
    if s[poz] == s[poz + 1]:
      return reduktor(s[0:poz:1] + s[poz + ile:], ile)
  return s

with open(plik, 'r', encoding='utf-8') as f:
  for l in f:
    l = l.strip()
    print('Rozpoczynam redukcję\n', l, '->\n', reduktor(l, 2))

print()

with open(plik, 'r', encoding='utf-8') as f:
  for l in f:
    l = l.strip()
    print('Rozpoczynam redukcję 2\n', l, '->\n', reduktor(l, 1))

# sposób 2 (wyrażenia regularne)
print()
print()

import re

def reduktorRegex(s: str, ile=2):
  """wzorzec r'(.)\1' znajduje znak i zaraz za nim taki sam znak"""
  if ile == 2:  # kasuję dwa identyczne znaki
    p, temp = re.subn(r'(.)\1', '', s, 1)
  elif ile == 1:  # zamieniam dwa identyczne na jeden
    p, temp = re.subn(r'(.)\1', r'\1', s, 1)
  if len(p) != len(s):
    return reduktorRegex(p, ile)
  else:
    return p

with open(plik, 'r', encoding='utf-8') as f:
  for l in f:
    l = l.strip()
    print('Rozpoczynam redukcję Regex\n', l, '->\n', reduktorRegex(l, 2))

print()

with open(plik, 'r', encoding='utf-8') as f:
  for l in f:
    l = l.strip()
    print('Rozpoczynam redukcję Regex 2\n', l, '->\n', reduktorRegex(l, 1))
