---
Utworzono: 2024-10-30T09:51:00
Zmodyfikowano: 2024-10-30T09:51:00
Źródło: chatGPT
tags:
  - "#dunder-method"
---

Dunder methods, znane również jako "**metody magiczne**" w Pythonie, to specjalne metody, które mają **podwójne podkreślenia** na początku i końcu nazwy, np. `__init__`, `__str__`, `__len__`. Skrót "dunder" pochodzi od *double underscore* (podwójnego podkreślenia). Te metody pozwalają na **specjalne zachowanie obiektów** i pozwalają na dostosowanie wbudowanych funkcji i operatorów do własnych potrzeb.

### Najważniejsze dunder methods:
- **`__init__`**: Konstruktor klasy, wywoływany podczas tworzenia nowego obiektu, np. `MyClass()`.
- **`__str__`**: Reprezentacja tekstowa obiektu zwracana przez `str()`, często używana do czytelnego wyświetlania obiektów.
- **`__repr__`**: Reprezentacja obiektu używana w `repr()`, zwraca bardziej szczegółowy opis obiektu, przydatna w debugowaniu.
- **`__len__`**: Zwraca długość obiektu, co pozwala na użycie `len()` na obiekcie.
- **`__getitem__`**, **`__setitem__`**: Pozwalają na dostęp do elementów za pomocą notacji `[]` (np. obiekt może działać jak lista lub słownik).
- **`__call__`**: Umożliwia wywołanie obiektu jak funkcji (np. `my_obj()`).
  
Dunder methods umożliwiają tworzenie czytelniejszego, bardziej "pythonicznego" kodu przez integrację obiektów z wbudowanymi funkcjami Pythona oraz operacjami na obiektach.


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