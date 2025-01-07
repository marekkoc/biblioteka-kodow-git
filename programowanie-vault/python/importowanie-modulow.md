---
Utworzono: 2024-10-28T11:31:00
Zmodyfikowano: 2024-10-28T11:31:00
Źródło: chatGPT
tags:
  - "#Importowanie-modulow"
---
Moduły w Pythonie powinny być importowane **na początku skryptu** (przed definicją funkcji i klas), co pozwala na lepszą organizację kodu i uniknięcie wielokrotnego importowania tego samego modułu.

### Zalecenia dotyczące importowania modułów:

1. **Importuj na początku skryptu**: Jest to zalecane, ponieważ Python wtedy importuje wszystkie potrzebne moduły raz, przed rozpoczęciem wykonywania kodu. W ten sposób unikamy opóźnień podczas wykonywania funkcji i nie powtarzamy importów.

   ```python
   import os
   import sys

   def my_function():
       # Kod funkcji
       pass
   ```

2. **Import wewnątrz funkcji** – kiedy jest to uzasadnione:
   - Jeśli importowany moduł jest **zasobożerny**, tzn. wymaga dużo pamięci lub ładowanie trwa długo, a potrzebujemy go tylko w jednej funkcji, wtedy warto rozważyć import wewnątrz tej funkcji. 
   - W ten sposób moduł zostanie zaimportowany dopiero w momencie, gdy funkcja zostanie wywołana.

   ```python
   def my_heavy_function():
       import pandas as pd  # import tylko w tej funkcji
       # Kod funkcji, który używa `pandas`
   ```

3. **Zgodność z konwencją PEP 8**: Standard PEP 8 zaleca umieszczanie importów na początku skryptu, w podziale na sekcje:
   - Standardowe moduły Pythona (np. `os`, `sys`).
   - Moduły zainstalowane w środowisku (np. `numpy`, `pandas`).
   - Moduły lokalne projektu (czyli nasze własne moduły).

   ```python
   # Standardowe biblioteki
   import os
   import sys

   # Biblioteki zewnętrzne
   import numpy as np
   import pandas as pd

   # Własne moduły
   from my_module import my_function
   ```

### Podsumowując:
- **Zawsze staraj się importować moduły na początku skryptu**.
- **Importuj w funkcji lub metodzie** tylko wtedy, gdy masz do tego uzasadniony powód (np. optymalizacja wydajności).
