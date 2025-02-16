---
Utworzono: 2025-02-15T10:33:00
Zmodyfikowano: 2025-02-15T10:33:00
Źródło: Claude
tags: 
Katalog:
---

Nie, metoda statyczna i metoda klasowa w Pythonie to nie to samo. Pozwól, że wyjaśnię różnice na przykładach:

```python
class Kalkulator:
    mnoznik = 2

    # Metoda statyczna - nie ma dostępu ani do klasy, ani do instancji
    @staticmethod
    def dodaj(a, b):
        return a + b
    
    # Metoda klasowa - ma dostęp do klasy poprzez parametr cls
    @classmethod
    def pomnoz(cls, liczba):
        return liczba * cls.mnoznik

# Użycie:
print(Kalkulator.dodaj(2, 3))      # 5
print(Kalkulator.pomnoz(5))        # 10
```

Główne różnice:
1. Metoda statyczna (@staticmethod):
   - Nie otrzymuje automatycznie żadnego pierwszego parametru
   - Nie ma dostępu ani do klasy, ani do instancji
   - Jest jak zwykła funkcja, tylko zgrupowana w przestrzeni nazw klasy
   - Używana głównie do operacji pomocniczych niezwiązanych ze stanem klasy

2. Metoda klasowa (@classmethod):
   - Otrzymuje automatycznie referencję do klasy jako pierwszy parametr (conventionally named `cls`)
   - Ma dostęp do atrybutów klasy i może je modyfikować
   - Może być używana do tworzenia alternatywnych konstruktorów
   - Dziedziczy się w podklasach i zachowuje kontekst aktualnej klasy

Praktyczny przykład alternatywnego konstruktora:

```python
class Data:
    def __init__(self, rok, miesiac, dzien):
        self.rok = rok
        self.miesiac = miesiac
        self.dzien = dzien

    @classmethod
    def z_tekstu(cls, data_tekst):
        rok, miesiac, dzien = map(int, data_tekst.split('-'))
        return cls(rok, miesiac, dzien)

    @staticmethod
    def czy_przestepny(rok):
        return rok % 4 == 0 and (rok % 100 != 0 or rok % 400 == 0)

# Użycie:
data1 = Data(2024, 2, 15)
data2 = Data.z_tekstu("2024-02-15")  # alternatywny konstruktor jako metoda klasowa
print(Data.czy_przestepny(2024))      # True - metoda statyczna sprawdza tylko rok
```

W tym przykładzie:
- `z_tekstu` jest metodą klasową, bo potrzebuje dostępu do klasy, aby utworzyć nową instancję
- `czy_przestepny` jest metodą statyczną, bo wykonuje tylko obliczenia na przekazanym roku, nie potrzebuje dostępu do klasy ani instancji