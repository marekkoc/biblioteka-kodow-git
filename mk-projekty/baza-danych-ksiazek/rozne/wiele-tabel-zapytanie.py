"""

Kod na podstawie notatki: baza-danych-ksiazwk-wyswietlanie-jednej-tabeli.md
Kod wygenerowany przez ChatGPT.

Do kodu chce dodać pole edycyjne w którym będzie można zapisać pytanie typu SELECT * FROM tabela WHERE 


Created: 2025.01.10
Modified: 2025.01.10
"""


import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                             QPushButton, QTableWidget, QTableWidgetItem,
                             QFileDialog, QMessageBox, QComboBox, QTextEdit)
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

        # Rozwijana lista tabel
        self.table_selector: QComboBox = QComboBox()
        self.table_selector.currentIndexChanged.connect(self.change_table)
        self.table_selector.hide()
        self.layout.addWidget(self.table_selector)
        
        # Edytor pytań        
        self.query_box: QTextEdit = QTextEdit()
        self.query_button: QPushButton = QPushButton("Query")
        
        self.edit_row: QHBoxLayout = QHBoxLayout()
        self.edit_row.addWidget(self.query_box)
        self.edit_row.addWidget(self.query_button)
        self.layout.addLayout(self.edit_row)


        # Tabela wyswietlajaca dane
        self.table:QTableWidget = QTableWidget()
        self.layout.addWidget(self.table)


    def open_database(self):
        """
        Otwiera plik bazy danych SQLite i wyświetal jego zawartość
        """
        file_path: str
        filters: str
        def_folder: str = "/home/marek/biblioteka-repozytoriow-git/biblioteka-kodow-git/mk-projekty/baza-danych-ksiazek"
        file_path, filters = QFileDialog.getOpenFileName(self, "Select Database File", def_folder, "SQLite Files (*.db *.sqlite *.sqlite3);;All Files (*)")

        if not file_path:
            return # Anulowano wybór pliku
        
        # Połączenie z bazą danych
        database: QSqlDatabase = QSqlDatabase().addDatabase("QSQLITE")
        database.setDatabaseName(file_path)

        if not database.open():
            QMessageBox.critcal(self, "Error", f"Failed to open database: {database.lastError().text()}")
            return
        
        # Pobieranie tabel z bazy danych
        query: QSqlQuery = QSqlQuery("SELECT name FROM sqlite_master WHERE type='table'")

        if not query.exec_():
            QMessageBox.critical(self, "Error", f"Failed to fetch tables: {query.lastError().text()}")
            return
        
        tables: list[str] = []
        while query.next():
            tables.append(query.value(0))

        if not tables:
            QMessageBox.information(self, "No Tables", "The selected database contains no tables.")
            return
        
        # Wypełnienie listy rozwijanej nazwami tabel
        self.table_selector.clear()
        self.table_selector.addItems(tables)
        self.table_selector.show()

        # Załadowanie pierwszej tabeli - wartość domyślna
        self.load_table_data(tables[0])


    def change_table(self):
        """Zmienia tabelę wyświetlaną w widoku tabeli"""
        table_name:str = self.table_selector.currentText()
        if table_name:
            self.load_table_data(table_name)

       


    def load_table_data(self, table_name):
        "Ładuje dane z wybranej tabeli do widoku tabeli."

        query: QSqlQuery = QSqlQuery(f"SELECT * FROM {table_name}")
        
        if not query.exec_():
            QMessageBox.critical(self, "Error", f"Failed to fetch data: {query.lastError().text()}")
            return

        # Pobieranie nagłówków kolumn
        column_count: int = query.record().count()
        headers: list[str] = [query.record().fieldName(i) for i in range(column_count)]

        # Czyszczenie tabeli i ustawianie nazw kolumn
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



if  __name__ == '__main__':
    app:QApplication = QApplication([])
    viewer: DatabaseViewer = DatabaseViewer()
    viewer.show()
    sys.exit(app.exec_())

