---
Utworzono: 2024-12-28T07:55:00
Zmodyfikowano: 2024-12-28T07:55:00
Źródło: chatGPT
tags:
  - "#sqlalchemy"
Katalog:
---

### **SQLAlchemy – Co to jest?**

**SQLAlchemy** to popularna biblioteka w Pythonie służąca do pracy z bazami danych. Jest to narzędzie typu **ORM** (Object-Relational Mapping) oraz **interfejs do bezpośredniej pracy z SQL**, które pozwala programistom łatwiej zarządzać bazami danych i łączyć je z aplikacjami.

SQLAlchemy jest cenione za swoją elastyczność i skalowalność – można go używać zarówno w prostych projektach, jak i w dużych, zaawansowanych systemach.

---

### **Główne cechy SQLAlchemy**

1. **ORM (Object-Relational Mapper)**:
    
    - Pozwala mapować tabele baz danych na klasy Pythona, a rekordy tabel na obiekty.
    - Ułatwia pracę z danymi w sposób obiektowy, zamiast pisać zapytania SQL.
2. **Core (SQL Expression Language)**:
    
    - SQLAlchemy oferuje również "niższy poziom" interakcji z bazami danych za pomocą SQL, pozwalając na tworzenie bardziej szczegółowych i kontrolowanych zapytań.
3. **Wsparcie dla wielu baz danych**:
    
    - Obsługuje różne systemy bazodanowe, takie jak PostgreSQL, MySQL, SQLite, Oracle, czy Microsoft SQL Server.
4. **Elastyczność**:
    
    - Możesz używać tylko ORM, tylko Core, albo kombinacji obu podejść w zależności od potrzeb projektu.

---

### **Dlaczego warto używać SQLAlchemy?**

1. **Uproszczenie pracy z bazą danych**:
    
    - Zamiast pisać ręczne zapytania SQL, możesz korzystać z bardziej intuicyjnego interfejsu.
2. **Przenośność między bazami danych**:
    
    - Kod napisany w SQLAlchemy jest bardziej przenośny między różnymi typami baz danych.
3. **Bezpieczeństwo**:
    
    - SQLAlchemy automatycznie zarządza wstrzykiwaniem parametrów (ang. _SQL injection_), co zmniejsza ryzyko ataków.
4. **Kompleksowe wsparcie**:
    
    - Obsługuje transakcje, relacje między tabelami, migracje schematów, optymalizacje zapytań itp.

---

### **Przykłady użycia SQLAlchemy**

#### **1. Instalacja**

Aby zainstalować SQLAlchemy, użyj pip:

```bash
pip install sqlalchemy
```

#### **2. Podstawowy przykład z ORM**

**Model (mapowanie klasy na tabelę):**

```python
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# Definicja tabeli jako klasy
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

# Tworzenie bazy danych w SQLite
engine = create_engine('sqlite:///example.db')
Base.metadata.create_all(engine)

# Tworzenie sesji
Session = sessionmaker(bind=engine)
session = Session()

# Dodawanie użytkownika
new_user = User(name="Alice", age=30)
session.add(new_user)
session.commit()

# Pobieranie danych
users = session.query(User).all()
for user in users:
    print(user.name, user.age)
```

**Wyjaśnienie**:

- `Base`: Klasa bazowa dla wszystkich modeli.
- `User`: Klasa reprezentująca tabelę w bazie danych.
- `create_engine`: Tworzy połączenie z bazą danych.
- `session`: Służy do wykonywania operacji na bazie (np. dodawanie, zapytania, usuwanie).

---

#### **3. Praca z Core (niższy poziom pracy z SQL)**

Jeśli chcesz pracować bezpośrednio z SQL:

```python
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

# Połączenie z bazą danych
engine = create_engine('sqlite:///example.db')
metadata = MetaData()

# Definiowanie tabeli
users = Table(
    'users', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('age', Integer)
)
metadata.create_all(engine)

# Dodawanie danych
with engine.connect() as conn:
    conn.execute(users.insert(), {'name': 'Bob', 'age': 40})
```

---

### **Podsumowanie**

SQLAlchemy to potężna biblioteka Python umożliwiająca pracę z bazami danych w sposób obiektowy (ORM) lub za pomocą wyrażeń SQL (Core). Jest szczególnie przydatna w projektach, gdzie potrzebna jest elastyczność, skalowalność i łatwość zarządzania bazami danych.