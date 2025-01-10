"""

Kod na podstawie notatki: baza-danych-ksiazwk-wyswietlanie-jednej-tabeli.md
Kod wygenerowany przez ChatGPT.


Created: 2025.01.09
Modified: 2025.01.09
"""


import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, 
                             QPushButton, QTableWidget, QTableWidgetItem,
                             QFileDialog, QMessageBox, QComboBox)
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

        # Tabela wyswietlajaca dane
        self.table:QTableWidget = QTableWidget()
        self.layout.addWidget(self.table)


    def open_database(self):
        pass

    def change_table(self):
        pass


if  __name__ == '__main__':
    app:QApplication = QApplication([])
    viewer: DatabaseViewer = DatabaseViewer()
    viewer.show()
    sys.exit(app.exec_())