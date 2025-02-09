---
Utworzono: 2025-02-09T13:09:00
Zmodyfikowano: 2025-02-09T13:09:00
Źródło: 
tags: 
Katalog:
---
# Co to jest parsowanie?


Parsowanie (ang. parsing) to proces analizy i przekształcania danych z jednego formatu na inny, zazwyczaj na format bardziej użyteczny dla programu. 

**Parsowanie ogólnie:**
- To proces "rozkładania" złożonych danych na prostsze elementy
- Analiza struktury danych i wyodrębnienie potrzebnych informacji
- Przekształcenie surowych danych w format, który program może łatwo wykorzystać

**Parsowanie stringów:**
To przekształcanie tekstu (ciągu znaków) na inne typy danych. Oto przykłady:

```python
# 1. Parsowanie stringów na liczby
tekst_liczba = "123"
liczba = int(tekst_liczba)  # parsowanie na int
print(type(liczba))  # <class 'int'>

# 2. Parsowanie stringów na liczby zmiennoprzecinkowe
tekst_float = "123.45"
liczba_float = float(tekst_float)  # parsowanie na float
print(type(liczba_float))  # <class 'float'>

# 3. Parsowanie daty i czasu
from datetime import datetime

tekst_data = "2024-03-15 14:30"
data = datetime.strptime(tekst_data, "%Y-%m-%d %H:%M")
print(type(data))  # <class 'datetime.datetime'>

# 4. Parsowanie listy liczb rozdzielonych przecinkami
tekst_lista = "1,2,3,4,5"
lista = [int(x) for x in tekst_lista.split(",")]
print(lista)  # [1, 2, 3, 4, 5]

# 5. Parsowanie danych JSON
import json

tekst_json = '{"imie": "Jan", "wiek": 30}'
dane = json.loads(tekst_json)
print(type(dane))  # <class 'dict'>
print(dane["imie"])  # Jan

# 6. Parsowanie argumentów wiersza poleceń
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--imie", type=str, help="Podaj imię")
args = parser.parse_args()
```

**Częste przypadki użycia parsowania:**
1. Przetwarzanie plików konfiguracyjnych
2. Odczytywanie danych z formularzy
3. Przetwarzanie danych z API
4. Analiza logów
5. Przetwarzanie danych wejściowych od użytkownika

**Przykład praktyczny - parsowanie pliku CSV:**
```python
import csv

# Przykładowy plik CSV z danymi pracowników
csv_text = """imie,stanowisko,pensja
Jan,Programista,5000
Anna,Designer,4500"""

# Parsowanie CSV na listę słowników
pracownicy = []
for row in csv.DictReader(csv_text.splitlines()):
    # Parsowanie pensji ze stringa na int
    row['pensja'] = int(row['pensja'])
    pracownicy.append(row)

print(pracownicy)
# [
#     {'imie': 'Jan', 'stanowisko': 'Programista', 'pensja': 5000}, 
#     {'imie': 'Anna', 'stanowisko': 'Designer', 'pensja': 4500}
# ]
```

**Dlaczego parsowanie jest ważne:**
6. Pozwala na konwersję danych do odpowiedniego formatu
7. Umożliwia walidację danych wejściowych
8. Ułatwia pracę z różnymi formatami danych
9. Pomaga w komunikacji między różnymi systemami
10. Jest kluczowe w przetwarzaniu danych wejściowych od użytkownika
