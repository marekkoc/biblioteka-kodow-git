Powyższy kod implementuje prosty program w PyQt5, który pozwala otworzyć plik bazy danych SQLite, załadować jej zawartość i wyświetlić dane z pierwszej tabeli w tabeli GUI.

### Kluczowe funkcjonalności:
1. **Przycisk "Open Database"**: Pozwala użytkownikowi wybrać plik SQLite.
2. **Ładowanie danych**: Po otwarciu pliku dane z pierwszej tabeli są wyświetlane w widoku tabeli.
3. **Tabela w GUI**: Dane są prezentowane w interaktywnym widoku tabeli.


```python
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QFileDialog, QMessageBox
)
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

class DatabaseViewer(QWidget):
    def __init__(self):
        super().__init__()

        # Inicjalizacja interfejsu użytkownika
        self.setWindowTitle("SQLite Viewer")
        self.resize(800, 600)

        # Layout główny
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Przycisk otwierania bazy danych
        self.open_button = QPushButton("Open Database")
        self.open_button.clicked.connect(self.open_database)
        self.layout.addWidget(self.open_button)

        # Tabela wyświetlająca dane
        self.table = QTableWidget()
        self.layout.addWidget(self.table)

    def open_database(self):
        """Otwiera plik bazy danych SQLite i wyświetla jego zawartość."""
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Database File", "", "SQLite Files (*.db *.sqlite *.sqlite3);;All Files (*)")

        if not file_path:
            return  # Anulowano wybór pliku

        # Połączenie z bazą danych
        database = QSqlDatabase.addDatabase("QSQLITE")
        database.setDatabaseName(file_path)

        if not database.open():
            QMessageBox.critical(self, "Error", f"Failed to open database: {database.lastError().text()}")
            return

        # Pobranie tabel z bazy danych
        query = QSqlQuery("SELECT name FROM sqlite_master WHERE type='table'")

        if not query.exec_():
            QMessageBox.critical(self, "Error", f"Failed to fetch tables: {query.lastError().text()}")
            return

        tables = []
        while query.next():
            tables.append(query.value(0))

        if not tables:
            QMessageBox.information(self, "No Tables", "The selected database contains no tables.")
            return

        # Załaduj pierwszą tabelę (dla uproszczenia)
        self.load_table_data(tables[0])

    def load_table_data(self, table_name):
        """Ładuje dane z wybranej tabeli do widoku tabeli."""
        query = QSqlQuery(f"SELECT * FROM {table_name}")

        if not query.exec_():
            QMessageBox.critical(self, "Error", f"Failed to fetch data: {query.lastError().text()}")
            return

        # Pobranie nagłówków kolumn
        column_count = query.record().count()
        headers = [query.record().fieldName(i) for i in range(column_count)]

        # Czyszczenie tabeli
        self.table.clear()
        self.table.setColumnCount(column_count)
        self.table.setHorizontalHeaderLabels(headers)

        # Wypełnianie tabeli danymi
        row = 0
        while query.next():
            self.table.insertRow(row)
            for col in range(column_count):
                value = query.value(col)
                self.table.setItem(row, col, QTableWidgetItem(str(value)))
            row += 1

        self.table.resizeColumnsToContents()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewer = DatabaseViewer()
    viewer.show()
    sys.exit(app.exec_())
```

