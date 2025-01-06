"""
expenses tracker

based on code with Josh
course: Python App Development: Build Modern GUIs in 7 Hours (Beginners Course)
link: https://www.youtube.com/watch?v=f_9NBdSAo-g&t=644s

start (GUI): 3h42min 
    SQL: 4h01min
    Add & Delete Expenses: 4h11min
        Implementacja kodu: 4h20min
    Add Expenses: 4h37min
    Delete Expenses: 4h50min
        Implementacja kodu: 4h54min
    CSS Styling: 5h03min
        Implementacja kodu: 5h08min
end: 5h16min

Created: 2025.01.04
Modified: 2025.01.05
"""
import sys
import os
from email.charset import QP
from pathlib import Path
from icecream import ic

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QComboBox, QDateEdit,\
     QTableWidget, QVBoxLayout, QHBoxLayout, QMessageBox, QTableWidgetItem, QHeaderView
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtCore import QDate, Qt

os.environ["QT_QUICK_BACKEND"] = "software"
os.environ["QT_OPENGL"] = "software"


DEBUG = 0


# Application Class
class ExpenseApp(QWidget):
    def __init__(self):
        super().__init__()
        
        # Main App Objects and Settings
        self.resize(1100, 700)
        self.setWindowTitle("expenses Tracker 2.0")

        # Create Objects
        self.date_box = QDateEdit()
        self.date_box.setDate(QDate.currentDate())
        self.dropdown = QComboBox()
        self.amount = QLineEdit()
        self.description = QLineEdit()

        self.add_button = QPushButton("Add expenses")
        self.delete_button = QPushButton("Delete expenses")
        self.add_button.clicked.connect(self.add_expense)
        self.delete_button.clicked.connect(self.delete_expense)

        self.table = QTableWidget()
        self.table.setColumnCount(5) # Id, date, category, amount, descriptoin
        self.table.setAlternatingRowColors(True)
        self.table.setHorizontalHeaderLabels(["Id", "Date", "Category", "Amount", "Description"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.sortByColumn(1,Qt.DescendingOrder)
        self.dropdown.addItems(["Food", "Transportation", "Rent", "Shopping", "Entertainment", "Bills", "Other"])
        
        self.setStyleSheet("""
                            QWidget{background-color: #b8c9e1;}

                            QLabel{
                                    color: #333;
                                    font_size: 14px;
                                    }

                            QLineEdit, QComboBox, QDateEdit{
                                        background-color: #b8c9e1;
                                        color: #333;
                                        border: 1px solid #444;
                                        padding: 5px;
                                        }

                            QTableWidget{
                                        background-color: #b8c9e1;
                                        color: #333;
                                        border: 1px solid #444;
                                        selection-background-color: #ddd;
                                        }

                            QPushButton{
                                        background-color: #4caf50;
                                        color: #fff;
                                        border: none;
                                        padding: 8px 16px;
                                        font-size: 20 px;
                                        }       
                            QPushButton:hover{background-color: #45a049;}
                            """)




        # Design App with Layouts
        self.master_layout = QVBoxLayout()
        self.row1 = QHBoxLayout()
        self.row2 = QHBoxLayout()
        self.row3 = QHBoxLayout()

        self.row1.addWidget(QLabel("Date:"))
        self.row1.addWidget(self.date_box)
        self.row1.addWidget(QLabel("Category:"))
        self.row1.addWidget(self.dropdown)

        self.row2.addWidget(QLabel("Amount:"))
        self.row2.addWidget(self.amount)
        self.row2.addWidget(QLabel("Description:"))
        self.row2.addWidget(self.description)

        self.row3.addWidget(self.add_button)
        self.row3.addWidget(self.delete_button)

        self.master_layout.addLayout(self.row1)
        self.master_layout.addLayout(self.row2)
        self.master_layout.addLayout(self.row3)

        self.master_layout.addWidget(self.table)

        self.setLayout(self.master_layout)

        self.load_table()


    def load_table(self):
        self.table.setRowCount(0)

        query = QSqlQuery("SELECT * FROM expenses")
        
        row = 0
        while query.next():
            expense_id = query.value(0)
            date = query.value(1)
            category = query.value(2)
            amount = query.value(3)
            description = query.value(4)

            # Add valuest to table
            self.table.insertRow(row)
            self.table.setItem(row, 0, QTableWidgetItem(str(expense_id)))
            self.table.setItem(row, 1, QTableWidgetItem(date))
            self.table.setItem(row, 2, QTableWidgetItem(category))
            self.table.setItem(row, 3, QTableWidgetItem(str(amount)))
            self.table.setItem(row, 4, QTableWidgetItem(description))           
            row += 1
    
    def add_expense(self):
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
            print(f"Error adding expenses: {query.lastError().text()}")
        else:
            print("expenses added successfully!")

        # Czyszczenie pól
        self.date_box.setDate(QDate.currentDate())
        self.dropdown.setCurrentIndex(0)
        self.amount.clear()
        self.description.clear()

        # Załaduj dane do tabeli
        self.load_table()

    def delete_expense(self):
        selected_row = self.table.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "No Expense Chosen", "Please choose an expense to delete!")
            return
        
        expense_id = int(self.table.item(selected_row, 0).text())

        confirm = QMessageBox.question(self,"Are you sure?", "Delete Expense?", QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.No:
            return
        
        query = QSqlQuery()
        query.prepare("DELETE FROM expenses WHERE id=?")
        query.addBindValue(expense_id)
        query.exec_()

        self.load_table()
        







# Create Database
current_path = Path(__file__).parent  # Pobranie aktualnej ścieżki katalogu
db_path = current_path / "expenses.db"  # Połączenie ścieżki z nazwą pliku bazy danych
if DEBUG: print(f"Database path: {db_path}")

database = QSqlDatabase.addDatabase("QSQLITE")
database.setDatabaseName(str(db_path))  # Przekazanie ścieżki jako string

if DEBUG:
    if os.access(db_path, os.W_OK):
        print(f"Database file '{db_path}' is writable.")
    else:
        print(f"Database file '{db_path}' is NOT writable. Check permissions.")


if not database.open():
    if DEBUG: print(f"Database error: {database.lastError().text()}")
    QMessageBox.critical(None, "Error", f"Could not open your database: {database.lastError().text()}")
    sys.exit(1)
else:
    if DEBUG: print(f"Utworzono bazę danych w lokalizacji: {db_path}")

# Tworzenie tabeli
query = QSqlQuery()
query.exec_("""
    CREATE TABLE IF NOT EXISTS expenses(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    category TEXT,
    amount REAL,
    description TEXT            
    )
""")


# Run the App
if __name__ == "__main__":
    app = QApplication([])
    main = ExpenseApp()
    main.show()
    app.exec_()