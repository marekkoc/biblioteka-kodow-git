# -*- coding: utf-8 -*-
"""
Spyder Editor

Code with Josh
QT tutorial
3 Qt calculator

Zamiana kodu ze skryptu na klase

C: 2024.10.15
M: 2024.10.17

1h48m17s
"""


from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QGridLayout, QLineEdit, QHBoxLayout
from PyQt5.QtGui import QFont


class CalcApp(QWidget):

    def __init__(self):
        super().__init__()
        self.resize(850, 600)
        self.setWindowTitle("My Class Calculator v 1.0")

        self.text_box = QLineEdit()
        self.text_box.setFont(QFont("Helvetica", 32))
        self.grid_layout = QGridLayout()

        self.button_name_list = ["7", "8", "9", "/",
                                "4", "5", "6", "*",
                                "1", "2","3", "-",
                                "0", ".", "=", "+"]
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
        master_layout.setContentsMargins(25,25,25,25)
        self.setLayout(master_layout)

        self.clear_button.clicked.connect(self.button_click)
        self.clear_button.setStyleSheet("QPushButton {font: 25pt Comic Sans MS; padding: 10 px;}")
        self.delete_button.clicked.connect(self.button_click)
        self.delete_button.setStyleSheet("QPushButton {font: 25pt Comic Sans MS; padding: 10 px;}")



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
        else:
            self.text_box.setText(self.text_box.text() + text)





if __name__ in "__main__":
    app = QApplication([])
    main_window = CalcApp()
    main_window.setStyleSheet("QWidget {background-color: #f0f0f8}")
    main_window.show()
    app.exec_()
