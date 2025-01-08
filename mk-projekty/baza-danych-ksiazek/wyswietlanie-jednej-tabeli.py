"""

Kod na podstawie notatki: baza-danych-ksiazwk-wyswietlanie-jednej-tabeli.md
Kod wygenerowany przez ChatGPT.


Created: 2025.01.07
Modified: 2025.01.08
"""

import sys
from icecream import ic

from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QTableWidget, 
    QTableWidgetItem, QFileDialog, QMessageBox
)
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

class DatabaseViewer(QWidget):
    def __init__(self):
        super().__init__()

        # Inicjalizacja interfejsu użytkownika
        self.setWindowTitle("SQLite Viewer")
        self.resize(800, 600)

        # Layout główny
        self.layout: QVBoxLayout = QVBoxLayout()
        self.setLayout(self.layout)

        # Przycisk otwierania bazy danych
        self.open_button: QPushButton = QPushButton("Open Database")
        self.open_button.clicked.connect(self.open_database)
        self.layout.addWidget(self.open_button)

        # Tabela wyświetlająca dane
        self.table: QTableWidget = QTableWidget()
        self.layout.addWidget(self.table)

    
    def open_database(self):
        "Open an SQLite database and display its contetnt"

        def_path: str = "/home/marek/biblioteka-repozytoriow-git/biblioteka-kodow-git/mk-projekty/baza-danych-ksiazek"
        
        file_path : str
        selected_filter: str
        file_path, selected_filter = QFileDialog.getOpenFileName(self, "Select Database File", def_path, "SQLite Files (*.db *.sqlite *.sqlite3);; All Files (*)")

        if not file_path:
            return # Anulowano otwieranie pliku
        
        # Połączenie z bazą danych
        database: QSqlDatabase = QSqlDatabase.addDatabase("QSQLITE")
        database.setDatabaseName(file_path)

        # Then call open() to activate the physical connection to the database.
        #  The connection is not usable until you open it.
        if not database.open():
            QMessageBox.critical(self, "Error", f"Failed to open database: {database.lastError().text()}.")
            return

        # Pobieranie tabel z bazy danych
        query: QSqlQuery = QSqlQuery("SELECT name FROM sqlite_master WHERE type='table'")

        if not query.exec_():
            QMessageBox.critical(self, "Error", f"Failed to fetch tables:\n{query.lastError().text()}.")
            return

        tables: list[str] = []
        while query.next():
            tables.append(query.value(0))

        if not tables:
            QMessageBox.information(self, "No Tables", "The selected database contains no tables.")
            return

        # Załaduj pierwszą tabelę (dla uproszczenia wybieramy pierwszą)
        self.load_table_data(tables[0])



    def load_table_data(self, table_name):
        "Ładuje dane z wybranej tabeli do widoku tabeli."
        query: QSqlQuery = QSqlQuery(f"SELECT * FROM {table_name}")

        if not query.exec_():
            QMessageBox.critical(self, "Error", f"Failed to fetch data: {query.lastError().text()}.")
            return

        # Pobieranie nagłówków kolumn
        column_count: int = query.record().count()
        headers: list[str] = [query.record().fieldName(i) for i in range(column_count)]
        
        # Czyszczenie tabeli
        self.table.clear()
        self.table.setColumnCount(column_count)
        self.table.setHorizontalHeaderLabels(headers)

        # Wypełnianie tabeli danymi
        row: int = 0
        while query.next():
            self.table.insertRow(row)
            for col in range(column_count):
                value = query.value(col)
                self.table.setItem(row, col, QTableWidgetItem(str(value)))
            row += 1

        # Problem polega na tym, że wywołanie 
        # self.table.resizeColumnsToContents() zmienia tylko
        #  szerokość kolumn w tabeli, ale nie wpływa na rozmiar
        # okna aplikacji. Jeśli chcesz, aby okno automatycznie
        #  dopasowało się do rozmiaru zawartości tabeli, musisz
        #  dynamicznie zmienić rozmiar okna aplikacji.
        # Dodaj wywołanie adjustSize()
        # do głównego widżetu i tabeli po załadowaniu danych:        
        self.table.resizeColumnsToContents()

        # Dopasowanie rozmiaru okna
        # Dopasowanie kolumn do zawartości
        self.adjust_table_and_window_size()

    def adjust_table_and_window_size(self):
        """Dopasowuje rozmiar tabeli i ustawia okno aplikacji jako skalowalne."""
        self.table.resizeColumnsToContents()

        # Ustawienie maksymalnej szerokości kolumn, aby zapobiec nadmiernemu rozszerzaniu
        for col in range(self.table.columnCount()):
            self.table.setColumnWidth(col, min(self.table.columnWidth(col), 300))

        # Oblicz rozmiar tabeli
        table_width = (
            self.table.horizontalHeader().length() +
            self.table.verticalScrollBar().sizeHint().width()
        )
        table_height = (
            self.table.verticalHeader().length() +
            self.table.horizontalHeader().height() +
            self.table.horizontalScrollBar().sizeHint().height()
        )

        # Pobierz wymiary ekranu i oblicz maksymalne rozmiary okna
        screen_geometry = QApplication.primaryScreen().geometry()
        screen_width = screen_geometry.width()
        screen_height = screen_geometry.height()

        max_width = int(screen_width * 0.8)  # 80% szerokości ekranu
        max_height = int(screen_height * 0.8)  # 80% wysokości ekranu

        # Ustawienia maksymalnych wymiarów dla tabeli
        self.table.setMaximumSize(max_width, max_height)

        # Dopasowanie rozmiaru tabeli do zawartości (ale nie większego niż maksymalne)
        self.table.setFixedSize(
            min(table_width, max_width),
            min(table_height, max_height)
        )

        # Dopasowanie rozmiaru okna, zostawiając miejsce na marginesy
        self.setMinimumSize(600, 400)  # Minimalny rozmiar, gdy tabela jest pusta lub mało danych
        self.resize(
            min(table_width + 50, max_width),
            min(table_height + 50, max_height)
        )





if __name__ == "__main__":
    app: QApplication = QApplication([])
    viewer: DatabaseViewer = DatabaseViewer()
    viewer.show()
    sys.exit(app.exec_())