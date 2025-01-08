"""

Kod na podstawie notatki: baza-danych-ksiazwk-wyswietlanie-jednej-tabeli.md
Kod wygenerowany przez ChatGPT.


Created: 2025.01.07
Modified: 2025.01.07
"""

import sys
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









if __name__ == "__main__":
    app = QApplication([])
    viewer = DatabaseViewer()
    viewer.show()
    sys.exit(app.exec_())