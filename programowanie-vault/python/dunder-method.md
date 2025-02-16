---
Utworzono: 2024-10-30T09:51:00
Zmodyfikowano: 2025-02-15T09:51:00
Źródło: chatGPT
tags:
  - "#dunder-method"
---
#metody-magiczne  #magic-method

Dunder methods, znane również jako "**metody magiczne**" w Pythonie, to specjalne metody, które mają **podwójne podkreślenia** na początku i końcu nazwy, np. `__init__`, `__str__`, `__len__`. Skrót "dunder" pochodzi od *double underscore* (podwójnego podkreślenia). Te metody pozwalają na **specjalne zachowanie obiektów** i pozwalają na dostosowanie wbudowanych funkcji i operatorów do własnych potrzeb.

### Najważniejsze dunder methods:
- **`__init__`**: Konstruktor klasy, wywoływany podczas tworzenia nowego obiektu, np. `MyClass()`.
- **`__str__`**: Reprezentacja tekstowa obiektu zwracana przez `str()`, często używana do czytelnego wyświetlania obiektów.
- **`__repr__`**: Reprezentacja obiektu używana w `repr()`, zwraca bardziej szczegółowy opis obiektu, przydatna w debugowaniu.
- **`__len__`**: Zwraca długość obiektu, co pozwala na użycie `len()` na obiekcie.
- **`__getitem__`**, **`__setitem__`**: Pozwalają na dostęp do elementów za pomocą notacji `[]` (np. obiekt może działać jak lista lub słownik).
- **`__call__`**: Umożliwia wywołanie obiektu jak funkcji (np. `my_obj()`).
  
Dunder methods umożliwiają tworzenie czytelniejszego, bardziej "pythonicznego" kodu przez integrację obiektów z wbudowanymi funkcjami Pythona oraz operacjami na obiektach.

# metody magiczne - wyjaśnienie 2

Oto przykład implementacji klasy `Vector`, która korzysta z różnych metod "dunder" (magic methods), by dostosować działanie typowych operacji na wektorach, takich jak dodawanie, mnożenie skalarne, wyznaczanie długości wektora czy porównywanie wektorów.

### Przykład klasy `Vector` z metodami dunder:

```python
import math

class Vector:
    def __init__(self, x, y):
        # Konstruktor (inicjalizuje współrzędne wektora)
        self.x = x
        self.y = y
    
    def __str__(self):
        # Czytelna reprezentacja wektora dla użytkownika
        return f"Vector({self.x}, {self.y})"
    
    def __repr__(self):
        # Szczegółowa reprezentacja obiektu (dla debugowania)
        return f"Vector(x={self.x}, y={self.y})"
    
    def __add__(self, other):
        # Dodawanie dwóch wektorów (Vector + Vector)
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented
    
    def __mul__(self, scalar):
        # Mnożenie wektora przez skalar (Vector * scalar)
        if isinstance(scalar, (int, float)):
            return Vector(self.x * scalar, self.y * scalar)
        return NotImplemented
    
    def __rmul__(self, scalar):
        # Mnożenie skalara przez wektor (scalar * Vector)
        return self.__mul__(scalar)
    
    def __len__(self):
        # Długość wektora dla funkcji len()
        return int(math.sqrt(self.x ** 2 + self.y ** 2))
    
    def __eq__(self, other):
        # Sprawdza, czy dwa wektory są równe (Vector == Vector)
        return self.x == other.x and self.y == other.y
    
    def __getitem__(self, index):
        # Umożliwia dostęp do współrzędnych wektora za pomocą indeksów (v[0] i v[1])
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError("Vector index out of range")

    def __call__(self):
        # Pozwala wywołać obiekt wektora jak funkcję, np. v()
        return (self.x, self.y)
    
    def __abs__(self):
        # Zwraca długość wektora (dla funkcji abs())
        return math.sqrt(self.x ** 2 + self.y ** 2)

# Przykłady użycia klasy Vector
v1 = Vector(3, 4)
v2 = Vector(1, 2)

# Wywołanie __str__
print(v1)                 # Vector(3, 4)

# Wywołanie __repr__
print(repr(v1))           # Vector(x=3, y=4)

# Dodawanie dwóch wektorów
v3 = v1 + v2               # Vector(4, 6)
print(v3)

# Mnożenie przez skalar
v4 = v1 * 3                # Vector(9, 12)
print(v4)

# Sprawdzenie długości wektora przez len()
print(len(v1))             # 5 (zaokrąglone do liczby całkowitej)

# Sprawdzenie równości
print(v1 == v2)            # False

# Wywołanie wektora jak funkcji
print(v1())                # (3, 4)

# Uzyskanie współrzędnych za pomocą indeksów
print(v1[0])               # 3
print(v1[1])               # 4

# Wyznaczanie długości wektora przez abs()
print(abs(v1))             # 5.0
```

### Opis użytych metod:

1. **`__init__`**: Inicjalizuje współrzędne wektora.
2. **`__str__`**: Reprezentacja tekstowa wektora, przydatna przy wyświetlaniu.
3. **`__repr__`**: Dokładna reprezentacja do debugowania.
4. **`__add__`**: Dodawanie dwóch wektorów.
5. **`__mul__`** i **`__rmul__`**: Mnożenie przez skalar (w obu kierunkach).
6. **`__len__`**: Wyznaczanie długości wektora jako liczby całkowitej.
7. **`__eq__`**: Porównanie wektorów.
8. **`__getitem__`**: Uzyskiwanie dostępu do współrzędnych wektora za pomocą indeksu.
9. **`__call__`**: Wywoływanie obiektu wektora jak funkcji, co zwraca współrzędne jako krotkę.
10. **`__abs__`**: Zwracanie długości wektora w stylu funkcji `abs()`.

### Działanie i zalety
Te metody sprawiają, że klasa `Vector` zachowuje się intuicyjnie i „naturalnie” w kodzie. Można dodawać wektory, porównywać je, a także wygodnie wyświetlać, co znacząco ułatwia korzystanie z obiektu klasy.


Chętnie wyjaśnię metody magiczne w Pythonie. Są to specjalne metody, które pozwalają na dostosowanie zachowania obiektów klasy.

Metody magiczne są otoczone podwójnymi podkreślnikami (__) i są wywoływane automatycznie w określonych sytuacjach. Oto najważniejsze z nich:

Inicjalizacja i tworzenie obiektów:
```python
class Przykład:
    def __init__(self, wartość):  # Konstruktor, wywoływany przy tworzeniu obiektu
        self.wartość = wartość
        
    def __new__(cls, *args):      # Kontroluje tworzenie nowej instancji
        return super().__new__(cls)
        
    def __del__(self):            # Wywoływana przy usuwaniu obiektu
        print("Obiekt usunięty")
```

Reprezentacja obiektu:
```python
class Liczba:
    def __init__(self, x):
        self.x = x
    
    def __str__(self):            # Czytelna reprezentacja dla użytkownika
        return f"Liczba: {self.x}"
        
    def __repr__(self):           # Techniczna reprezentacja dla programisty
        return f"Liczba({self.x})"
```

Operatory matematyczne:
```python
class Wektor:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):     # Dodawanie: v1 + v2
        return Wektor(self.x + other.x, self.y + other.y)
        
    def __sub__(self, other):     # Odejmowanie: v1 - v2
        return Wektor(self.x - other.x, self.y - other.y)
        
    def __mul__(self, scalar):    # Mnożenie: v1 * 2
        return Wektor(self.x * scalar, self.y * scalar)
```

Porównania:
```python
class Osoba:
    def __init__(self, wiek):
        self.wiek = wiek
    
    def __eq__(self, other):      # Równość: a == b
        return self.wiek == other.wiek
        
    def __lt__(self, other):      # Mniejsze niż: a < b
        return self.wiek < other.wiek
        
    def __gt__(self, other):      # Większe niż: a > b
        return self.wiek > other.wiek
```

Zachowanie kontenerowe:
```python
class MojaLista:
    def __init__(self):
        self.dane = []
    
    def __len__(self):            # Długość: len(obj)
        return len(self.dane)
        
    def __getitem__(self, idx):   # Dostęp przez indeks: obj[idx]
        return self.dane[idx]
        
    def __setitem__(self, idx, val):  # Ustawianie wartości: obj[idx] = val
        self.dane[idx] = val
        
    def __contains__(self, item): # Sprawdzanie zawierania: item in obj
        return item in self.dane
```

Metody kontekstowe:
```python
class Plik:
    def __enter__(self):          # Rozpoczęcie bloku with
        print("Otwieranie pliku")
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):  # Zakończenie bloku with
        print("Zamykanie pliku")
```

Metody magiczne są potężnym mechanizmem, który pozwala na:
- Dostosowanie zachowania obiektów do standardowych operacji Pythona
- Tworzenie klas, które zachowują się jak wbudowane typy danych
- Implementację własnych protokołów i interfejsów
- Zwiększenie czytelności i intuicyjności kodu

Warto pamiętać, że metody magiczne są wywoływane automatycznie przez interpreter Pythona w odpowiednich sytuacjach, nie powinno się ich wywoływać bezpośrednio (z wyjątkiem niektórych specyficznych przypadków).