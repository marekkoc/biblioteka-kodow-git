---
Utworzono: 2025-01-06
Zmodyfikowano: 2025-01-07
Źródło: chatGPT
tags: 
Katalog:
---

# Zapytanie 1
Budowa systemu klas, takich jak klasa **Książka**, z podklasami lub skojarzonymi obiektami, takimi jak **Autor**, **Tytuł**, czy **Opis**, ma sens w określonych przypadkach. Taki system może być szczególnie przydatny, gdy:

### Kiedy warto rozważyć system klas:
1. **Złożoność danych**:
   - Jeśli modelujesz złożone relacje między danymi, np. książki mogą mieć wielu autorów, autorzy mogą napisać wiele książek, a każda książka może być opisana w różnych kategoriach.
   - W takich sytuacjach obiekty odpowiadające rekordom w bazie danych mogą pomóc w zachowaniu przejrzystości kodu.

2. **Logika biznesowa**:
   - Jeśli aplikacja wymaga bardziej skomplikowanej logiki, np. przetwarzania danych, obliczeń lub walidacji, klasy mogą stanowić naturalne miejsce do jej implementacji.

3. **Reużywalność i rozszerzalność**:
   - Klasy umożliwiają łatwe rozszerzanie aplikacji o nowe funkcjonalności i są łatwiejsze w zarządzaniu w większych projektach.

4. **Czytelność i organizacja kodu**:
   - Kiedy chcemy, aby kod był bardziej czytelny, logicznie podzielony na warstwy (np. warstwa modelu, logiki biznesowej, prezentacji), klasy dobrze się sprawdzają.

### Kiedy system klas może być nadmiarowy:
1. **Prosty odczyt i wyświetlanie**:
   - Obecny program ma prostą funkcję: wyświetla dane z bazy. Dodanie klas w takim przypadku mogłoby nadmiernie skomplikować kod.
2. **Brak przetwarzania danych**:
   - Jeśli program tylko odczytuje dane z bazy i nie wykonuje na nich żadnych operacji, klasy mogą być zbędne.

### Jak zaimplementować system klas w obecnym programie?
Możesz wprowadzić klasy reprezentujące tabele w bazie danych (np. Książka, Autor). Oto przykład:

```python
class Book:
    def __init__(self, title, description, authors):
        self.title = title
        self.description = description
        self.authors = authors

class Author:
    def __init__(self, name):
        self.name = name
```

### Przykład wykorzystania:
1. Pobierasz dane z bazy i tworzysz obiekty reprezentujące książki:
   ```python
   books = []
   query = QSqlQuery("SELECT title, description FROM books")
   while query.next():
       title = query.value(0)
       description = query.value(1)
       authors_query = QSqlQuery(f"SELECT name FROM authors WHERE book_title='{title}'")
       authors = [authors_query.value(0) for _ in range(authors_query.size())]
       books.append(Book(title, description, authors))
   ```

2. Wyświetlasz te dane w interfejsie:
   ```python
   for book in books:
       print(f"Title: {book.title}, Authors: {', '.join(book.authors)}")
   ```

### Podsumowanie:
Dodanie klas ma sens, jeśli planujesz rozwijać aplikację o dodatkowe funkcje (np. edycję danych, bardziej skomplikowaną logikę). Jednak dla prostego programu do wyświetlania zawartości baz danych może być to zbyt skomplikowane rozwiązanie.

---

Wprowadzenie systemu klas do programu zarządzającego bazą danych książek pozwala na realizację bardziej zaawansowanych funkcji. Przykłady i możliwe operacje:

---
# Zapytanie 2

### 1. **Złożone relacje i nawigacja między obiektami**

Przy użyciu klas możesz odwzorować relacje między tabelami, np.:
- Książka ma wielu autorów (relacja wiele-do-wielu).
- Każda książka należy do kategorii.
- Każdy autor ma swoją biografię.

**Przykładowe klasy**:
```python
class Book:
    def __init__(self, book_id, title, description, authors):
        self.book_id = book_id
        self.title = title
        self.description = description
        self.authors = authors  # Lista obiektów Author

class Author:
    def __init__(self, author_id, name, biography):
        self.author_id = author_id
        self.name = name
        self.biography = biography
```

**Operacje**:
- Pobieranie listy książek napisanych przez danego autora.
- Znajdowanie wszystkich książek w danej kategorii.

---

### 2. **Filtrowanie i wyszukiwanie danych**

Dodaj logikę do klas, aby implementować funkcje takie jak:
- Wyszukiwanie książek według tytułu, kategorii lub autora.
- Filtracja książek na podstawie roku wydania, popularności itp.

**Przykład wyszukiwania książek przez autora**:
```python
class BookManager:
    def __init__(self, database_connection):
        self.db = database_connection

    def get_books_by_author(self, author_name):
        query = QSqlQuery(f"""
            SELECT books.id, books.title, books.description
            FROM books
            JOIN book_author ON books.id = book_author.book_id
            JOIN authors ON authors.id = book_author.author_id
            WHERE authors.name LIKE '%{author_name}%'
        """)
        books = []
        while query.next():
            books.append(Book(
                book_id=query.value(0),
                title=query.value(1),
                description=query.value(2),
                authors=[]
            ))
        return books
```

---

### 3. **Obsługa logiki biznesowej**

Możesz dodawać metody biznesowe, takie jak:
- Sprawdzenie dostępności książki (np. w bibliotece lub magazynie).
- Rezerwacja książki.
- Wyświetlenie rankingu najczęściej wypożyczanych książek.

**Przykład**:
```python
class Book:
    def is_available(self):
        query = QSqlQuery(f"SELECT available FROM books WHERE id = {self.book_id}")
        if query.next():
            return query.value(0)
        return False
```

---

### 4. **Importowanie i eksportowanie danych**

Dodanie klas ułatwia implementację funkcji:
- Eksport danych do formatu JSON, CSV lub XML.
- Import danych z zewnętrznych źródeł, np. API, plików.

**Przykład eksportu do JSON**:
```python
import json

class Book:
    def to_dict(self):
        return {
            "id": self.book_id,
            "title": self.title,
            "description": self.description,
            "authors": [author.name for author in self.authors]
        }

class BookManager:
    def export_books_to_json(self, books, file_path):
        with open(file_path, 'w') as file:
            json.dump([book.to_dict() for book in books], file, indent=4)
```

---

### 5. **Walidacja danych**

Używając klas, możesz wprowadzić walidację, np.:
- Tytuł książki nie może być pusty.
- Cena musi być liczbą dodatnią.
- Każda książka musi mieć przypisanego autora.

**Przykład walidacji**:
```python
class Book:
    def __init__(self, title, description, authors):
        if not title:
            raise ValueError("Title cannot be empty")
        if not authors:
            raise ValueError("Book must have at least one author")
        self.title = title
        self.description = description
        self.authors = authors
```

---

### 6. **Testowanie i symulacje**

Dzięki klasom łatwiej testować logikę biznesową w izolacji:
- Tworzenie obiektów książek do testów jednostkowych.
- Symulowanie operacji na danych bez połączenia z bazą.

**Przykład testu**:
```python
def test_book_creation():
    author = Author(author_id=1, name="John Doe", biography="Famous author")
    book = Book(book_id=1, title="Sample Book", description="A great book", authors=[author])
    assert book.title == "Sample Book"
```

---

### 7. **Interakcja z zewnętrznymi źródłami danych**

- Pobieranie danych o książkach z zewnętrznego API (np. Google Books API).
- Synchronizacja danych z innym systemem.

---

### Podsumowanie:
Użycie klas w programie zarządzającym bazą danych książek pozwala:
- **Uprościć i uporządkować logikę biznesową**.
- **Wprowadzić bardziej złożone relacje i operacje** na danych.
- **Ułatwić rozwój i utrzymanie kodu** poprzez separację odpowiedzialności.
- **Zapewnić czytelność i reużywalność** kodu.

Jeśli planujesz rozwijać program w kierunku bardziej zaawansowanych funkcji (np. wyszukiwania, walidacji, integracji z API), system klas będzie doskonałym fundamentem.

----
# Zapytanie 3

Masz rację, wiele operacji, takich jak wyszukiwanie, filtrowanie czy relacje między danymi, można zrealizować bezpośrednio za pomocą zapytań SQL w bazie danych. Jednak wprowadzenie systemu klas w kodzie programistycznym ma następujące uzasadnienia i dodatkowe korzyści:

---

### **1. Hermetyzacja logiki biznesowej**
Klasy pozwalają na oddzielenie logiki aplikacji od szczegółów bazy danych. Dzięki temu:
- Możesz łatwo zmieniać strukturę bazy danych bez wpływu na logikę aplikacji.
- Logika aplikacji staje się bardziej przejrzysta i zorganizowana.

Przykład:
- Metoda `Book.get_by_author("John Doe")` może zawierać odpowiednie zapytanie SQL, ale użytkownik klasy nie musi znać szczegółów SQL.

---

### **2. Obsługa danych niezależnie od bazy**
Dzięki klasom dane mogą być obsługiwane jako obiekty, co ułatwia ich manipulację w aplikacji:
- Możesz wczytać dane z bazy do obiektów Python (`Book`, `Author`), a potem na nich operować, np. zmieniać dane, sortować czy filtrować.
- Pozwala to na pracę z danymi w pamięci, co może być szybsze w przypadku operacji wymagających wielu kroków.

---

### **3. Rozszerzalność aplikacji**
Gdy aplikacja rozwija się, klasy pozwalają na łatwe dodawanie nowych funkcji:
- Możesz wprowadzić dodatkowe metody, np. `Book.recommend_similar_books()`, które analizują dane książki i polecają inne książki.
- Możesz zaimplementować logikę wykraczającą poza to, co oferuje SQL, np. algorytmy przetwarzania danych.

---

### **4. Testowanie**
Używając klas, możesz łatwo testować logikę aplikacji bez konieczności interakcji z bazą danych:
- Możesz utworzyć obiekty Python i testować ich zachowanie w izolacji.
- Jest to szczególnie przydatne w testach jednostkowych.

---

### **5. Reużywalność**
Metody zdefiniowane w klasach mogą być używane wielokrotnie w różnych miejscach aplikacji. 
Przykład:
- `Book.save()` — metoda zapisuje dane obiektu książki do bazy danych.
- `Author.list_all_books()` — metoda zwraca wszystkie książki autora.

---

### **6. Składanie danych z różnych źródeł**
Jeśli Twoja aplikacja łączy dane z bazy danych i np. API zewnętrznego (np. Goodreads API), klasy mogą służyć jako warstwa agregująca dane z różnych źródeł.

Przykład:
- Obiekt `Book` może zawierać dane z lokalnej bazy danych oraz dodatkowe informacje, takie jak oceny czy recenzje z API.

---

### **Przykłady zaawansowanych operacji:**
#### Przykład 1: Pobieranie książek z konkretnym autorem i ich edycja:
```python
class Book:
    def __init__(self, book_id, title, description, authors):
        self.book_id = book_id
        self.title = title
        self.description = description
        self.authors = authors  # lista obiektów Author
    
    @staticmethod
    def get_by_author(author_name, db_connection):
        query = QSqlQuery(f"""
            SELECT books.id, books.title, books.description
            FROM books
            JOIN book_author ON books.id = book_author.book_id
            JOIN authors ON authors.id = book_author.author_id
            WHERE authors.name LIKE '%{author_name}%'
        """, db_connection)
        books = []
        while query.next():
            books.append(Book(
                book_id=query.value(0),
                title=query.value(1),
                description=query.value(2),
                authors=[author_name]
            ))
        return books
```

#### Przykład 2: Wyszukiwanie rekomendacji:
```python
class Book:
    def recommend_books(self):
        # Wyszukaj książki w tej samej kategorii, które mają podobny opis
        query = QSqlQuery(f"""
            SELECT id, title, description
            FROM books
            WHERE category = (SELECT category FROM books WHERE id = {self.book_id})
            AND id != {self.book_id}
            LIMIT 5
        """)
        recommendations = []
        while query.next():
            recommendations.append(Book(
                book_id=query.value(0),
                title=query.value(1),
                description=query.value(2),
                authors=[]
            ))
        return recommendations
```

#### Przykład 3: Eksportowanie danych do JSON:
```python
class Book:
    def to_dict(self):
        return {
            "id": self.book_id,
            "title": self.title,
            "description": self.description,
            "authors": self.authors
        }

class Exporter:
    @staticmethod
    def export_books_to_json(books, file_path):
        import json
        with open(file_path, 'w') as file:
            json.dump([book.to_dict() for book in books], file, indent=4)
```

---

### **Podsumowanie**
Chociaż wiele operacji można wykonać za pomocą zapytań SQL, system klas pozwala na:
1. **Lepszą organizację kodu.**
2. **Możliwość pracy na danych jako obiektach.**
3. **Łatwiejsze testowanie i rozwijanie aplikacji.**
4. **Realizację bardziej zaawansowanych funkcji i logiki.**

System klas jest szczególnie przydatny, gdy aplikacja staje się większa lub wymaga przetwarzania danych z wielu źródeł.

---

# Zapytanie 4
Oto bardziej szczegółowe wyjaśnienia dotyczące punktów:

---

### **1. Możesz łatwo zmieniać strukturę bazy danych bez wpływu na logikę aplikacji**
Jeśli używasz klas jako pośrednika między aplikacją a bazą danych, zmiany w strukturze bazy danych (np. dodanie nowej kolumny) są łatwiejsze do zaimplementowania. 

**Przykład**: 
Wyobraź sobie, że dodajesz nową kolumnę `rating` do tabeli `books`. 

- W przypadku samego SQL, musisz zmodyfikować wszystkie miejsca w kodzie, które odnoszą się do tej tabeli.
- Jeśli korzystasz z klas, wystarczy dodać atrybut do klasy `Book` oraz odpowiednią metodę obsługującą ten atrybut.

```python
class Book:
    def __init__(self, title, author, description, rating=None):
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating  # Nowy atrybut

    @staticmethod
    def from_db_row(row):
        return Book(row["title"], row["author"], row["description"], row.get("rating"))
```

Dzięki temu większość logiki aplikacji (np. wyświetlanie książek, edycja danych) nie wymaga zmian, mimo że baza danych została rozszerzona.

---

### **2. Logika aplikacji staje się bardziej przejrzysta i zorganizowana**
SQL często wymaga pisania złożonych zapytań dla bardziej zaawansowanych operacji, co prowadzi do trudnego w utrzymaniu kodu. Klasy pozwalają przenieść tę logikę do metod, które są łatwiejsze do zrozumienia i wielokrotnego użycia.

**Przykład**:
Zamiast używać złożonych zapytań SQL w całej aplikacji:
```sql
SELECT * FROM books WHERE title LIKE '%python%' AND rating > 4
```
Możesz stworzyć metodę w klasie:
```python
class Book:
    @staticmethod
    def find_books_by_criteria(title_contains, min_rating, db):
        query = QSqlQuery(f"""
            SELECT * FROM books 
            WHERE title LIKE '%{title_contains}%' 
              AND rating > {min_rating}
        """, db)
        books = []
        while query.next():
            books.append(Book.from_db_row(query.record()))
        return books
```

Teraz wystarczy wywołać:
```python
books = Book.find_books_by_criteria("python", 4, db_connection)
```

To podejście jest bardziej czytelne i wielokrotnego użytku.

---

### **3. Możesz zaimplementować logikę wykraczającą poza to, co oferuje SQL**
SQL świetnie radzi sobie z wyszukiwaniem, filtrowaniem i agregacją danych, ale nie jest przeznaczony do bardziej złożonych obliczeń lub logiki, takich jak:

- **Rekomendacje**: Wyszukiwanie książek podobnych do tej, którą użytkownik przegląda.
- **Przetwarzanie danych**: Tworzenie zestawień, analizy danych w czasie rzeczywistym, porównywanie zestawów danych.
- **Optymalizacja**: Logika decyzyjna, np. wybór najtańszego dostawcy książek.

**Przykład: Rekomendacje**
SQL może znaleźć książki z tej samej kategorii, ale jeśli chcesz użyć bardziej zaawansowanych algorytmów, takich jak analiza wektorowa opisów książek (np. porównanie słów kluczowych), użyjesz języka Python.

```python
class Book:
    def recommend_similar_books(self, all_books):
        # Porównaj książki na podstawie ich opisu (np. używając Cosine Similarity)
        recommendations = []
        for book in all_books:
            if self.similarity(self.description, book.description) > 0.8:
                recommendations.append(book)
        return recommendations

    def similarity(self, desc1, desc2):
        # Prosty przykład na liczenie podobieństwa (np. Cosine Similarity)
        return cosine_similarity(vectorize(desc1), vectorize(desc2))
```

---

### **4. Klasy jako warstwa agregująca dane z różnych źródeł**
Jeśli aplikacja korzysta z danych z bazy SQLite oraz np. z API zewnętrznego (jak Goodreads), klasy mogą zintegrować dane w jednym miejscu.

**Przykład**:
Chcesz pobrać dane książek z bazy danych i jednocześnie wzbogacić je o oceny z Goodreads API.

```python
class Book:
    def __init__(self, title, author, description, rating=None):
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating

    def fetch_external_rating(self):
        # Połącz się z API Goodreads i pobierz ocenę
        self.rating = get_rating_from_goodreads(self.title, self.author)
```

**Korzystanie:**
```python
book = Book("Python Basics", "John Doe", "Introduction to Python.")
book.fetch_external_rating()
print(f"{book.title} - Goodreads Rating: {book.rating}")
```

To podejście umożliwia:
1. **Łączenie różnych źródeł danych** w jednym obiekcie.
2. **Automatyczne aktualizacje danych** (np. pobieranie ocen w tle).
3. **Spójność danych** — użytkownik aplikacji pracuje z obiektami `Book`, a nie musi martwić się, skąd pochodzą dane.

---

### **Podsumowanie**
Chociaż SQL jest potężnym narzędziem, system klas daje większą elastyczność, modularność i możliwość rozszerzenia aplikacji w przyszłości. Klasy sprawiają, że kod staje się bardziej czytelny, łatwiejszy w utrzymaniu i gotowy na nowe wymagania użytkowników.

---
# Zapytanie 5
Algorytmy przetwarzania danych mogą być zastosowane w różnych scenariuszach, zwłaszcza w kontekście pracy z bazą danych książek. Oto kilka przykładów i potencjalne zastosowania:

---

### **1. Rekomendacje książek**
**Algorytm:** Filtracja treści lub filtracja kolaboracyjna.  
**Zastosowanie:**  
- Polecanie książek użytkownikowi na podstawie jego historii zakupów, wypożyczeń lub ocen.
- Wyszukiwanie książek podobnych pod względem kategorii, autora, słów kluczowych w opisie lub ocen innych użytkowników.

**Przykład:**  
Użytkownik ocenił wysoko książkę "Python Basics". Algorytm może znaleźć książki o podobnych słowach kluczowych w opisie lub te oceniane wysoko przez osoby, które również oceniły "Python Basics".

```python
class BookRecommender:
    @staticmethod
    def recommend_similar_books(target_book, all_books):
        # Prostota: znajdź książki z tej samej kategorii
        return [book for book in all_books if book.category == target_book.category and book != target_book]
```

---

### **2. Klasyfikacja książek na podstawie treści**
**Algorytm:** Klasyfikatory, np. drzewa decyzyjne, SVM, sieci neuronowe.  
**Zastosowanie:**  
- Automatyczne przypisywanie kategorii książkom na podstawie ich opisu.
- Wykrywanie nieprawidłowych danych w bazie, np. błędnie przypisanej kategorii.

**Przykład:**  
Nowa książka została dodana do bazy, ale bez kategorii. Na podstawie analizy jej opisu (np. słów kluczowych) algorytm może przypisać ją do kategorii "Programowanie" lub "Podróże".

```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC

class BookClassifier:
    def __init__(self, books):
        self.vectorizer = TfidfVectorizer()
        self.model = SVC()
        self.train_model(books)

    def train_model(self, books):
        texts = [book.description for book in books]
        categories = [book.category for book in books]
        X = self.vectorizer.fit_transform(texts)
        self.model.fit(X, categories)

    def predict_category(self, description):
        X = self.vectorizer.transform([description])
        return self.model.predict(X)[0]
```

---

### **3. Analiza popularności i trendów**
**Algorytm:** Analiza statystyczna i predykcja (np. regresja).  
**Zastosowanie:**  
- Prognozowanie popularności książek na podstawie ich sprzedaży, wypożyczeń lub ocen w czasie.
- Identyfikacja trendów w popularności autorów, gatunków lub tematów.

**Przykład:**  
Książka "Data Science 101" sprzedaje się coraz lepiej w ostatnich miesiącach. Algorytm może przewidzieć, że będzie jednym z bestsellerów w najbliższym kwartale.

```python
import numpy as np
from sklearn.linear_model import LinearRegression

class TrendAnalyzer:
    @staticmethod
    def predict_sales(sales_data):
        months = np.array([i for i in range(len(sales_data))]).reshape(-1, 1)
        sales = np.array(sales_data).reshape(-1, 1)
        model = LinearRegression().fit(months, sales)
        next_month = np.array([[len(sales_data)]])
        return model.predict(next_month)[0][0]
```

---

### **4. Deduplikacja danych**
**Algorytm:** Porównywanie podobieństwa tekstu (np. Levenshtein distance, Jaccard similarity).  
**Zastosowanie:**  
- Wyszukiwanie i usuwanie zduplikowanych książek w bazie danych.
- Weryfikacja, czy książka o podobnym tytule i autorze nie istnieje już w bazie.

**Przykład:**  
W bazie znajdują się dwie pozycje: "Data Science Basics" i "Data Science Basic". Algorytm może rozpoznać, że to potencjalne duplikaty i oznaczyć je do weryfikacji.

```python
from difflib import SequenceMatcher

class DuplicateFinder:
    @staticmethod
    def find_duplicates(books):
        duplicates = []
        for i, book1 in enumerate(books):
            for j, book2 in enumerate(books):
                if i < j and SequenceMatcher(None, book1.title, book2.title).ratio() > 0.8:
                    duplicates.append((book1, book2))
        return duplicates
```

---

### **5. Analiza sentymentu recenzji**
**Algorytm:** Analiza sentymentu (np. modele NLP).  
**Zastosowanie:**  
- Automatyczne ocenianie nastroju recenzji użytkowników (pozytywny, negatywny, neutralny).
- Grupowanie książek na podstawie opinii, np. książki o dużym odsetku negatywnych recenzji mogą wymagać poprawienia opisu lub reklamy.

**Przykład:**  
Algorytm analizuje recenzje użytkowników i stwierdza, że książka "Machine Learning for Dummies" ma 70% pozytywnych opinii.

```python
from textblob import TextBlob

class SentimentAnalyzer:
    @staticmethod
    def analyze_review_sentiment(review):
        analysis = TextBlob(review)
        if analysis.sentiment.polarity > 0:
            return "Positive"
        elif analysis.sentiment.polarity == 0:
            return "Neutral"
        else:
            return "Negative"
```

---

### **6. Personalizacja dla użytkowników**
**Algorytm:** Systemy rekomendacyjne, np. filtracja kolaboracyjna.  
**Zastosowanie:**  
- Tworzenie spersonalizowanych list książek dla użytkowników na podstawie ich historii przeglądania, ocen lub zakupów.
- Proponowanie książek na podstawie danych demograficznych użytkowników (wiek, zainteresowania).

**Przykład:**  
Użytkownik interesuje się książkami naukowymi. Algorytm sugeruje mu inne książki w tej kategorii, które oceniły wysoko osoby o podobnym profilu.

---

### **7. Zaawansowane filtrowanie danych**
**Algorytm:** Kombinacja logiki Python i SQL.  
**Zastosowanie:**  
- Wyszukiwanie książek na podstawie niestandardowych kryteriów, np. "książki, które mają > 100 stron, były wydane po 2015 roku i należą do kategorii 'Nauka'".

**Przykład:**
```python
class AdvancedFilter:
    @staticmethod
    def filter_books(min_pages, after_year, category, db):
        query = QSqlQuery(f"""
            SELECT * FROM books 
            WHERE pages > {min_pages} 
              AND year > {after_year} 
              AND category = '{category}'
        """, db)
        books = []
        while query.next():
            books.append(Book.from_db_row(query.record()))
        return books
```

---

### **Podsumowanie**
Wykorzystanie algorytmów przetwarzania danych pozwala wyjść poza podstawowe operacje SQL i dodać wartość do aplikacji poprzez lepsze zrozumienie danych, automatyzację procesów, personalizację i zaawansowaną analizę. To kluczowe w projektach, gdzie dane są głównym zasobem i narzędziem dostarczania wartości użytkownikom.

---

# Zapytanie 6
Oto przykład prostego API do obsługi bazy danych SQLite, które można połączyć z powyższym programem. API to pozwala na wykonywanie operacji CRUD (Create, Read, Update, Delete) na bazie danych w sposób bardziej modularny. Możesz je zaimplementować jako osobną klasę lub moduł.

### Przykład klasy API

```python
import sqlite3

class DatabaseAPI:
    def __init__(self, db_path):
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()

    def get_tables(self):
        """Zwraca listę tabel w bazie danych."""
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        return [row[0] for row in self.cursor.fetchall()]

    def get_table_data(self, table_name):
        """Pobiera wszystkie dane z podanej tabeli."""
        self.cursor.execute(f"SELECT * FROM {table_name}")
        columns = [description[0] for description in self.cursor.description]
        data = self.cursor.fetchall()
        return columns, data

    def insert_row(self, table_name, data):
        """Wstawia nowy wiersz do tabeli."""
        placeholders = ", ".join(["?"] * len(data))
        query = f"INSERT INTO {table_name} VALUES ({placeholders})"
        self.cursor.execute(query, data)
        self.connection.commit()

    def update_row(self, table_name, updates, condition):
        """
        Aktualizuje istniejący wiersz w tabeli.
        :param updates: dict, np. {"column_name": "new_value"}
        :param condition: str, np. "id=1"
        """
        set_clause = ", ".join([f"{key} = ?" for key in updates.keys()])
        query = f"UPDATE {table_name} SET {set_clause} WHERE {condition}"
        self.cursor.execute(query, list(updates.values()))
        self.connection.commit()

    def delete_row(self, table_name, condition):
        """Usuwa wiersz z tabeli spełniający podany warunek."""
        query = f"DELETE FROM {table_name} WHERE {condition}"
        self.cursor.execute(query)
        self.connection.commit()

    def close(self):
        """Zamyka połączenie z bazą danych."""
        self.connection.close()
```

### Jak korzystać z API w programie?

Zaktualizuj funkcjonalność swojego programu, aby używać klasy `DatabaseAPI` do komunikacji z bazą danych.

#### Integracja z istniejącym kodem:
1. W metodzie `open_database` inicjalizuj instancję `DatabaseAPI`.
2. Użyj `get_tables` do załadowania nazw tabel.
3. Użyj `get_table_data` do pobierania danych dla wybranej tabeli.

#### Przykład użycia:
```python
from database_api import DatabaseAPI  # Zakładając, że zapisano jako database_api.py

class DatabaseViewer(QWidget):
    def __init__(self):
        super().__init__()
        self.db_api = None  # API bazy danych

    def open_database(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Database File", "", "SQLite Files (*.db *.sqlite *.sqlite3);;All Files (*)")
        if not file_path:
            return

        self.db_api = DatabaseAPI(file_path)
        tables = self.db_api.get_tables()

        if not tables:
            QMessageBox.information(self, "No Tables", "The selected database contains no tables.")
            return

        self.table_selector.clear()
        self.table_selector.addItems(tables)
        self.table_selector.show()

        self.load_table_data(tables[0])

    def load_table_data(self, table_name):
        columns, data = self.db_api.get_table_data(table_name)
        self.table.setColumnCount(len(columns))
        self.table.setHorizontalHeaderLabels(columns)
        self.table.setRowCount(len(data))
        for row_idx, row_data in enumerate(data):
            for col_idx, value in enumerate(row_data):
                self.table.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))

    def closeEvent(self, event):
        if self.db_api:
            self.db_api.close()
        event.accept()
```

Dzięki temu podejściu logika pracy z bazą danych jest oddzielona od logiki GUI, co sprawia, że kod jest bardziej modularny i łatwiejszy do utrzymania.

----


# Zapytanie 7

### Proponowana struktura klas do zarządzania bazą danych książek

Bazując na opisanych kolumnach w Twojej bazie danych, możesz podzielić je na klasy w celu lepszego zarządzania logiką aplikacji oraz umożliwienia bardziej złożonych operacji. 

#### Struktura klas

1. **Book**: Reprezentuje pojedynczą książkę.
2. **Author**: Reprezentuje autora książki.
3. **BookSeries**: Reprezentuje serię książek.
4. **Publisher**: Reprezentuje wydawnictwo.
5. **BookDatabaseManager**: Odpowiada za zarządzanie operacjami na bazie danych.

#### Przykładowa implementacja

```python
from typing import Optional, List
import sqlite3

class Author:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name

class Publisher:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name

class BookSeries:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name

class Book:
    def __init__(self, title: str, author: Author, publisher: Publisher, series: Optional[BookSeries] = None,
                 year: Optional[int] = None, format: Optional[str] = None, price: Optional[float] = None,
                 read: bool = False, read_start: Optional[str] = None, read_end: Optional[str] = None,
                 paper_version: bool = False, notes: Optional[str] = None):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.series = series
        self.year = year
        self.format = format
        self.price = price
        self.read = read
        self.read_start = read_start
        self.read_end = read_end
        self.paper_version = paper_version
        self.notes = notes

    def __str__(self):
        return f"'{self.title}' by {self.author}"

class BookDatabaseManager:
    def __init__(self, db_path: str):
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()

    def create_tables(self):
        """Tworzy tabelę książek w bazie danych."""
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            author TEXT,
            series TEXT,
            publisher TEXT,
            year INTEGER,
            format TEXT,
            price REAL,
            read BOOLEAN,
            read_start DATE,
            read_end DATE,
            paper_version BOOLEAN,
            notes TEXT
        )
        """)
        self.connection.commit()

    def add_book(self, book: Book):
        """Dodaje książkę do bazy danych."""
        self.cursor.execute("""
        INSERT INTO books (title, author, series, publisher, year, format, price, read, read_start, read_end, paper_version, notes)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            book.title,
            book.author.name,
            book.series.name if book.series else None,
            book.publisher.name,
            book.year,
            book.format,
            book.price,
            book.read,
            book.read_start,
            book.read_end,
            book.paper_version,
            book.notes
        ))
        self.connection.commit()

    def get_books(self) -> List[Book]:
        """Pobiera wszystkie książki z bazy danych."""
        self.cursor.execute("SELECT * FROM books")
        rows = self.cursor.fetchall()
        books = []
        for row in rows:
            books.append(Book(
                title=row[1],
                author=Author(row[2]),
                series=BookSeries(row[3]) if row[3] else None,
                publisher=Publisher(row[4]),
                year=row[5],
                format=row[6],
                price=row[7],
                read=bool(row[8]),
                read_start=row[9],
                read_end=row[10],
                paper_version=bool(row[11]),
                notes=row[12]
            ))
        return books

    def close(self):
        """Zamyka połączenie z bazą danych."""
        self.connection.close()
```

#### Przykładowe użycie

```python
if __name__ == "__main__":
    db_manager = BookDatabaseManager("books.db")
    db_manager.create_tables()

    author = Author("J.K. Rowling")
    publisher = Publisher("Bloomsbury")
    series = BookSeries("Harry Potter")

    book = Book(
        title="Harry Potter and the Philosopher's Stone",
        author=author,
        publisher=publisher,
        series=series,
        year=1997,
        format="Hardcover",
        price=19.99,
        read=True,
        read_start="2023-01-01",
        read_end="2023-01-15",
        paper_version=True,
        notes="First edition"
    )

    db_manager.add_book(book)
    books = db_manager.get_books()
    for b in books:
        print(b)

    db_manager.close()
```

### Korzyści

- **Modularność**: Klasy oddzielają różne aspekty danych (np. autorzy, wydawcy, serie).
- **Reużywalność**: Możesz wielokrotnie używać klas `Author`, `Publisher`, itp. w innych kontekstach.
- **Rozszerzalność**: Łatwo dodać nowe właściwości lub funkcje (np. licznik czytelników dla książek).
- **Złożona logika**: Możesz zaimplementować operacje takie jak filtrowanie książek według autora, serii, czy roku.

# Zapytanie 8
Oczywiście, możemy kontynuować! 😊 Jakie aspekty bazy danych książek chciałbyś omówić dalej? Możemy zgłębić:

- Złożoną logikę aplikacji i operacje na danych.
- Rozszerzenie struktury klas.
- Interakcję z GUI (np. w PyQt5).
- Wydajność zapytań do bazy danych.
- Synchronizację danych z zewnętrznymi API (np. Goodreads, Open Library).
- Praktyki związane z migracją danych lub backupem bazy danych.

Daj znać, co Cię najbardziej interesuje!

# Zapytanie 9

Twoje pytanie o strukturę bazy danych jest bardzo istotne i kluczowe dla wydajności oraz elastyczności aplikacji. Rozważmy najpierw, jak można rozdzielić dane z bazy książek na różne tabele i jak je ze sobą powiązać.

---

### 1. **Czy jedna tabela wystarczy?**

Jedna tabela może być wystarczająca dla prostych przypadków użycia, ale:

- Trudno ją rozbudowywać w przyszłości.
- Duplikujesz dane (np. ten sam autor czy wydawnictwo mogą występować wielokrotnie).
- Trudniej unikać błędów, takich jak literówki w danych.

Dlatego w bardziej rozbudowanych aplikacjach stosuje się podejście relacyjne, w którym dane dzielone są na wiele tabel.

---

### 2. **Propozycja struktury wielotabelowej**

Możesz podzielić dane na logiczne części i utworzyć tabele z powiązaniami między nimi. Przykładowa struktura:

#### a) **Tabela `books` (Książki)**
Reprezentuje unikalne książki:
- `id` (klucz główny, PRIMARY KEY)
- `title` (tytuł książki)
- `author_id` (klucz obcy do tabeli `authors`)
- `publisher_id` (klucz obcy do tabeli `publishers`)
- `series_id` (klucz obcy do tabeli `series`)
- `year` (rok wydania)
- `format` (np. "PDF", "EPUB", "Paperback")
- `genre` (np. "Fiction", "Non-Fiction")
- `is_read` (czy książka była czytana, boolean)
- `notes` (uwagi)

#### b) **Tabela `authors` (Autorzy)**
Zawiera dane o autorach:
- `id` (klucz główny)
- `name` (imię i nazwisko autora)

#### c) **Tabela `publishers` (Wydawnictwa)**
Zawiera dane o wydawnictwach:
- `id` (klucz główny)
- `name` (nazwa wydawnictwa)

#### d) **Tabela `series` (Serie książek)**
Zawiera dane o seriach książkowych:
- `id` (klucz główny)
- `name` (nazwa serii)

#### e) **Tabela `bookshops` (Księgarnie)**
Rejestruje miejsca zakupu:
- `id` (klucz główny)
- `name` (nazwa księgarni)

#### f) **Tabela `purchases` (Zakupy)**
Łączy książki z informacjami o zakupach:
- `id` (klucz główny)
- `book_id` (klucz obcy do tabeli `books`)
- `bookshop_id` (klucz obcy do tabeli `bookshops`)
- `purchase_date` (data zakupu)
- `price` (cena)

#### g) **Tabela `reading_log` (Log czytania)**
Zawiera dane o procesie czytania:
- `id` (klucz główny)
- `book_id` (klucz obcy do tabeli `books`)
- `read_from` (data rozpoczęcia czytania)
- `read_to` (data zakończenia czytania)

---

### 3. **Powiązania między tabelami**

#### Relacje:
- **`books` → `authors`**: Jeden autor może napisać wiele książek (relacja *wiele do jednego*).
- **`books` → `publishers`**: Jedno wydawnictwo może opublikować wiele książek (relacja *wiele do jednego*).
- **`books` → `series`**: Jedna seria może zawierać wiele książek, ale książka należy do jednej serii (relacja *wiele do jednego*).
- **`purchases` → `books`**: Jedna książka może być kupiona w wielu miejscach, jeśli np. posiadasz różne wydania (relacja *wiele do jednego*).
- **`reading_log` → `books`**: Dla jednej książki możesz mieć wiele logów czytania, np. przy powtórnym czytaniu (relacja *jeden do wielu*).

---

### 4. **Jak powinny współpracować tabele?**

- **Unikanie duplikacji**: Dzięki podzieleniu na tabele np. `authors`, `publishers`, czy `series`, dane powtarzalne zapisujesz tylko raz.
- **Optymalizacja zapytań**: Możesz pobrać szczegółowe dane np. o książkach i ich autorach jednym zapytaniem z JOIN:
  ```sql
  SELECT books.title, authors.name AS author, publishers.name AS publisher, series.name AS series
  FROM books
  JOIN authors ON books.author_id = authors.id
  JOIN publishers ON books.publisher_id = publishers.id
  LEFT JOIN series ON books.series_id = series.id;
  ```
- **Łatwość rozwijania**: Możesz dodawać nowe kolumny lub tabele bez zmiany logiki w już istniejących tabelach.

---

### 5. **Zalety podejścia wielotabelowego**
- **Modularność**: Możesz łatwo dodawać nowe funkcjonalności, np. tabelę do oceniania książek.
- **Redukcja błędów**: Literówki w nazwach autorów czy wydawnictw są wyeliminowane dzięki używaniu kluczy obcych.
- **Wydajność**: Tabele są mniejsze i bardziej zrozumiałe, co przyspiesza operacje na danych.

---

Czy chciałbyś, abym zaprojektował SQL dla takiej struktury, a może przedstawił, jak zaimplementować klasy w Pythonie odzwierciedlające tę bazę danych? 😊

# Zapytanie 10

Świetnie! Oto szczegółowy plan na zaprojektowanie systemu zarządzania bazą danych książek z użyciem SQLite i klas w Pythonie.

---

## **1. Struktura bazy danych (SQL)**

```sql
-- Tabela autorów
CREATE TABLE authors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

-- Tabela wydawnictw
CREATE TABLE publishers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

-- Tabela serii książek
CREATE TABLE series (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
);

-- Tabela księgarni
CREATE TABLE bookshops (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

-- Tabela książek
CREATE TABLE books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author_id INTEGER,
    publisher_id INTEGER,
    series_id INTEGER,
    year INTEGER,
    format TEXT,
    genre TEXT,
    is_read BOOLEAN DEFAULT 0,
    notes TEXT,
    FOREIGN KEY (author_id) REFERENCES authors (id),
    FOREIGN KEY (publisher_id) REFERENCES publishers (id),
    FOREIGN KEY (series_id) REFERENCES series (id)
);

-- Tabela zakupów książek
CREATE TABLE purchases (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_id INTEGER NOT NULL,
    bookshop_id INTEGER NOT NULL,
    purchase_date DATE,
    price REAL,
    FOREIGN KEY (book_id) REFERENCES books (id),
    FOREIGN KEY (bookshop_id) REFERENCES bookshops (id)
);

-- Tabela logów czytania
CREATE TABLE reading_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_id INTEGER NOT NULL,
    read_from DATE,
    read_to DATE,
    FOREIGN KEY (book_id) REFERENCES books (id)
);
```

---

## **2. Klasy w Pythonie**

W Pythonie zaimplementujemy klasy odzwierciedlające strukturę bazy danych. Wykorzystamy bibliotekę `sqlite3` do komunikacji z bazą danych.

```python
import sqlite3
from datetime import date


class Author:
    def __init__(self, name, author_id=None):
        self.id = author_id
        self.name = name

    @staticmethod
    def create_table(connection):
        with connection:
            connection.execute("""
                CREATE TABLE IF NOT EXISTS authors (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL
                )
            """)

    def save(self, connection):
        with connection:
            if self.id is None:
                cursor = connection.execute(
                    "INSERT INTO authors (name) VALUES (?)",
                    (self.name,)
                )
                self.id = cursor.lastrowid
            else:
                connection.execute(
                    "UPDATE authors SET name = ? WHERE id = ?",
                    (self.name, self.id)
                )


class Book:
    def __init__(self, title, author_id, publisher_id=None, series_id=None,
                 year=None, book_format=None, genre=None, is_read=False, notes=None, book_id=None):
        self.id = book_id
        self.title = title
        self.author_id = author_id
        self.publisher_id = publisher_id
        self.series_id = series_id
        self.year = year
        self.format = book_format
        self.genre = genre
        self.is_read = is_read
        self.notes = notes

    @staticmethod
    def create_table(connection):
        with connection:
            connection.execute("""
                CREATE TABLE IF NOT EXISTS books (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    author_id INTEGER,
                    publisher_id INTEGER,
                    series_id INTEGER,
                    year INTEGER,
                    format TEXT,
                    genre TEXT,
                    is_read BOOLEAN DEFAULT 0,
                    notes TEXT,
                    FOREIGN KEY (author_id) REFERENCES authors (id),
                    FOREIGN KEY (publisher_id) REFERENCES publishers (id),
                    FOREIGN KEY (series_id) REFERENCES series (id)
                )
            """)

    def save(self, connection):
        with connection:
            if self.id is None:
                cursor = connection.execute("""
                    INSERT INTO books (
                        title, author_id, publisher_id, series_id, year,
                        format, genre, is_read, notes
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (self.title, self.author_id, self.publisher_id, self.series_id,
                      self.year, self.format, self.genre, self.is_read, self.notes))
                self.id = cursor.lastrowid
            else:
                connection.execute("""
                    UPDATE books
                    SET title = ?, author_id = ?, publisher_id = ?, series_id = ?,
                        year = ?, format = ?, genre = ?, is_read = ?, notes = ?
                    WHERE id = ?
                """, (self.title, self.author_id, self.publisher_id, self.series_id,
                      self.year, self.format, self.genre, self.is_read, self.notes, self.id))


class Purchase:
    def __init__(self, book_id, bookshop_id, purchase_date=None, price=None, purchase_id=None):
        self.id = purchase_id
        self.book_id = book_id
        self.bookshop_id = bookshop_id
        self.purchase_date = purchase_date or date.today().isoformat()
        self.price = price

    @staticmethod
    def create_table(connection):
        with connection:
            connection.execute("""
                CREATE TABLE IF NOT EXISTS purchases (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    book_id INTEGER NOT NULL,
                    bookshop_id INTEGER NOT NULL,
                    purchase_date DATE,
                    price REAL,
                    FOREIGN KEY (book_id) REFERENCES books (id),
                    FOREIGN KEY (bookshop_id) REFERENCES bookshops (id)
                )
            """)

    def save(self, connection):
        with connection:
            if self.id is None:
                cursor = connection.execute("""
                    INSERT INTO purchases (book_id, bookshop_id, purchase_date, price)
                    VALUES (?, ?, ?, ?)
                """, (self.book_id, self.bookshop_id, self.purchase_date, self.price))
                self.id = cursor.lastrowid
            else:
                connection.execute("""
                    UPDATE purchases
                    SET book_id = ?, bookshop_id = ?, purchase_date = ?, price = ?
                    WHERE id = ?
                """, (self.book_id, self.bookshop_id, self.purchase_date, self.price, self.id))
```

---

## **3. Inicjalizacja bazy danych**

```python
def initialize_database(connection):
    Author.create_table(connection)
    Book.create_table(connection)
    Purchase.create_table(connection)
    # Dodaj funkcje dla innych klas, np. Publisher, Series
```

---

## **4. Przykład użycia**

```python
def main():
    connection = sqlite3.connect("books.db")

    # Inicjalizacja bazy danych
    initialize_database(connection)

    # Dodanie autora
    author = Author(name="George Orwell")
    author.save(connection)

    # Dodanie książki
    book = Book(title="1984", author_id=author.id, year=1949, genre="Dystopia", is_read=True)
    book.save(connection)

    # Dodanie zakupu
    purchase = Purchase(book_id=book.id, bookshop_id=1, price=25.99)
    purchase.save(connection)

    print(f"Book '{book.title}' by {author.name} saved with ID {book.id}")


if __name__ == "__main__":
    main()
```

---

## **Podsumowanie**

- **Struktura SQL** jest przejrzysta i pozwala na unikanie redundancji.
- **Klasy w Pythonie** oferują prosty sposób na zarządzanie rekordami.
- System można łatwo rozszerzać o dodatkowe funkcjonalności, takie jak logi czytania czy integracje z API.

Czy chciałbyś coś jeszcze dopracować? 😊

# Zapytanie 11
Oczywiście! Oto uproszczona wersja systemu z trzema tabelami oraz szczegółowe wyjaśnienie działania i wstawiania rekordów.

---

## **1. Uproszczona Struktura Bazy Danych**

Baza danych będzie zawierała:
1. **Tabela `authors`** - przechowuje autorów książek.
2. **Tabela `books`** - przechowuje książki i wskazuje autora (relacja jeden-do-wielu).
3. **Tabela `purchases`** - przechowuje informacje o zakupach książek.

### Struktura SQL:
```sql
-- Tabela autorów
CREATE TABLE authors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

-- Tabela książek
CREATE TABLE books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author_id INTEGER NOT NULL,
    FOREIGN KEY (author_id) REFERENCES authors (id)
);

-- Tabela zakupów
CREATE TABLE purchases (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_id INTEGER NOT NULL,
    purchase_date DATE,
    price REAL,
    FOREIGN KEY (book_id) REFERENCES books (id)
);
```

---

## **2. Klasy w Pythonie**

### Implementacja:

```python
import sqlite3
from datetime import date

class Author:
    def __init__(self, name, author_id=None):
        self.id = author_id
        self.name = name

    def save(self, connection):
        """Zapisuje autora w bazie danych."""
        with connection:
            if self.id is None:
                cursor = connection.execute(
                    "INSERT INTO authors (name) VALUES (?)",
                    (self.name,)
                )
                self.id = cursor.lastrowid
            else:
                connection.execute(
                    "UPDATE authors SET name = ? WHERE id = ?",
                    (self.name, self.id)
                )

class Book:
    def __init__(self, title, author_id, book_id=None):
        self.id = book_id
        self.title = title
        self.author_id = author_id

    def save(self, connection):
        """Zapisuje książkę w bazie danych."""
        with connection:
            if self.id is None:
                cursor = connection.execute(
                    "INSERT INTO books (title, author_id) VALUES (?, ?)",
                    (self.title, self.author_id)
                )
                self.id = cursor.lastrowid
            else:
                connection.execute(
                    "UPDATE books SET title = ?, author_id = ? WHERE id = ?",
                    (self.title, self.author_id, self.id)
                )

class Purchase:
    def __init__(self, book_id, purchase_date=None, price=None, purchase_id=None):
        self.id = purchase_id
        self.book_id = book_id
        self.purchase_date = purchase_date or date.today().isoformat()
        self.price = price

    def save(self, connection):
        """Zapisuje zakup w bazie danych."""
        with connection:
            if self.id is None:
                cursor = connection.execute(
                    "INSERT INTO purchases (book_id, purchase_date, price) VALUES (?, ?, ?)",
                    (self.book_id, self.purchase_date, self.price)
                )
                self.id = cursor.lastrowid
            else:
                connection.execute(
                    "UPDATE purchases SET book_id = ?, purchase_date = ?, price = ? WHERE id = ?",
                    (self.book_id, self.purchase_date, self.price, self.id)
                )
```

---

## **3. Przykład działania**

### Inicjalizacja bazy danych:
```python
def initialize_database(connection):
    with connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS authors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
        """)
        connection.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author_id INTEGER NOT NULL,
                FOREIGN KEY (author_id) REFERENCES authors (id)
            )
        """)
        connection.execute("""
            CREATE TABLE IF NOT EXISTS purchases (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                book_id INTEGER NOT NULL,
                purchase_date DATE,
                price REAL,
                FOREIGN KEY (book_id) REFERENCES books (id)
            )
        """)
```

### Dodawanie danych:
Przykład wstawiania rekordów do bazy danych:

```python
def main():
    connection = sqlite3.connect("simple_books.db")
    initialize_database(connection)

    # Dodajemy autora
    author = Author(name="George Orwell")
    author.save(connection)
    print(f"Author added with ID: {author.id}")

    # Dodajemy książkę
    book = Book(title="1984", author_id=author.id)
    book.save(connection)
    print(f"Book added with ID: {book.id}")

    # Dodajemy zakup
    purchase = Purchase(book_id=book.id, price=29.99)
    purchase.save(connection)
    print(f"Purchase added with ID: {purchase.id}")

if __name__ == "__main__":
    main()
```

---

## **4. Wyjaśnienie Działania**

### 1. Dodanie autora
- Kiedy wywołujemy `author.save(connection)`, system wykonuje SQL:
  ```sql
  INSERT INTO authors (name) VALUES ('George Orwell');
  ```
- SQLite generuje unikalny `id` dla tego autora, który jest dostępny jako `author.id`.

### 2. Dodanie książki
- Gdy dodajemy książkę `1984`, wskazujemy, że należy do autora o `id=1`:
  ```sql
  INSERT INTO books (title, author_id) VALUES ('1984', 1);
  ```
- Klasa `Book` przechowuje odniesienie do `author_id`, co tworzy powiązanie.

### 3. Dodanie zakupu
- Tworzymy zakup książki `1984` (z `id=1`):
  ```sql
  INSERT INTO purchases (book_id, purchase_date, price) VALUES (1, '2025-01-06', 29.99);
  ```

---

## **5. Przykład w bazie danych**

### Tabela `authors`:
| id  | name           |
|-----|----------------|
| 1   | George Orwell  |

### Tabela `books`:
| id  | title  | author_id |
|-----|--------|-----------|
| 1   | 1984   | 1         |

### Tabela `purchases`:
| id  | book_id | purchase_date | price |
|-----|---------|---------------|-------|
| 1   | 1       | 2025-01-06    | 29.99 |

---

Dzięki relacjom między tabelami możemy w łatwy sposób łączyć dane, np.:
- Lista wszystkich książek autorów:
  ```sql
  SELECT books.title, authors.name
  FROM books
  JOIN authors ON books.author_id = authors.id;
  ```
- Suma wydatków:
  ```sql
  SELECT SUM(price) FROM purchases;
  ```

Jeśli potrzebujesz dodatkowych przykładów lub szczegółowego wyjaśnienia, daj znać! 😊