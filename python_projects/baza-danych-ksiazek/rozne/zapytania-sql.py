import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QPlainTextEdit, QTableWidget, QTableWidgetItem, QMessageBox
)
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

class SQLQueryEditor(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("SQL Query Editor")
        self.resize(800, 600)

        # Layout główny
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Pole tekstowe do wpisywania zapytań SQL
        self.query_input = QPlainTextEdit()
        self.query_input.setPlaceholderText("Enter your SQL query here...")
        layout.addWidget(self.query_input)

        # Przycisk wykonania zapytania
        button_layout = QHBoxLayout()
        self.execute_button = QPushButton("Execute Query")
        self.execute_button.clicked.connect(self.execute_query)
        button_layout.addWidget(self.execute_button)

        layout.addLayout(button_layout)

        # Tabela do wyświetlania wyników
        self.results_table = QTableWidget()
        layout.addWidget(self.results_table)

        # Połączenie z bazą danych
        self.database = QSqlDatabase.addDatabase("QSQLITE")
        self.database.setDatabaseName("example.db")  # Ścieżka do bazy danych SQLite
        if not self.database.open():
            QMessageBox.critical(self, "Error", f"Failed to open database: {self.database.lastError().text()}")

    def execute_query(self):
        """Wykonuje zapytanie SQL wpisane w pole tekstowe."""
        sql_query = self.query_input.toPlainText().strip()

        if not sql_query:
            QMessageBox.warning(self, "Warning", "Please enter a valid SQL query.")
            return

        query = QSqlQuery(sql_query)
        if not query.exec_():
            QMessageBox.critical(self, "Error", f"Query execution failed:\n{query.lastError().text()}")
            return

        # Wypełnienie tabeli wynikami zapytania
        self.populate_results(query)

    def populate_results(self, query):
        """Wypełnia tabelę wynikami zapytania."""
        self.results_table.clear()

        # Pobieranie nagłówków kolumn
        column_count = query.record().count()
        self.results_table.setColumnCount(column_count)
        self.results_table.setHorizontalHeaderLabels(
            [query.record().fieldName(i) for i in range(column_count)]
        )

        # Wypełnianie wierszy
        rows = []
        while query.next():
            rows.append([query.value(i) for i in range(column_count)])

        self.results_table.setRowCount(len(rows))
        for row_idx, row_data in enumerate(rows):
            for col_idx, cell_data in enumerate(row_data):
                self.results_table.setItem(row_idx, col_idx, QTableWidgetItem(str(cell_data)))

        self.results_table.resizeColumnsToContents()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    editor = SQLQueryEditor()
    editor.show()
    sys.exit(app.exec_())
