---
Utworzono: 2024-12-27T15:53:00
Zmodyfikowano: 2024-12-27T15:53:00
Źródło: chatGPT
tags: 
Katalog:
---
### **Walrus Operator (`:=`) w Pythonie**

**Walrus operator**, oficjalnie znany jako **operator przypisania wartości w wyrażeniu** (ang. *assignment expression*), został wprowadzony w Pythonie 3.8. Symbolizowany jest jako `:=`.

### **Jak działa?**

Operator `:=` pozwala przypisać wartość do zmiennej w ramach wyrażenia. Jest używany, gdy chcesz przypisać wartość do zmiennej i jednocześnie użyć tej wartości w dalszym kodzie. Zmniejsza to konieczność powtarzania kodu.

### **Potrzeba stosowania**

1. **Oszczędność kodu:**
   Umożliwia uniknięcie wielokrotnego obliczania tej samej wartości lub powtarzania tej samej funkcji w kodzie.

2. **Poprawa czytelności:**
   Łączy przypisanie zmiennej i jej użycie w jednym miejscu, co zmniejsza liczbę wierszy kodu.

3. **Optymalizacja:**
   Pozwala na przechowanie wyniku funkcji lub obliczeń w zmiennej bez potrzeby ponownego ich wykonywania.

---

### **Przykłady**

#### **1. Tradycyjny kod (przed `:=`)**
```python
data = input("Podaj dane: ")
if len(data) > 5:
    print(f"Długie dane: {data}")
```

Za pomocą `walrus operator` kod staje się krótszy:

#### **2. Z użyciem `:=`**
```python
if (data := input("Podaj dane: ")) and len(data) > 5:
    print(f"Długie dane: {data}")
```

---

### **Główne zastosowania**

#### **1. Pętle (while)**
Operator `:=` jest bardzo przydatny w pętlach, szczególnie w przypadku `while`, gdzie przypisanie zmiennej i warunek mogą być połączone.

**Tradycyjny kod:**
```python
data = input("Podaj wartość (lub 'stop' aby przerwać): ")
while data != "stop":
    print(f"Wprowadziłeś: {data}")
    data = input("Podaj wartość (lub 'stop' aby przerwać): ")
```

**Z `:=`:**
```python
while (data := input("Podaj wartość (lub 'stop' aby przerwać): ")) != "stop":
    print(f"Wprowadziłeś: {data}")
```

---

#### **2. Filtry w list comprehensions**
Przydaje się do przypisywania wartości wewnątrz list comprehensions.

**Tradycyjny kod:**
```python
results = []
for item in data:
    size = len(item)
    if size > 3:
        results.append((item, size))
```

**Z `:=`:**
```python
results = [(item, size) for item in data if (size := len(item)) > 3]
```

---

### **Zalety `:=`**

- Skraca kod.
- Unika wielokrotnego wywoływania funkcji (oszczędność zasobów).
- Wspiera bardziej czytelny i zwięzły zapis.

---

### **Kiedy unikać `walrus operator`?**

1. **Zbyt złożone wyrażenia:**
   Jeśli użycie `:=` sprawia, że kod staje się trudny do odczytania, lepiej tego unikać.

2. **Niepotrzebne skróty:**
   W prostych przypadkach lepiej trzymać się tradycyjnego przypisania, aby zachować czytelność.

---

### **Podsumowanie**

**Walrus operator** (`:=`) jest narzędziem, które zwiększa elastyczność i zwięzłość kodu w Pythonie. Jednak jego stosowanie powinno być przemyślane, aby nie utracić przejrzystości kodu. Idealnie sprawdza się w pętlach, list comprehensions i warunkach, gdzie przypisanie i użycie wartości mogą być połączone.