---
Utworzono: 2024-10-13T10:18:00
Zmodyfikowano: 2024-12-01T13:08:00
tags:
  - "#type-annotation"
Źródło: chatGPT
---


# Type annotation - type hint

Notatka na podstawie odpowiedzi chatGPT.

W Pythonie **"type hint"** (wskazówka typów) lub **"type annotation"** (anotacja typów) to sposób na informowanie o typach danych używanych w kodzie, co ułatwia jego czytelność, sprawdzanie poprawności oraz narzędziom statycznym wykrywanie potencjalnych błędów.

### Jak to działa?
Type hinting pozwala na wskazanie typów danych dla zmiennych, argumentów funkcji oraz wartości zwracanych przez funkcje, ale nie jest przez Python bezpośrednio egzekwowane (nie wprowadza typowania statycznego). Wskazówki typów działają jako informacja pomocnicza dla programisty oraz narzędzi, takich jak ==**mypy**==, **PyCharm**, czy **VS Code**, do przeprowadzania sprawdzeń typów.

### Przykłady użycia

1. **Anotacja zmiennych**:
   ```python
   age: int = 25
   name: str = "Alice"
   scores: list[int] = [95, 87, 92]
   ```

2. **Type hints w funkcjach**:
   - **Dla argumentów i wartości zwracanej**:
     ```python
     def greet(name: str) -> str:
         return f"Hello, {name}"
     ```
   - **Funkcja z listą jako argument**:
     ```python
     def calculate_average(scores: list[float]) -> float:
         return sum(scores) / len(scores)
     ```

3. **Opcjonalne typy**: Jeśli funkcja może przyjąć wartość `None`, stosujemy **Optional** (dostępne z modułu `typing`):
   ```python
   from typing import Optional

   def get_user_age(user_id: int) -> Optional[int]:
       # Funkcja może zwrócić wiek użytkownika lub None
       ...
   ```

4. **Typy złożone i zagnieżdżone**: Typy dla słowników, tupli, zestawów, itp., można określić przy użyciu `typing.Dict`, `typing.Tuple`, itp.:
   ```python
   from typing import Dict, Tuple

   def get_user_info(user_id: int) -> Dict[str, Tuple[str, int]]:
       # Zwraca słownik, gdzie klucz to str, a wartość to tupla z nazwą i wiekiem
       ...
   ```

### Zalety "type hint"
- **Czytelność**: Kod jest łatwiejszy do zrozumienia.
- **Sprawdzanie błędów**: Narzędzia mogą analizować kod i wykrywać błędy typów.
- **Intuicyjność dla IDE**: Edytory kodu mogą podpowiadać odpowiednie typy danych i autouzupełnianie.

Type hinty to przydatne narzędzie, które zwiększa jakość kodu i wspomaga jego utrzymanie, szczególnie w większych projektach.


## Kilka słów dlaczego stosować "podpowiedzi typów"

Fragment pochodzi z książki: #book-2019-kopec-classic-computer-science-problems-in-python 
ze strony 4:

Every code listing in this book makes use of Python type hints, also known as type
annotations. These annotations are a relatively new feature for the Python language,
and they may look intimidating to Python programmers who have never seen them
before. They are used for three reasons:

1. They provide clarity about the types of variables, function parameters, and function returns
2. They self-document the code in a sense, as a result of reason 1. Instead of having to search through a comment or docstring to find the return type of a function, you can just look at its signature.
3. They allow the code to be type-checked for correctness. One popular Python
type checker is mypy.

They provide clarity about the types of variables, function parameters, and function returns.
They self-document the code in a sense, as a result of reason 1. Instead of having to search through a comment or docstring to find the return type of a function, you can just look at its signature.
They allow the code to be type-checked for correctness. One popular Python type checker  is ==mypy==

# mypy

Odpowiedź z chatGPT

**`mypy`** to pakiet do statycznego sprawdzania typów w Pythonie. Pozwala analizować kod, aby upewnić się, że typy używane w całym programie są zgodne z oczekiwaniami, co pomaga zapobiegać błędom wynikającym z niepoprawnych typów danych. `mypy` współpracuje z type hintami (anotacjami typów) w Pythonie, które programista umieszcza w kodzie dla zmiennych, argumentów funkcji oraz wartości zwracanych.

### Jak działa `mypy`?
1. **Analiza statyczna**: `mypy` działa w czasie statycznym, co oznacza, że sprawdza kod bez jego uruchamiania. Analizuje zgodność typów w oparciu o anotacje typów.
2. **Kompatybilność z PEP 484**: `mypy` opiera się na standardzie **PEP 484**, który wprowadza type hinty do Pythona, i obsługuje także zaawansowane typy, takie jak typy złożone, typy opcjonalne, unie, generatory itp.
3. **Integracja z narzędziami**: `mypy` można zintegrować z edytorami kodu, np. VS Code lub PyCharm, aby sprawdzał typy w locie i pokazywał potencjalne błędy.

### Przykład użycia `mypy`
Poniższy kod zawiera błędne przypisanie typu. `mypy` zasygnalizuje niezgodność między deklarowanym typem `int` a przypisaną wartością `str`:

```python
def add(a: int, b: int) -> int:
    return a + b

result: int = add(5, "10")  # Błąd: drugi argument jest typu `str`, a nie `int`.
```

Jeśli uruchomimy `mypy` na powyższym kodzie:
```bash
mypy script.py
```

To wynik pokaże błąd typu, ponieważ `"10"` jest typu `str`, a nie `int`.

### Dlaczego warto używać `mypy`?
- **Większa niezawodność kodu**: Zapewnia zgodność typów, co zmniejsza liczbę błędów.
- **Lepsza czytelność**: Kod z anotacjami typów jest bardziej przejrzysty i łatwiejszy do zrozumienia.
- **Pomoc w refaktoryzacji**: `mypy` pomaga zidentyfikować potencjalne problemy typowe przy zmianach w kodzie.

`mypy` jest szczególnie przydatny w większych projektach lub tam, gdzie Python współpracuje z różnorodnymi typami danych i złożonymi strukturami, zapewniając lepszą kontrolę nad spójnością typów.

# Zastosowanie listy obiektów klasy ``Pirate``

Aby zastosować **type annotations** dla listy obiektów klasy `Pirate` w Pythonie, można użyć wbudowanego modułu `typing`, który oferuje narzędzia do precyzyjnego opisywania typów.

### Przykład

Załóżmy, że masz klasę `Pirate` i chcesz zadeklarować listę zawierającą obiekty tej klasy.

1. Importujesz `List` z modułu `typing`.
2. Deklarujesz typ listy za pomocą `List[Pirate]`.

#### Kod:

```python
from typing import List

class Pirate:
    def __init__(self, name: str, ship: str):
        self.name = name
        self.ship = ship

# Deklaracja zmiennej zawierającej listę obiektów Pirate
pirates: List[Pirate] = [
    Pirate("Jack Sparrow", "Black Pearl"),
    Pirate("Hector Barbossa", "Queen Anne's Revenge"),
]

# Przykład funkcji operującej na liście Pirate
def list_pirates(pirates: List[Pirate]) -> None:
    for pirate in pirates:
        print(f"{pirate.name} sails on the {pirate.ship}")

# Wywołanie funkcji
list_pirates(pirates)
```

### Wyjaśnienia:

1. **`List[Pirate]`**:
    - Oznacza listę, której elementy są obiektami klasy `Pirate`.
2. **Type annotation dla funkcji**:
    - Funkcja `list_pirates` przyjmuje jako argument listę obiektów typu `Pirate` i nie zwraca żadnej wartości (`-> None`).

### Wersja z `from __future__ import annotations` (opcjonalne)

Od Pythona 3.7 możesz użyć przyszłościowej opcji, aby uprościć deklaracje typów, szczególnie w przypadku klas, które nie są jeszcze zdefiniowane:

```python
from __future__ import annotations

class Pirate:
    def __init__(self, name: str, ship: str):
        self.name = name
        self.ship = ship

pirates: list[Pirate] = [Pirate("Anne Bonny", "Revenge")]
```

Tutaj używamy małych liter `list` zamiast `List` dzięki wprowadzeniu w Pythonie 3.9 ulepszonych natywnych typów.

# ``list`` vs. ``List``

W Pythonie `list` i `List` to dwa różne pojęcia, które mają inne zastosowania i znaczenie:

---

### **1. `list` – Wbudowany typ w Pythonie**

- **Czym jest**: `list` to wbudowany typ danych w Pythonie, który reprezentuje dynamicznie rozciągliwą listę.
- **Jak działa**: Możesz używać `list` do tworzenia rzeczywistych list i manipulowania nimi w czasie wykonania programu.

#### Przykład:

```python
my_list = [1, 2, 3]  # Tworzenie listy
print(type(my_list))  # <class 'list'>
```

---

### **2. `List` – Typ do adnotacji (annotations) z modułu `typing`**

- **Czym jest**: `List` pochodzi z modułu `typing` i służy wyłącznie do **adnotacji typów**. Jest używane w celu wskazania, jakiego rodzaju wartości lista ma przechowywać.
- **Jak działa**: Pozwala programiście i narzędziom (np. linters, IDE, mypy) sprawdzić, czy lista zawiera elementy zgodne z oczekiwanym typem.

#### Przykład:

```python
from typing import List

def process_numbers(numbers: List[int]) -> int:
    return sum(numbers)

# Deklaracja, że lista powinna zawierać liczby całkowite
nums: List[int] = [1, 2, 3]  # Poprawnie
```

---

### **Różnice między `list` a `List`:**

|**Cecha**|**list**|**List (z `typing`)**|
|---|---|---|
|**Przeznaczenie**|Wbudowany typ danych|Typ dla adnotacji|
|**Działanie w czasie**|Tworzy listę i operuje na niej w runtime|Używany tylko do opisywania typów w kodzie|
|**Import**|Wbudowany (nie wymaga importu)|Wymaga importu z `typing` (do Pythona 3.9)|
|**Wersja Pythona**|Dostępny zawsze|Od Pythona 3.5 (z `typing`)|

---

### **Od Pythona 3.9: uproszczenie adnotacji**

W Pythonie 3.9 wprowadzono możliwość użycia wbudowanego `list` jako typu dla adnotacji. Dzięki temu zamiast `List` z `typing`, możesz po prostu pisać:

```python
def process_numbers(numbers: list[int]) -> int:  # Nowy styl
    return sum(numbers)
```

To oznacza, że od Pythona 3.9 `List` z `typing` staje się mniej potrzebny, ale nadal jest używany w starszych kodach.

---

### Kiedy używać?

- Używasz **`list`** do faktycznego tworzenia i manipulacji list w swoim kodzie.
- Używasz **`List`** (lub od Pythona 3.9 `list[int]`) do opisywania typów dla narzędzi analizy kodu i poprawy czytelności kodu.
# Popularne typy zmiennych w module ``typing``

Moduł `typing` w Pythonie dostarcza bogaty zestaw oznaczeń do opisywania typów zmiennych, argumentów funkcji, oraz wartości zwracanych. Oto lista popularnych oznaczeń:

---

### **Podstawowe typy**

1. **`Any`**  
    Reprezentuje dowolny typ. Używane, gdy typ nie jest znany lub może być dowolny.
    
    ```python
    from typing import Any
    def process(data: Any) -> None:
        pass
    ```
    
2. **`Union`**  
    Wskazuje, że wartość może być jednym z wielu typów.
    
    ```python
    from typing import Union
    def process(value: Union[int, str]) -> None:
        pass
    ```
    
3. **`Optional`**  
    Skrót dla `Union[Typ, None]`. Wskazuje, że wartość może być określonego typu lub `None`.
    
    ```python
    from typing import Optional
    def get_name(id: int) -> Optional[str]:
        return None if id == 0 else "John"
    ```
    

---

### **Kolekcje**

4. **`List`**  
    Lista z elementami określonego typu.
    
    ```python
    from typing import List
    numbers: List[int] = [1, 2, 3]
    ```
    
5. **`Tuple`**  
    Krotka z określoną liczbą i typem elementów.
    
    ```python
    from typing import Tuple
    coordinates: Tuple[float, float] = (1.0, 2.0)
    ```
    
6. **`Set`**  
    Zbiór z elementami określonego typu.
    
    ```python
    from typing import Set
    unique_ids: Set[int] = {1, 2, 3}
    ```
    
7. **`Dict`**  
    Słownik z kluczami i wartościami określonych typów.
    
    ```python
    from typing import Dict
    user_data: Dict[str, int] = {"age": 30, "score": 100}
    ```
    
8. **`FrozenSet`**  
    Niezmienny zbiór z elementami określonego typu.
    
    ```python
    from typing import FrozenSet
    permissions: FrozenSet[str] = frozenset(["read", "write"])
    ```
    
9. **`Deque`**  
    Kolejka dwustronna z elementami określonego typu.
    
    ```python
    from typing import Deque
    from collections import deque
    tasks: Deque[str] = deque(["task1", "task2"])
    ```
    

---

### **Funkcje**

10. **`Callable`**  
    Oznacza funkcję z określonymi typami argumentów i zwracaną wartością.
    
    ```python
    from typing import Callable
    def execute(func: Callable[[int, int], int]) -> int:
        return func(1, 2)
    ```
    

---

### **Iteratory i generatory**

11. **`Iterable`**  
    Obiekt, który można iterować (np. lista, generator).
    
    ```python
    from typing import Iterable
    def process(items: Iterable[int]) -> None:
        for item in items:
            print(item)
    ```
    
12. **`Iterator`**  
    Obiekt, który implementuje metodę `__next__`.
    
    ```python
    from typing import Iterator
    def get_numbers() -> Iterator[int]:
        yield from range(10)
    ```
    

---

### **Specjalne typy kolekcji**

13. **`TypedDict`**  
    Słownik z określonymi typami kluczy i wartości.
    
    ```python
    from typing import TypedDict
    class User(TypedDict):
        name: str
        age: int
    user: User = {"name": "Alice", "age": 25}
    ```
    
14. **`Literal`**  
    Wartość musi być jedną z podanych w adnotacji.
    
    ```python
    from typing import Literal
    def set_mode(mode: Literal["read", "write"]) -> None:
        print(f"Mode set to {mode}")
    ```
    

---

### **Typy ogólne (Generic Types)**

15. **`TypeVar`**  
    Używane do definiowania generycznych typów w funkcjach lub klasach.
    
    ```python
    from typing import TypeVar
    T = TypeVar('T')
    def echo(value: T) -> T:
        return value
    ```
    

---

### **Starsze kolekcje vs nowe typy w Pythonie 3.9+**

W Pythonie 3.9 wprowadzono wsparcie dla natywnych typów generics, dzięki czemu zamiast `List[int]` możesz pisać `list[int]`.

Przykłady:

- `list[int]` zamiast `List[int]`
- `dict[str, int]` zamiast `Dict[str, int]`
- `tuple[int, str]` zamiast `Tuple[int, str]

# Podstawowe typy: str, int, float

W Pythonie typy takie jak `int`, `float`, czy `str` (string) są wbudowane i można ich używać zarówno w czasie wykonywania programu, jak i w adnotacjach typów. Python jednak nie posiada bezpośredniego odpowiednika typu `double`, ponieważ `float` jest domyślnym typem reprezentującym liczby zmiennoprzecinkowe (odpowiadający 64-bitowemu `double` w C).

Oto szczegóły dotyczące tych typów w Pythonie:

---

### **1. `int`**

- Reprezentuje liczby całkowite (np. `1`, `42`, `-7`).
- Używany w adnotacjach typów bez dodatkowych importów.

#### Przykład:

```python
x: int = 10
def add(a: int, b: int) -> int:
    return a + b
```

---

### **2. `float`**

- Reprezentuje liczby zmiennoprzecinkowe (np. `3.14`, `-0.001`, `2.0`).
- W Pythonie odpowiada typowi `double` w językach takich jak C/C++.

#### Przykład:

```python
pi: float = 3.14
def multiply(a: float, b: float) -> float:
    return a * b
```

---

### **3. `str`**

- Reprezentuje ciągi znaków, czyli teksty (np. `"hello"`, `"123"`).
- Używany w adnotacjach typów do oznaczania zmiennych tekstowych.

#### Przykład:

```python
name: str = "Alice"
def greet(person: str) -> str:
    return f"Hello, {person}!"
```

---

### **4. `bool`**

- Reprezentuje wartość logiczną: `True` lub `False`.

#### Przykład:

```python
is_active: bool = True
def toggle(status: bool) -> bool:
    return not status
```

---

### **A co z typem `double`?**

- Python nie ma typu `double` jako odrębnej kategorii. W języku Python typ `float` jest równoważny typowi `double` w innych językach programowania, ponieważ używa 64-bitowej precyzji IEEE 754.
- Nie ma potrzeby specjalnej adnotacji dla `double`, ponieważ `float` wystarcza.

#### Przykład:

```python
value: float = 3.14159265359  # Precyzja 64-bitowa
```

---

### **Porównanie z innymi językami**

|Typ w Pythonie|Odpowiednik w C/C++|Uwagi w Pythonie|
|---|---|---|
|`int`|`int`, `long`|Obsługuje arbitralnie duże liczby|
|`float`|`float`, `double`|Równoważne `double` (64-bitowy)|
|`str`|`char*`, `std::string`|Unicode, dynamiczna długość|
|`bool`|`bool`|True/False|

---

### **W użyciu z modułem `typing`**

Moduł `typing` nie wymaga osobnych typów dla tych podstawowych kategorii (`int`, `float`, `str`, `bool`). Używasz ich tak samo w adnotacjach typów, np.:

```python
def calculate_area(width: float, height: float) -> float:
    return width * height

def format_message(user: str, age: int) -> str:
    return f"{user} is {age} years old."
```

Nie ma potrzeby importowania tych typów z `typing`, ponieważ są wbudowane.