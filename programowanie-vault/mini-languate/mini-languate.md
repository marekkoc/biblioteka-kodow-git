---
Utworzono: 2025-02-09T13:11:00
Zmodyfikowano: 2025-02-09T13:11:00
Źródło: 
tags: 
Katalog:
---

# Co to jest mini language?


Minilanguage (mini-język) w kontekście formatowania czasu w Pythonie to specjalna składnia używana do określania formatu wyświetlania daty i czasu. W przypadku godzin i minut, jest to część składni strftime()/strptime().

Oto najważniejsze znaczniki dla czasu:

```python
from datetime import datetime

time = datetime.now()

# Przykłady formatowania:
print(f"{time:%H:%M}")  # 14:30 (format 24-godzinny)
print(f"{time:%I:%M %p}")  # 02:30 PM (format 12-godzinny z AM/PM)
```

Najczęściej używane znaczniki dla czasu:
- `%H` - godziny w formacie 24h (00-23)
- `%I` - godziny w formacie 12h (01-12)
- `%M` - minuty (00-59)
- `%S` - sekundy (00-59)
- `%p` - AM/PM
- `%X` - standardowa reprezentacja czasu dla danej lokalizacji

Przykłady praktyczne:
```python
time = datetime(2024, 3, 15, 14, 30, 45)

# Różne formaty wyświetlania
print(f"{time:%H:%M}")      # 14:30
print(f"{time:%H:%M:%S}")   # 14:30:45
print(f"{time:%I:%M %p}")   # 02:30 PM
print(f"{time:%H.%M}")      # 14.30
print(f"{time:%Hh%M}")      # 14h30

# Użycie w klasie ScheduleReport
class ScheduleReport(Report):
    def print_report(self):
        print("Schedule report")
        print("-" * 40)
        for emp in self._emp_list:
            print(f"{emp.get_full_name()}, {emp.start_time:%H:%M} do {emp.end_time:%H:%M}")
```

Zalety używania minilanguage:
1. Standardowy format w Pythonie
2. Czytelny i zwięzły zapis
3. Elastyczność w formatowaniu
4. Możliwość dostosowania do różnych lokalnych formatów
5. Łatwa zmiana formatu bez modyfikacji logiki

Warto pamiętać, że te same znaczniki działają też przy parsowaniu stringów na daty:
```python
from datetime import datetime

# Parsowanie stringa do datetime
time_str = "14:30"
time = datetime.strptime(time_str, "%H:%M")
```

# Czy są inne odmiany mini-language?



Tak, w Pythonie jest kilka rodzajów mini-language. Oto najważniejsze z nich:

1. **Format String Mini-language** (f-stringi i metoda format):
```python
name = "Jan"
age = 30
salary = 5000.50

# Różne sposoby formatowania
print(f"{name:>10}")        # Wyrównanie do prawej na 10 znaków
print(f"{name:<10}")        # Wyrównanie do lewej na 10 znaków
print(f"{name:^10}")        # Wycentrowanie na 10 znaków
print(f"{salary:,.2f}")     # 5,000.50 (separator tysięcy i 2 miejsca po przecinku)
print(f"{salary:>10.2f}")   # Wyrównanie do prawej z 2 miejscami po przecinku
print(f"{age:03d}")         # 030 (dopełnienie zerami)
```

2. **Regular Expression Mini-language** (wyrażenia regularne):
```python
import re

tekst = "Python 3.9"
# Przykłady wzorców:
pattern1 = r"\d+\.\d+"      # Liczby z kropką
pattern2 = r"[A-Za-z]+"     # Ciąg liter
pattern3 = r"\s"            # Biały znak
pattern4 = r"\w+"           # Znaki alfanumeryczne

# Użycie
print(re.findall(pattern1, tekst))  # ['3.9']
print(re.findall(pattern2, tekst))  # ['Python']
```

1. **Path Mini-language** (ścieżki w pathlib):
```python
from pathlib import Path

# Różne operacje na ścieżkach
path = Path("folder") / "plik.txt"  # Łączenie ścieżek
path = Path("~/Documents").expanduser()  # Rozwinięcie ścieżki użytkownika
path = Path("folder").glob("*.txt")  # Wzorzec wyszukiwania plików
```

2. **SQL Mini-language** (w stringach SQL):
```python
# Przykład z SQLAlchemy
query = """
    SELECT *
    FROM employees
    WHERE salary > :min_salary
    AND department = :dept
"""

# Przykład z f-stringami (uwaga: podatne na SQL injection!)
min_salary = 5000
dept = "IT"
query = f"""
    SELECT *
    FROM employees
    WHERE salary > {min_salary}
    AND department = '{dept}'
"""
```

3. **Logging Mini-language** (formatowanie logów):
```python
import logging

# Konfiguracja formatu logów
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)
logger.info("Test message")
# Output: 2024-03-15 14:30:45,123 - __main__ - INFO - Test message
```

4. **String Template Mini-language**:
```python
from string import Template

# Szablony tekstu
template = Template("Witaj $name! Masz $age lat.")
text = template.substitute(name="Jan", age=30)
print(text)  # Witaj Jan! Masz 30 lat.
```

5. **URL Mini-language**:
```python
from urllib.parse import urlparse, urlencode

# Parsowanie URL
url = urlparse("https://example.com/path?key=value")
print(url.scheme)  # https
print(url.netloc)  # example.com
print(url.path)    # /path

# Tworzenie query string
params = {'key1': 'value1', 'key2': 'value2'}
query = urlencode(params)
print(query)  # key1=value1&key2=value2
```

Zalety używania mini-languages:
6. Standardowy sposób formatowania/parsowania
7. Zwięzła i czytelna składnia
8. Mniejsza szansa na błędy
9. Łatwość modyfikacji formatu
10. Dobra dokumentacja
11. Wsparcie w edytorach kodu (podpowiedzi)

Warto pamiętać, że każdy z tych mini-języków ma swoją własną dokumentację i specyficzne przypadki użycia. Warto zapoznać się z dokumentacją konkretnego mini-języka przed jego użyciem.
