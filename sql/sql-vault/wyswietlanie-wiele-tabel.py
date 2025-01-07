import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QFileDialog, QMessageBox, QComboBox
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

        # Rozwijana lista tabel
        self.table_selector = QComboBox()
        self.table_selector.currentIndexChanged.connect(self.change_table)
        self.layout.addWidget(self.table_selector)
        self.table_selector.hide()

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

        # Wypełnienie listy rozwijanej nazwami tabel
        self.table_selector.clear()
        self.table_selector.addItems(tables)
        self.table_selector.show()

        # Załaduj pierwszą tabelę domyślnie
        self.load_table_data(tables[0])

    def change_table(self):
        """Zmienia tabelę wyświetlaną w widoku tabeli."""
        table_name = self.table_selector.currentText()
        if table_name:
            self.load_table_data(table_name)

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
        self.table.setRowCount(0)
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
