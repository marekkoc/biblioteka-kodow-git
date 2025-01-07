### Created: 2024.12.27
### Modified: 2024.12.27

___
Source: Code with Josh

Episode: [SQL in Python for Beginners](https://www.youtube.com/watch?v=tXJtY51xHq8&t=5s)

Inne: [SQLite tutrial](https://www.sqlitetutorial.net)
___


# Moduł ``main.py``
1. Najpierw w funkcji tworzymy połączenie z bazą danych, a potem to połączenie przekazujemy do wszystkich innych funkcji:


1. Obsługa bazy danych odbywa się przez przekazywanie obiektu `connection` do wszystkich funkcji.
1. Obługa zapytań ``SQL`` z poziomu Pythona odbywa się tak:  
	```try:
        with connection:
            connection.execute(query)
        print("Table was created")
    except Exception as e:
        print(e)```
1. Funkcje do wykonywania zapytan:
	1. ``connection.execute(query)``
	1. ``connection.execute(query, (name, age, email))`` -> argumenty jako krotka
	1. ``rows = connection.execute(query).fetchall()``-> pobiera wszystko
	1. ``connection.execute(query, (user_id,))``-> ważny przecinek na końcu
	1. ``connection.execute(query, (email, user_id))``
	1. ``connection.executemany(query, users)`` -> wykonuje wile razy (users jest listą krotek)


## Funkcje SQL
1. ```query = """CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT NOT NULL, age INTEGER, email TEXT UNIQUE )"""```
1. ```query = "INSERT INTO users (name, age, email) VALUES (?, ?, ?)```
1. ```query = "SELECT * FROM users WHERE {condition}" ```
1. ```query = "DELETE FROM users WHERE id = ?"```
1. ```query = "UPDATE users SET email = ? WHERE id = ?"```
1. ```query = "INSERT INTO users (name, age, email) VALUES (?,?,?)"```

# main-test-1.py

W tej funkcji testowałem działanie warunku ograniczającego wyswietlanie zakresu tabeli.

# mk-test.py

Moduł w którym testuje bazę danych moich książek. Jest to kopia pliku utorznona 27 grudnia 2024 roku.