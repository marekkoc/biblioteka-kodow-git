---
Utworzono: 2024-11-25T09:08:00
Zmodyfikowano: 2024-11-25T09:08:00
Źródło: chatGPT
tags:
---

Dekorator **`@abstractmethod`** jest kluczowym elementem definiowania metod abstrakcyjnych w klasach abstrakcyjnych w Pythonie. Jego obecność wpływa na to, jak zachowuje się klasa abstrakcyjna i jej klasy dziedziczące.

### Dlaczego używamy `@abstractmethod`?

1. **Wymusza implementację w klasach pochodnych**:
    
    - Metoda oznaczona jako `@abstractmethod` musi być zaimplementowana w każdej klasie dziedziczącej.
    - Jeśli klasa dziedzicząca nie zaimplementuje wszystkich metod abstrakcyjnych, sama stanie się klasą abstrakcyjną i nie będzie można utworzyć jej instancji.
2. **Tworzy formalny interfejs**:
    
    - `@abstractmethod` pozwala jasno określić, które metody są obowiązkowe do zaimplementowania przez klasy dziedziczące.
    - To pomaga utrzymać strukturę kodu i ułatwia jego czytelność.

### Czy `@abstractmethod` jest konieczny?

Nie, można utworzyć klasę abstrakcyjną bez użycia `@abstractmethod`. W takim przypadku klasa abstrakcyjna może mieć tylko częściowo zdefiniowane metody (albo nawet pełne implementacje metod), ale **nie będzie wymuszać implementacji żadnych metod w klasach pochodnych**. Taki przypadek może być uzasadniony w zależności od wymagań projektu, ale traci kluczową funkcjonalność, jaką daje `@abstractmethod`.

---

### Przykład z `@abstractmethod`

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

# Próba stworzenia instancji klasy Animal
# animal = Animal()  # Błąd: nie można instancjonować klasy abstrakcyjnej

dog = Dog()  # OK
dog.make_sound()  # Woof!
```

Tutaj `@abstractmethod` wymusza, aby każda klasa dziedzicząca po `Animal` zaimplementowała metodę `make_sound`.

---

### Przykład bez `@abstractmethod`

```python
from abc import ABC

class Animal(ABC):
    def make_sound(self):
        print("Default sound")

class Dog(Animal):
    pass

dog = Dog()
dog.make_sound()  # Default sound
```

Tutaj klasa abstrakcyjna `Animal` nie wymusza implementacji metody `make_sound` w klasie `Dog`. W efekcie `Dog` dziedziczy domyślną implementację metody.

---

### Podsumowanie

- **`@abstractmethod` jest opcjonalny**, ale jeśli zależy nam na wymuszaniu pewnych implementacji w klasach pochodnych, jest konieczny.
- Bez `@abstractmethod` klasa abstrakcyjna działa bardziej jak szablon, który klasy pochodne mogą, ale nie muszą rozszerzać.
- Użycie `@abstractmethod` jest szczególnie przydatne, gdy chcemy tworzyć **interfejsy** lub jasno określone kontrakty dla klas dziedziczących.