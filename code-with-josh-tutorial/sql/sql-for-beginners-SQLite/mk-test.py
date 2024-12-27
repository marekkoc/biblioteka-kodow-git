import sqlite3
from icecream import ic


connection = sqlite3.connect("ksiazki.sqlite")
cursor = connection.cursor()
# Wykonanie zapytania do pobrania nazw tabel
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
# Wypisanie wszystkich tabel
tables = cursor.fetchall()
for table in tables:
    ic(table[0])  # Nazwa tabeli znajduje się w pierwszym elemencie krotki
# Zamknięcie połączenia
cursor.close()
connection.close()