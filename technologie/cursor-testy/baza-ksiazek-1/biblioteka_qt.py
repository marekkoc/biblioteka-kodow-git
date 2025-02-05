from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                            QPushButton, QTableWidget, QTableWidgetItem, 
                            QDialog, QFormLayout, QLineEdit, QMessageBox)
import sys
import sqlite3

class DodajKsiazkeDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Dodaj nową książkę")
        self.setModal(True)
        
        # Tworzenie formularza
        layout = QFormLayout()
        
        self.tytul_input = QLineEdit()
        self.autor_input = QLineEdit()
        
        layout.addRow("Tytuł:", self.tytul_input)
        layout.addRow("Autor:", self.autor_input)
        
        # Przycisk zapisz
        zapisz_btn = QPushButton("Zapisz")
        zapisz_btn.clicked.connect(self.accept)
        layout.addRow(zapisz_btn)
        
        self.setLayout(layout)

class BibliotekaBaza(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("System Biblioteczny")
        self.setGeometry(100, 100, 800, 600)
        
        # Połączenie z bazą danych
        try:
            self.conn = sqlite3.connect('ksiazki.sqlite')
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Błąd", f"Nie można połączyć z bazą danych: {e}")
        
        # Tworzenie głównego widgetu i layoutu
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # Przyciski
        pokaz_btn = QPushButton("Pokaż wszystkie książki")
        dodaj_btn = QPushButton("Dodaj książkę")
        
        pokaz_btn.clicked.connect(self.pokaz_ksiazki)
        dodaj_btn.clicked.connect(self.dodaj_ksiazke)
        
        layout.addWidget(pokaz_btn)
        layout.addWidget(dodaj_btn)
        
        # Tabela
        self.tabela = QTableWidget()
        self.tabela.setColumnCount(3)
        self.tabela.setHorizontalHeaderLabels(['ID', 'Tytuł', 'Autor'])
        layout.addWidget(self.tabela)
        
    def pokaz_ksiazki(self):
        try:
            self.cursor.execute("SELECT * FROM papierowe")
            dane = self.cursor.fetchall()
            
            self.tabela.setRowCount(len(dane))
            for i, wiersz in enumerate(dane):
                for j, wartosc in enumerate(wiersz):
                    self.tabela.setItem(i, j, QTableWidgetItem(str(wartosc)))
                    
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Błąd", f"Nie można pobrać książek: {e}")
            
    def dodaj_ksiazke(self):
        dialog = DodajKsiazkeDialog(self)
        if dialog.exec_() == QDialog.Accepted:
            tytul = dialog.tytul_input.text()
            autor = dialog.autor_input.text()
            
            try:
                self.cursor.execute("INSERT INTO papierowe (tytul, autor) VALUES (?, ?)", 
                                  (tytul, autor))
                self.conn.commit()
                QMessageBox.information(self, "Sukces", "Książka została dodana!")
                self.pokaz_ksiazki()
            except sqlite3.Error as e:
                QMessageBox.critical(self, "Błąd", f"Nie można dodać książki: {e}")

def main():
    app = QApplication(sys.argv)
    window = BibliotekaBaza()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main() 