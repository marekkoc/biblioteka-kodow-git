# -*- coding: utf-8 -*-
"""
Spyder Editor

Code with Josh
QT tutorial
3 Qt calculator

1. Moje pierwsze modyfikacje

C: 2024.10.15
M: 2024.10.18

1h48m17s
"""


from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QGridLayout, QLineEdit, QHBoxLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class CalcApp(QWidget):

    def __init__(self):
        super().__init__()
        self.resize(850, 600)
        self.setWindowTitle("My Class Calculator v 1.0")

        self.text_box = QLineEdit()
        self.text_box.setFont(QFont("Helvetica", 32))
        self.text_box.setAlignment(Qt.AlignRight)
        self.grid_layout = QGridLayout()

        self.button_name_list = ["0", "1", "2", "/",
                                "3", "4", "5", "*",
                                "6", "7","8", "-",
                                "9", ".", "rnd.", "+"]
        row = 0
        col = 0

        for button_text in self.button_name_list:
            button = QPushButton(button_text)
            button.clicked.connect(self.button_click)
            button.setStyleSheet("QPushButton {font: 25pt Comic Sans MS; padding: 10 px;}")
            self.grid_layout.addWidget(button, row, col)
            col += 1
            if col>3:
                col = 0
                row += 1


        master_layout = QVBoxLayout()
        master_layout.addWidget(self.text_box)
        master_layout.addLayout(self.grid_layout)

        self.clear_button = QPushButton("Clear")
        self.delete_button = QPushButton("Delete")
        row_layout = QHBoxLayout()
        row_layout.addWidget(self.clear_button)
        row_layout.addWidget(self.delete_button)
        master_layout.addLayout(row_layout)

        self.equal_button = QPushButton("=")
        master_layout.addWidget((self.equal_button))
        self.equal_button.setStyleSheet("""
                    QPushButton {
                        background-color: #3498db;  /* Kolor tła */
                        color: white;               /* Kolor tekstu */
                        border-radius: 10px;        /* Zaokrąglone rogi */
                        padding: 10px;              /* Wewnętrzny margines */
                        font: 25pt Comic Sans MS    /*czcionka */
                        }
                    QPushButton:hover {
                        background-color: #2980b9;  /* Kolor tła po najechaniu */
                        }
                    """)

        master_layout.setContentsMargins(25,25,25,25)
        self.setLayout(master_layout)

        single_buttons = [self.clear_button, self.delete_button, self.equal_button]
        for b in single_buttons:
            b.clicked.connect(self.button_click)
        for b in single_buttons[:-1]:
            b.setStyleSheet("QPushButton {font: 25pt Comic Sans MS; padding: 10 px}")



    def button_click(self):
        button = app.sender()
        text = button.text()

        if text == "=":
            symbol = self.text_box.text()
            try:
                result = eval(symbol)
                self.text_box.setText(str(result))
            except Exception as e:
                self.text_box.setText("ERROR!")
        elif text =="Clear":
            self.text_box.clear()
        elif text == "Delete":
            self.text_box.setText(self.text_box.text()[:-1])
        elif text == "rnd.":
            val = str(round(float(self.text_box.text()),2))
            self.text_box.setText(val)
        else:
            self.text_box.setText(self.text_box.text() + text)





if __name__ in "__main__":
    app = QApplication([])
    main_window = CalcApp()
    main_window.setStyleSheet("QWidget {background-color: #f0f0f8}")
    main_window.show()
    app.exec_()
