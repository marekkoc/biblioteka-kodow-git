---
Utworzono: 2025-01-08T13:52:00
Zmodyfikowano: 2025-01-08T13:52:00
Źródło: chatGPT
tags: 
Katalog:
---

Ta linia kodu wykonuje zapytanie SQL, które ma na celu pobranie nazw wszystkich tabel znajdujących się w bazie danych SQLite. Przyjrzyjmy się jej szczegółowo.

---

### **Rozbiór składni**

```python
QSqlQuery("SELECT name FROM sqlite_master WHERE type='table'")
```

#### 1. **`QSqlQuery`**:
   - Klasa dostarczona przez moduł `QtSql` w PyQt.
   - Służy do wykonywania zapytań SQL na bazie danych podłączonej za pomocą obiektu `QSqlDatabase`.
   - Tworzenie instancji `QSqlQuery` z ciągiem SQL (np. `"SELECT ..."`) automatycznie wykonuje zapytanie na bieżącym połączeniu z bazą.

#### 2. **`"SELECT name FROM sqlite_master WHERE type='table'"`**:
   - Jest to zapytanie SQL, które korzysta ze specjalnej tabeli systemowej SQLite o nazwie `sqlite_master`.
   - **Tabela `sqlite_master`**:
     - Tabela systemowa SQLite, która przechowuje metadane o wszystkich obiektach w bazie danych (np. tabele, indeksy, widoki, wyzwalacze).
     - Jej kolumny zawierają informacje o tych obiektach:
       - `type`: Typ obiektu (np. `'table'`, `'index'`, `'view'`, `'trigger'`).
       - `name`: Nazwa obiektu (np. tabela lub indeks).
       - `tbl_name`: Nazwa tabeli, do której odnosi się obiekt (dotyczy indeksów i wyzwalaczy).
       - `sql`: Instrukcja SQL użyta do stworzenia obiektu.
   - **`SELECT name FROM sqlite_master`**:
     - Pobiera tylko nazwy (`name`) obiektów z tabeli systemowej.
   - **`WHERE type='table'`**:
     - Filtruje wyniki, aby zwrócić tylko obiekty typu tabela.

---

### **Co robi ten kod?**
- Kod tworzy instancję `QSqlQuery` i wykonuje zapytanie SQL, które zwraca listę nazw wszystkich tabel w bazie danych SQLite.
- Wynikiem zapytania będzie zestaw wierszy zawierających nazwy tabel.

---

### **Przykład działania**

#### **Scenariusz:**
Załóżmy, że baza danych SQLite zawiera następujące tabele:
- `books`
- `authors`
- `publishers`

Tabela systemowa `sqlite_master` może wyglądać tak:

| type  | name         | tbl_name    | sql                                      |
|-------|--------------|-------------|------------------------------------------|
| table | books        | books       | CREATE TABLE books (...)                 |
| table | authors      | authors     | CREATE TABLE authors (...)               |
| table | publishers   | publishers  | CREATE TABLE publishers (...)            |
| index | idx_books    | books       | CREATE INDEX idx_books ON books (...)    |

Zapytanie:

```sql
SELECT name FROM sqlite_master WHERE type='table';
```

Zwróci:

| name       |
|------------|
| books      |
| authors    |
| publishers |

---

### **Użycie wyniku w PyQt**

Po wykonaniu zapytania można iterować po wynikach:

```python
query = QSqlQuery("SELECT name FROM sqlite_master WHERE type='table'")
while query.next():  # Przechodzi przez wszystkie wyniki
    table_name = query.value(0)  # Pobiera nazwę tabeli (pierwsza kolumna)
    print(f"Found table: {table_name}")
```

**Przykładowy wynik w terminalu:**

```
Found table: books
Found table: authors
Found table: publishers
```

---

### **Dlaczego takie zapytanie jest użyteczne?**
1. **Dynamika aplikacji**: Aplikacja może automatycznie wykrywać tabele w bazie danych bez znajomości ich nazw z góry.
2. **Tworzenie interfejsu użytkownika**: Lista tabel może być wyświetlana w GUI, umożliwiając użytkownikowi wybór tabeli do przeglądania lub edycji.
3. **Zarządzanie bazą danych**: Możesz iterować po tabelach i wykonywać na nich operacje, takie jak eksport danych czy migracje.