from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QTableWidget, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menedżer Biblioteki")
        
        # Główny widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # Tabela z książkami
        self.books_table = QTableWidget()
        layout.addWidget(self.books_table)
        
        # Przyciski akcji
        self.add_book_btn = QPushButton("Dodaj książkę")
        self.generate_report_btn = QPushButton("Generuj raport")
        self.custom_query_btn = QPushButton("Własne zapytanie")
        
        layout.addWidget(self.add_book_btn)
        layout.addWidget(self.generate_report_btn)
        layout.addWidget(self.custom_query_btn)

def test_connection():
    db = DatabaseManager()
    if db.connect():
        # Sprawdź tabele w bazie
        cursor = db.execute_query("SELECT name FROM sqlite_master WHERE type='table';")
        if cursor:
            tables = cursor.fetchall()
            print("\nDostępne tabele:")
            for table in tables:
                print(f"- {table[0]}")
        db.disconnect() 