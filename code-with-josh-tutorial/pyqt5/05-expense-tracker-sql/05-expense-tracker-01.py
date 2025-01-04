"""
Expense tracker

based on code with Josh
course: Python App Development: Build Modern GUIs in 7 Hours (Beginners Course)
link: https://www.youtube.com/watch?v=f_9NBdSAo-g&t=644s

start (GUI): 3h42min 
SQL: 4h01min
Add & Delete Expenses: 4h11min
    Implementacja kodu: 4h20min
Add Expenses: 4h37min
end:

Created: 2025.01.04
Modified: 2025.01.05
"""
import sys
from email.charset import QP
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QComboBox, QDateEdit, QTableWidget, QVBoxLayout, QHBoxLayout, QMessageBox, QTableWidgetItem
from PyQt5.QtSql import QSqlDatabase, QSqlQuery


# Application Class
class ExpenseApp(QWidget):
    def __init__(self):
        super().__init__()
        # Main App Objects and Settings
        self.resize(1150, 500)
        self.setWindowTitle("Expense Tracker 2.0")

        # Create Objects
        self.date_box = QDateEdit()
        self.dropdown = QComboBox()
        self.amount = QLineEdit()
        self.description = QLineEdit()

        self.add_button = QPushButton("Add Expense")
        self.delete_button = QPushButton("Delete Expense")

        self.table = QTableWidget()
        self.table.setColumnCount(5) # Id, date, category, amount, descriptoin
        self.table.setHorizontalHeaderLabels(["Id", "Date", "Category", "Amount", "Description"])
        
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
            self.table.setItem(row, 0, QTableWidgetIetm(str(expense_id)))
            self.table.setItem(row, 1, QTableWidgetIetm(date))
            self.table.setItem(row, 2, QTableWidgetIetm(category))
            self.table.setItem(row, 3, QTableWidgetIetm(str(amount)))
            self.table.setItem(row, 4, QTableWidgetIetm(description))
           
            row += 1



# Create Database
database = QSqlDatabase("QSQLITE")
database.setDatabaseName("expense.db")
if not database.open():
    QMessageBox.critical(None, "Error", "Could not open your database")
    sys.exit(1)

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