"""

Expenses tracker - kod przerabiany - zmodyfikowany za pomoca ChatGPT.

based on code with Josh
course: Python App Development: Build Modern GUIs in 7 Hours (Beginners Course)
link: https://www.youtube.com/watch?v=f_9NBdSAo-g&t=644s

Kod zrefaktoryzowany przez ChatGPT - opis w pliku: 05-expense-tracker-02.md


Created: 2025.01.06
Modified: 2025.01.06
"""

import sys
import os
from pathlib import Path
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QLineEdit, QComboBox, QDateEdit,
    QTableWidget, QVBoxLayout, QHBoxLayout, QMessageBox, QTableWidgetItem, QHeaderView
)
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtCore import QDate, Qt

# Stałe konfiguracyjne
DEBUG = 0
STYLESHEET = """
    QWidget { background-color: #b8c9e1; }

    QLabel {
        color: #333;
        font-size: 28px;
    }

    QLineEdit, QComboBox, QDateEdit {
        background-color: #b8c9e1;
        color: #333;
        border: 1px solid #444;
        padding: 5px;
    }

    QTableWidget {
        background-color: #b8c9e1;
        color: #333;
        border: 1px solid #444;
        selection-background-color: #ddd;
        font-size: 28px;
    }

    QPushButton {
        background-color: #4caf50;
        color: #fff;
        border: none;
        padding: 8px 22px;
        font-size: 28px;
    }
    QPushButton:hover { background-color: #45a049; }
"""
TABLE_HEADERS = ["Id", "Date", "Category", "Amount", "Description"]
CATEGORIES = ["Food", "Transportation", "Rent", "Shopping", "Entertainment", "Bills", "Other"]

# Klasa aplikacji
class ExpenseApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.setup_database()
        self.load_table()

    def setup_ui(self):
        """Konfiguracja interfejsu użytkownika."""
        self.setWindowTitle("Expenses Tracker 2.0")
        self.resize(1100, 700)
        self.setStyleSheet(STYLESHEET)

        # Tworzenie widżetów
        self.date_box: QDateEdit = QDateEdit(QDate.currentDate())
        self.dropdown: QComboBox = QComboBox()
        self.dropdown.addItems(CATEGORIES)
        self.amount: QLineEdit = QLineEdit()
        self.description: QLineEdit = QLineEdit()

        self.add_button: QPushButton = QPushButton("Add Expense")
        self.delete_button: QPushButton = QPushButton("Delete Expense")
        self.add_button.clicked.connect(self.add_expense)
        self.delete_button.clicked.connect(self.delete_expense)

        self.table: QTableWidget = QTableWidget()
        self.table.setColumnCount(len(TABLE_HEADERS))
        self.table.setHorizontalHeaderLabels(TABLE_HEADERS)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setAlternatingRowColors(True)
        
        # Layouty
        self.master_layout: QVBoxLayout = QVBoxLayout()

        input_layout1: QHBoxLayout = QHBoxLayout()
        input_layout1.addWidget(QLabel("Date:"))
        input_layout1.addWidget(self.date_box)
        input_layout1.addWidget(QLabel("Category:"))
        input_layout1.addWidget(self.dropdown)

        input_layout2: QHBoxLayout = QHBoxLayout()
        input_layout2.addWidget(QLabel("Amount:"))
        input_layout2.addWidget(self.amount)
        input_layout2.addWidget(QLabel("Description:"))
        input_layout2.addWidget(self.description)

        button_layout: QHBoxLayout = QHBoxLayout()
        button_layout.addWidget(self.add_button)
        button_layout.addWidget(self.delete_button)

        self.master_layout.addLayout(input_layout1)
        self.master_layout.addLayout(input_layout2)
        self.master_layout.addLayout(button_layout)
        self.master_layout.addWidget(self.table)

        self.setLayout(self.master_layout)

    def setup_database(self):
        """Konfiguracja bazy danych."""
        current_path: Path = Path(__file__).parent
        db_path: Path = current_path / "expenses.db"

        database:QSqlDatabase = QSqlDatabase.addDatabase("QSQLITE")
        database.setDatabaseName(str(db_path))

        if not database.open():
            QMessageBox.critical(self, "Error", f"Could not open database: {database.lastError().text()}")
            sys.exit(1)

        query = QSqlQuery()
        query.exec_("""
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT,
                category TEXT,
                amount REAL,
                description TEXT
            )
        """)

    def load_table(self):
        """Załadowanie danych z bazy do tabeli."""
        self.table.setRowCount(0)
        query: QSqlQuery = QSqlQuery("SELECT * FROM expenses ORDER BY date DESC")

        row = 0
        while query.next():
            self.table.insertRow(row)
            for col in range(len(TABLE_HEADERS)):
                self.table.setItem(row, col, QTableWidgetItem(str(query.value(col))))
            row += 1

    def add_expense(self):
        """Dodanie nowego wydatku."""
        date = self.date_box.date().toString("yyyy-MM-dd")
        category = self.dropdown.currentText()
        amount = self.amount.text()
        description = self.description.text()

        query = QSqlQuery()
        query.prepare("""
            INSERT INTO expenses (date, category, amount, description)
            VALUES (?, ?, ?, ?)
        """)
        query.addBindValue(date)
        query.addBindValue(category)
        query.addBindValue(amount)
        query.addBindValue(description)

        if not query.exec_():
            QMessageBox.critical(self, "Error", f"Failed to add expense: {query.lastError().text()}")
        else:
            self.amount.clear()
            self.description.clear()
            self.load_table()

    def delete_expense(self):
        """Usunięcie zaznaczonego wydatku."""
        selected_row = self.table.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Error", "Please select an expense to delete!")
            return

        expense_id = int(self.table.item(selected_row, 0).text())
        confirm = QMessageBox.question(self, "Confirm", "Are you sure you want to delete this expense?", QMessageBox.Yes | QMessageBox.No)

        if confirm == QMessageBox.Yes:
            query = QSqlQuery()
            query.prepare("DELETE FROM expenses WHERE id = ?")
            query.addBindValue(expense_id)
            if not query.exec_():
                QMessageBox.critical(self, "Error", f"Failed to delete expense: {query.lastError().text()}")
            self.load_table()

# Uruchomienie aplikacji
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = ExpenseApp()
    main.show()
    sys.exit(app.exec_())
