---
Utworzono: 2024-11-09T14:06:00
Zmodyfikowano: 2024-11-09T14:06:00
Źródło: 
tags:
---
Oto lista 20 przydatnych i "fajnych" zagadnień w Pythonie, które są przydatne w codziennym kodowaniu i mogą znacząco zwiększyć efektywność pracy:

---

1. **Operator trójargumentowy (ternary operator)**: Szybkie przypisywanie wartości na podstawie warunku.
   ```python
   wynik = "parzysta" if liczba % 2 == 0 else "nieparzysta"
   ```

2. **List comprehension**: Tworzenie listy w jednej linii, często używane do filtrowania lub transformacji.
   ```python
   kwadraty = [x**2 for x in range(10)]
   ```

3. **Dict comprehension**: Tworzenie słowników w jednej linii, podobnie jak list comprehension.
   ```python
   kwadraty = {x: x**2 for x in range(10)}
   ```

4. **Set comprehension**: Tworzenie zbioru w jednej linii, eliminując duplikaty.
   ```python
   unikalne_kwadraty = {x**2 for x in range(-10, 10)}
   ```

5. **Funkcje lambda**: Tworzenie małych funkcji anonimowych, zwykle jako argumenty do innych funkcji.
   ```python
   dodaj = lambda x, y: x + y
   ```

6. **Funkcje `map`, `filter`, i `reduce`**: Narzędzia do pracy z listami i innymi iterablami.
   ```python
   liczby = [1, 2, 3, 4, 5]
   podwojone = list(map(lambda x: x * 2, liczby))
   ```

7. **Unpacking**: Rozpakowywanie list, tupli lub słowników.
   ```python
   a, b, *c = [1, 2, 3, 4, 5]
   ```

8. **Walrus operator `:=`**: Przypisywanie wartości w wyrażeniu, dostępne od Pythona 3.8.
   ```python
   if (n := len(lista)) > 10:
       print(f"Lista ma więcej niż 10 elementów: {n}")
   ```

9. **Dekoratory**: Używane do modyfikowania funkcji lub metod, np. `@staticmethod`, `@classmethod`.
   ```python
   @cache
   def fibonacci(n):
       ...
   ```

10. **Funkcje `zip` i `enumerate`**: Łączenie list w pary lub dodawanie indeksu do elementów.
    ```python
    pary = list(zip(['a', 'b'], [1, 2]))
    ```

11. **Typ danych `Counter` z `collections`**: Szybkie liczenie elementów w sekwencji.
    ```python
    from collections import Counter
    c = Counter("abrakadabra")
    ```

12. **Slicing**: Wybieranie podciągów listy, ciągu znaków, itp.
    ```python
    sublista = lista[2:5]
    ```

13. **F-strings**: Łatwe i wydajne formatowanie tekstu (Python 3.6+).
    ```python
    name = "Anna"
    print(f"Cześć, {name}!")
    ```

14. **`__name__ == "__main__"`**: Sprawdzanie, czy plik jest uruchamiany jako główny skrypt.
    ```python
    if __name__ == "__main__":
        print("Kod uruchomiony bezpośrednio")
    ```

15. **Metody magiczne (dunder methods)**: Przesłanianie zachowania operatorów, np. `__str__`, `__repr__`, `__add__`.
    ```python
    def __repr__(self):
        return f"Obiekt({self.name})"
    ```

16. **Typ danych `defaultdict` z `collections`**: Automatyczne przypisywanie domyślnej wartości dla nieistniejących kluczy.
    ```python
    from collections import defaultdict
    dd = defaultdict(int)
    dd['klucz'] += 1
    ```

17. **Zarządzanie zasobami (`with` i menedżery kontekstu)**: Automatyczne otwieranie i zamykanie zasobów, np. plików.
    ```python
    with open("plik.txt") as f:
        dane = f.read()
    ```

18. **Generator expressions**: Podobne do list comprehension, ale zwraca generator zamiast listy, co jest bardziej wydajne pamięciowo.
    ```python
    generator_kwadratow = (x**2 for x in range(10))
    ```

19. **Funkcje `any()` i `all()`**: Sprawdzanie, czy dowolny (lub wszystkie) elementy w iteracji spełniają dany warunek.
    ```python
    if any(x > 10 for x in liczby):
        print("Jest liczba większa niż 10")
    ```

20. **Funkcja `itertools`**: Obsługuje operacje na iterablach, takie jak permutacje, kombinacje, grupowanie, itd.
    ```python
    from itertools import permutations
    perm = list(permutations([1, 2, 3]))
    ```

---

Opanowanie tych zagadnień może zdecydowanie przyspieszyć pracę i sprawić, że kod będzie bardziej czytelny, zwarty i efektywny.