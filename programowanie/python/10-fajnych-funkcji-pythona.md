---
Utworzono: 2024-11-09T14:06:00
Zmodyfikowano: 2024-11-09T14:06:00
Źródło: 
tags:
---

Oto lista dziesięciu przydatnych zagadnień w Pythonie, które są bardzo użyteczne i często stosowane, szczególnie gdy zależy nam na pisaniu zwięzłego i eleganckiego kodu:

1. **Operator trójargumentowy**:
   Pozwala przypisać wartość zależnie od warunku w jednej linii. 

   ```python
   status = "parzysta" if liczba % 2 == 0 else "nieparzysta"
   ```

2. **List comprehension**:
   Skrócona forma zapisu pętli `for` z opcjonalnym warunkiem, stosowana do generowania listy.

   ```python
   kwadraty = [x**2 for x in range(10) if x % 2 == 0]
   ```

3. **Dictionary comprehension**:
   Podobna idea do `list comprehension`, ale dla słowników. Umożliwia szybkie tworzenie słowników.

   ```python
   kwadraty = {x: x**2 for x in range(10)}
   ```

4. **Set comprehension**:
   Szybkie generowanie zbiorów za pomocą składni podobnej do `list comprehension`.

   ```python
   parzyste = {x for x in range(10) if x % 2 == 0}
   ```

5. **Funkcje lambda**:
   Funkcje anonimowe, które można tworzyć „w locie”, np. jako argumenty do funkcji takich jak `map`, `filter`.

   ```python
   suma = lambda a, b: a + b
   ```

6. **Dekoratory**:
   Funkcje modyfikujące inne funkcje bez zmiany ich kodu. Są powszechnie stosowane np. w Django do zarządzania uprawnieniami, a także do rejestrowania wywołań funkcji.

   ```python
   def log(funkcja):
       def wrapper(*args, **kwargs):
           print(f"Wywołano {funkcja.__name__}")
           return funkcja(*args, **kwargs)
       return wrapper

   @log
   def przyklad():
       print("Hello!")
   ```

7. **Context managers (`with`)**:
   Używane do zarządzania zasobami (np. plikami), które automatycznie są zamykane po zakończeniu działania.

   ```python
   with open('plik.txt', 'r') as file:
       dane = file.read()
   ```

8. **Funkcje `map`, `filter`, `reduce`**:
   Funkcje funkcyjne do przetwarzania listy lub innej kolekcji.

   ```python
   liczby = [1, 2, 3, 4]
   podwojone = list(map(lambda x: x * 2, liczby))  # [2, 4, 6, 8]
   ```

9. **Unpacking (`*` i `**`)**:
   Pozwala na rozpakowywanie list, krotek oraz słowników. Często stosowane w przekazywaniu argumentów do funkcji.

   ```python
   lista = [1, 2, 3]
   def przyklad(a, b, c):
       print(a, b, c)

   przyklad(*lista)  # Wywoła przyklad(1, 2, 3)
   ```

10. **Operatory `zip` i `enumerate`**:
    `zip` łączy dwie listy w listę krotek, a `enumerate` dodaje indeks do elementów listy.

    ```python
    imiona = ['Ala', 'Ola', 'Ela']
    wiek = [20, 25, 30]
    for imie, wiek in zip(imiona, wiek):
        print(f"{imie} ma {wiek} lat")

    for indeks, wartosc in enumerate(imiona):
        print(f"{indeks}: {wartosc}")
    ```

Znajomość tych konstrukcji może znacznie zwiększyć wydajność i czytelność kodu w Pythonie!