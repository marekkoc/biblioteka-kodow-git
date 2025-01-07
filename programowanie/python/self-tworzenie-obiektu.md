---
Utworzono: 2024-11-06T14:48:00
Zmodyfikowano: 2024-11-06T14:48:00
Źródło: 
tags:
---

W Pythonie, podczas tworzenia obiektu klasy, nie podajemy parametru `self`, ponieważ jest on automatycznie obsługiwany przez język. Wyjaśnijmy dokładnie, jak to działa:

### Co to jest `self`?
- W metodach klasy `self` reprezentuje instancję, na której dana metoda jest wywoływana. 
- `self` umożliwia dostęp do atrybutów i innych metod tej konkretnej instancji. 
- Jest to tylko konwencja — można by użyć innej nazwy, ale `self` jest standardem, który czyni kod bardziej czytelnym.

### Dlaczego `self` nie jest podawany przy tworzeniu obiektu?
Kiedy tworzymy nową instancję klasy w Pythonie (na przykład `my_obj = MyClass()`), Python:
1. **Tworzy nową instancję** klasy `MyClass`.
2. **Automatycznie przekazuje tę instancję** jako pierwszy argument (`self`) do metody `__init__`, gdy jest ona wywoływana.

### Przykład: jak to działa
Zobaczmy przykład:

```python
class MyClass:
    def __init__(self, name):
        self.name = name  # Ustawiamy atrybut instancji name

obj = MyClass("Alice")
```

W momencie tworzenia `obj`:
- Python tworzy nową instancję `MyClass`.
- Wywołuje `__init__`, przekazując nowo utworzony obiekt jako `self` oraz `"Alice"` jako `name`.
- `self` jest przekazywane automatycznie, więc przy tworzeniu obiektu `obj = MyClass("Alice")` podajemy tylko wartość `"Alice"` jako argument metody `__init__`.

### Dlaczego to działa w ten sposób?
Dzięki temu możemy skupić się na przekazywaniu tylko parametrów specyficznych dla obiektu. Python automatycznie obsługuje `self` jako odniesienie do obiektu, co ułatwia zarządzanie instancjami oraz pozwala programistom pisać bardziej czytelny kod.