---
Utworzono: 2024-11-08T08:54:00
Zmodyfikowano: 2024-11-08T08:54:00
Źródło: chatGPT
tags:
---
W Pythonie zarówno metody klasowe (`@classmethod`), jak i statyczne (`@staticmethod`) różnią się od metod instancji. Oto główne różnice między metodami klasowymi a statycznymi:

### 1. **Metoda klasowa (`@classmethod`)**
   - Metoda klasowa jest związana z **klasą**, a nie z konkretną instancją klasy.
   - Jako pierwszy argument przyjmuje `cls`, który odnosi się do samej klasy, a nie do obiektu (instancji) klasy. Nazwa `cls` jest konwencjonalna, tak jak `self` dla metod instancji.
   - Jest używana, gdy potrzebujemy operować na danych lub metodach na poziomie klasy (np. zmiennych klasowych) zamiast na poziomie instancji.
   - Dzięki `@classmethod` możemy tworzyć alternatywne konstruktory (metody, które tworzą obiekty klasy).

   **Przykład metody klasowej:**

   ```python
   class MyClass:
       class_variable = "Jestem zmienną klasową"

       @classmethod
       def show_class_variable(cls):
           print(cls.class_variable)

       @classmethod
       def create_with_default(cls):
           return cls("domyślne imię")

       def __init__(self, name):
           self.name = name

   # Wywołanie metody klasowej bez tworzenia instancji
   MyClass.show_class_variable()

   # Użycie metody klasowej jako alternatywnego konstruktora
   obj = MyClass.create_with_default()
   print(obj.name)
   ```

   - `show_class_variable` wyświetla wartość zmiennej `class_variable`, która jest wspólna dla całej klasy.
   - `create_with_default` to alternatywny konstruktor, który pozwala utworzyć obiekt klasy z domyślnym argumentem.

### 2. **Metoda statyczna (`@staticmethod`)**
   - Metoda statyczna jest również związana z klasą, ale **nie przyjmuje żadnego specjalnego argumentu** (`cls` lub `self`), więc nie ma bezpośredniego dostępu ani do stanu klasy, ani do stanu instancji.
   - Jest stosowana wtedy, gdy funkcjonalność metody jest logicznie związana z klasą, ale nie potrzebuje dostępu do jej wewnętrznych danych.
   - Metody statyczne mogą być wywoływane bez tworzenia instancji klasy, a ich głównym celem jest wykonywanie funkcji pomocniczych lub narzędziowych, które są powiązane z logiką klasy.

   **Przykład metody statycznej:**

   ```python
   class MathOperations:
       @staticmethod
       def add(x, y):
           return x + y

       @staticmethod
       def multiply(x, y):
           return x * y

   # Wywołanie metod statycznych bez tworzenia instancji
   print(MathOperations.add(5, 3))        # Output: 8
   print(MathOperations.multiply(4, 6))   # Output: 24
   ```

   - `add` i `multiply` są metodami pomocniczymi, które wykonują operacje matematyczne, ale nie potrzebują dostępu do danych klasy ani do jej instancji.

### Główne różnice podsumowane:

| Typ metody         | Dekorator       | Pierwszy argument | Dostęp do klasy | Dostęp do instancji |
|--------------------|-----------------|-------------------|------------------|----------------------|
| Metoda klasowa     | `@classmethod`  | `cls`            | Tak             | Nie                 |
| Metoda statyczna   | `@staticmethod` | brak             | Nie             | Nie                 |
| Metoda instancji   | brak            | `self`           | Tak             | Tak                 |

Metody klasowe są używane, gdy musimy pracować na poziomie klasy (np. przy tworzeniu obiektów lub manipulowaniu zmiennymi klasowymi), natomiast metody statyczne służą do oddzielenia funkcji pomocniczych, które nie wymagają ani dostępu do instancji, ani do samej klasy.
