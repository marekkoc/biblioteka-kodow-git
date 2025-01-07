---
Utworzono: 2024-12-27T15:22:00
Zmodyfikowano: 2024-12-27T15:22:00
Źródło: chatGPT
tags: 
Katalog:
---
# Try-except

W Pythonie konstrukcja **`try...except`** służy do obsługi wyjątków, czyli błędów, które mogą wystąpić podczas wykonywania programu. Dzięki niej możesz przechwycić potencjalne błędy i zapobiec awarii programu.

### Składnia

```python
try:
    # Kod, który może spowodować wyjątek
except [ExceptionType] [as variable]:
    # Kod, który zostanie wykonany, jeśli wystąpi wyjątek
else:
    # (Opcjonalne) Kod, który zostanie wykonany, jeśli nie wystąpi wyjątek
finally:
    # (Opcjonalne) Kod, który zawsze zostanie wykonany, niezależnie od tego, czy wyjątek wystąpił, czy nie
```

### Jak działa `try...except`

1. **Blok `try`:**
   Kod w bloku `try` jest wykonywany. Jeśli wystąpi wyjątek, kontrola przechodzi do bloku `except`.

2. **Blok `except`:**
   Kod w bloku `except` zostanie wykonany, jeśli w bloku `try` wystąpi wyjątek pasujący do podanego typu. Możesz obsłużyć konkretny typ wyjątku lub wszystkie wyjątki.

3. **Blok `else` (opcjonalny):**
   Jeśli blok `try` zakończy się bez błędów, zostanie wykonany blok `else`.

4. **Blok `finally` (opcjonalny):**
   Kod w bloku `finally` zawsze zostanie wykonany, bez względu na to, czy wyjątek wystąpił, czy nie. Używany jest do sprzątania, np. zamykania plików lub połączeń.

---

### Przykład 1: Podstawowe użycie `try...except`
```python
try:
    num = int(input("Podaj liczbę: "))
    wynik = 10 / num
    print(f"Wynik: {wynik}")
except ZeroDivisionError:
    print("Nie można dzielić przez zero!")
except ValueError:
    print("Wprowadź poprawną liczbę!")
```

**Działanie:**
- Jeśli użytkownik wprowadzi `0`, zostanie przechwycony wyjątek `ZeroDivisionError`.
- Jeśli użytkownik wprowadzi niepoprawną wartość (np. tekst), zostanie przechwycony wyjątek `ValueError`.

---

### Przykład 2: Obsługa różnych typów wyjątków
```python
try:
    with open("plik.txt", "r") as plik:
        zawartość = plik.read()
except FileNotFoundError:
    print("Plik nie został znaleziony.")
except PermissionError:
    print("Brak uprawnień do otwarcia pliku.")
else:
    print("Zawartość pliku:", zawartość)
finally:
    print("Operacja pliku zakończona.")
```

**Działanie:**
- Jeśli plik nie istnieje, zostanie przechwycony wyjątek `FileNotFoundError`.
- Jeśli brakuje uprawnień, zostanie przechwycony `PermissionError`.
- Blok `finally` zostanie wykonany niezależnie od błędów.

---

### Kiedy używać `try...except`?

1. **Zapobieganie awariom programu:** 
   Używaj `try...except`, aby program działał dalej mimo błędów.
   
2. **Przewidywanie błędów:**
   Obsługuj sytuacje, w których błąd jest możliwy, np. brak pliku, dzielenie przez zero.

3. **Sprzątanie:**
   W połączeniu z `finally`, np. do zamykania plików lub połączeń sieciowych.

---

### Kluczowe wskazówki

- Nie używaj **zbyt ogólnych `except`**, takich jak:
  ```python
  except:
      print("Wystąpił błąd.")
  ```
  Lepiej określać konkretne typy wyjątków.

- Możesz złapać wiele wyjątków:
  ```python
  except (ValueError, TypeError):
      print("Obsługuję ValueError lub TypeError.")
  ```

- Jeśli musisz złapać wszystkie błędy, zaleca się użycie `Exception`:
  ```python
  except Exception as e:
      print(f"Wystąpił błąd: {e}")
  ```

Teraz zrozumiesz, jak `try...except` pomaga w kontrolowaniu błędów i sprawnym działaniu programu! 😊

# Angielska wersja:

Konstrukcja **`try...except`** w Pythonie nazywa się po angielsku **"exception handling"** (obsługa wyjątków). Poszczególne części mają również swoje nazwy:

- **`try` block**: Blok kodu, w którym próbujemy wykonać operacje, które mogą spowodować wyjątek (ang. "try block").
- **`except` block**: Blok, w którym przechwytujemy i obsługujemy wyjątki (ang. "except block").
- **`else` block** (opcjonalny): Blok wykonywany, jeśli nie wystąpiły żadne wyjątki (ang. "else block").
- **`finally` block** (opcjonalny): Blok wykonywany niezależnie od tego, czy wystąpił wyjątek (ang. "finally block").

Całość jest określana jako **"try-except construct"** lub po prostu **"try-except statement"**.

Podstawowa terminologia:

- **Exception Handling**: Ogólna nazwa procesu obsługi wyjątków.
- **Exception**: Sam błąd (wyjątek), który występuje podczas wykonywania programu.