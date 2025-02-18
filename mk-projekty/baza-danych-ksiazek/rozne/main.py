"""
Zarzadzanie biblioteka ksiazek.

Created: 2024.12.23
Modified: 2024.12.23
"""
import sqlite3
from icecream import ic

class Book:
    def __init__(self, author, title):
        self.author: str = author
        self.title: str = title

    

books = [
    Book("Angela Duckworth", "Upiór"),
    Book("Zbigniew Lewicki", "Historia Stanów Zjednoczonych Ameryki"),
    Book("Bodo Shafer", "Moge to zrobic")
]

print()
for book in books:
    ic(f"{book.title}")
print()


# Otwieranie bazy danych
database_path = "ksiazki.sqlite"  # Podaj ścieżkę do pliku bazy danych
connection = sqlite3.connect(database_path)
cursor = connection.cursor()

# Pobranie listy tabel w bazie danych
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

if tables:
    print("Tabele w bazie danych:")
    for table in tables:
        print(table[0])
else:
    print("Brak tabel w bazie danych.")

# Zamknięcie połączenia
connection.close()