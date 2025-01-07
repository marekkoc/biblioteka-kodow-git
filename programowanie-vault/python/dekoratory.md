---
Utworzono: 2025-01-05T15:17:00
Zmodyfikowano: 2025-01-05T15:17:00
Źródło: chatGPT
tags:
  - "#dekoratory"
Katalog:
---

Dekoratory w Pythonie są specjalnymi funkcjami, które modyfikują lub rozszerzają zachowanie innych funkcji, metod lub klas. Są powszechnie używane w celu zmniejszenia redundancji kodu, poprawy czytelności i umożliwienia łatwego dodawania dodatkowych funkcjonalności.

---

### **Zasada działania dekoratorów**
Dekorator to funkcja, która przyjmuje inną funkcję jako argument, a następnie zwraca nową funkcję (lub obiekt callable). Nowa funkcja może modyfikować lub rozszerzać działanie oryginalnej funkcji.

```python
def dekorator(funkcja):
    def nowa_funkcja(*args, **kwargs):
        print("Przed wywołaniem funkcji")
        wynik = funkcja(*args, **kwargs)
        print("Po wywołaniu funkcji")
        return wynik
    return nowa_funkcja
```

Dekorator można nałożyć na funkcję za pomocą symbolu `@`:

```python
@dekorator
def przyklad():
    print("Działanie funkcji")

przyklad()
```

**Wynik działania:**
```
Przed wywołaniem funkcji
Działanie funkcji
Po wywołaniu funkcji
```

---

### **Cel stosowania dekoratorów**
1. **Separacja logiki:** Dekoratory pozwalają oddzielić dodatkowe funkcjonalności (np. logowanie, sprawdzanie uprawnień) od głównej logiki funkcji.
2. **Reużywalność:** Dekoratory można łatwo zastosować w wielu miejscach w kodzie.
3. **Czytelność:** Kod jest bardziej czytelny, ponieważ dodatkowe operacje są przeniesione do dekoratorów, a funkcje pozostają czyste i zwięzłe.
4. **Dynamiczne modyfikacje:** Dekoratory pozwalają zmieniać działanie funkcji lub metod w czasie działania programu.

---

### **Przykłady użycia dekoratorów**

#### **1. Logowanie wywołań funkcji**
```python
def logowanie(funkcja):
    def opakowanie(*args, **kwargs):
        print(f"Wywołanie funkcji {funkcja.__name__} z argumentami {args} i {kwargs}")
        wynik = funkcja(*args, **kwargs)
        print(f"Funkcja {funkcja.__name__} zwróciła: {wynik}")
        return wynik
    return opakowanie

@logowanie
def dodaj(a, b):
    return a + b

dodaj(2, 3)
```

**Wynik:**
```
Wywołanie funkcji dodaj z argumentami (2, 3) i {}
Funkcja dodaj zwróciła: 5
```

---

#### **2. Sprawdzanie uprawnień**
```python
def wymaga_uprawnien(funkcja):
    def opakowanie(*args, **kwargs):
        user = kwargs.get('user', 'nieznany')
        if user != 'admin':
            raise PermissionError("Brak uprawnień!")
        return funkcja(*args, **kwargs)
    return opakowanie

@wymaga_uprawnien
def usun_dane(id, user):
    print(f"Dane o id={id} zostały usunięte.")

# Prawidłowe wywołanie
usun_dane(42, user='admin')

# Nieprawidłowe wywołanie
usun_dane(42, user='guest')  # Wywoła wyjątek
```

---

#### **3. Pamięć podręczna (cache)**
Dekorator do zapamiętywania wyników funkcji:

```python
def cache(funkcja):
    pamiec = {}
    def opakowanie(*args):
        if args in pamiec:
            print("Zwracanie z pamięci podręcznej")
            return pamiec[args]
        wynik = funkcja(*args)
        pamiec[args] = wynik
        return wynik
    return opakowanie

@cache
def silnia(n):
    if n == 0:
        return 1
    return n * silnia(n - 1)

print(silnia(5))  # Oblicza i zapisuje wynik
print(silnia(5))  # Zwraca z pamięci podręcznej
```

---

### **Ważne informacje**
1. **`functools.wraps`:** Używanie tego dekoratora w środku dekoratora zachowuje metadane oryginalnej funkcji (np. `__name__`, `__doc__`).
   ```python
   from functools import wraps

   def dekorator(funkcja):
       @wraps(funkcja)
       def opakowanie(*args, **kwargs):
           return funkcja(*args, **kwargs)
       return opakowanie
   ```

2. **Dekorowanie metod klas:** Dekoratory działają zarówno na funkcjach wolnostojących, jak i metodach w klasach.

3. **Kaskadowe dekoratory:** Można nałożyć wiele dekoratorów, które są stosowane w kolejności od góry do dołu.

---

Dekoratory to potężne narzędzie w Pythonie, które ułatwia tworzenie eleganckiego, czytelnego i elastycznego kodu!