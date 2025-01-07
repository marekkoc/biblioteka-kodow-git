---
Utworzono: 2024-10-30T12:27:00
Zmodyfikowano: 
Źródło: 
tags:
---

W Pythonie funkcje `__repr__` i `__str__` mają różne zastosowania, choć obie odpowiadają za reprezentację tekstową obiektów.

1. **`__repr__`**:
   - **Cel**: Działa głównie jako reprezentacja obiektu do debugowania i logowania.
   - **Opis**: Powinna zwracać dokładną, jednoznaczną informację o obiekcie – taką, którą moglibyśmy wykorzystać, by odtworzyć ten obiekt w kodzie.
   - **Zastosowanie**: Gdy wykonamy `repr(obj)` lub po prostu wywołamy obiekt w trybie interaktywnym, wywoła się właśnie `__repr__`.
   - **Konwencja**: Jeśli to możliwe, `__repr__` powinna zwracać string, który może być od razu przekazany do funkcji `eval` w celu utworzenia kopii obiektu.

   **Przykład**:
   ```python
   class Point:
       def __init__(self, x, y):
           self.x = x
           self.y = y
       def __repr__(self):
           return f"Point(x={self.x}, y={self.y})"
   
   p = Point(2, 3)
   print(repr(p))   # Wyświetli: Point(x=2, y=3)
   ```

2. **`__str__`**:
   - **Cel**: Jest bardziej przyjazną reprezentacją obiektu, przeznaczoną dla użytkownika.
   - **Opis**: Zwraca string, który reprezentuje obiekt w formie bardziej czytelnej niż `__repr__`, a jego głównym celem jest ułatwienie prezentacji danych.
   - **Zastosowanie**: Funkcja `print(obj)` oraz `str(obj)` wywołają `__str__`. Jeśli nie zaimplementujemy `__str__`, zostanie automatycznie użyta `__repr__`.
   
   **Przykład**:
   ```python
   class Point:
       def __init__(self, x, y):
           self.x = x
           self.y = y
       def __repr__(self):
           return f"Point(x={self.x}, y={self.y})"
       def __str__(self):
           return f"Point at coordinates ({self.x}, {self.y})"
   
   p = Point(2, 3)
   print(str(p))   # Wyświetli: Point at coordinates (2, 3)
   ```

### Różnice między `__repr__` a `__str__` w podsumowaniu
- **`__repr__`**: Przeznaczona do debugowania, dokładna, jednoznaczna reprezentacja obiektu, pomocna dla programistów.
- **`__str__`**: Przyjazna dla użytkownika, uproszczona i czytelna reprezentacja obiektu, używana do wyświetlania danych w bardziej przystępny sposób.