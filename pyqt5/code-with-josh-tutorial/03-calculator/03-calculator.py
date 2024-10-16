# -*- coding: utf-8 -*-
"""
Spyder Editor

Code with Josh
QT tutorial
3 Qt calculator

C: 2024.10.15
M: 2024.10.15
"""

# 1. Import all libraries
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QGridLayout, QLineEdit, QHBoxLayout

# 2. Create and set properies to the App and main window
app = QApplication([])
main_window = QWidget()
main_window.resize(850,600)
main_window.setWindowTitle("Calculator")


# 3. Creage all objescts and widgets
text_box = QLineEdit()

grid_layout = QGridLayout()

button_name_list = ["7", "8", "9", "/",
                "4", "5", "6", "*",
                "1", "2","3", "-",
                "0", ".", "=", "+"]

clear_button = QPushButton("Clear")
delete_button = QPushButton("Delete")

row: int = 0
col: int = 0

grid_layout = QGridLayout()

def button_click():
    button = app.sender()
    text = button.text()


    if text == "=":
        symbol = text_box.text()
        try:
            result = eval(symbol)
            text_box.setText(str(result))
        except Exception as e:
            text_box.setText("ERROR!")

    elif text =="Clear":
        text_box.clear()

    elif text == "Delete":
        text_box.setText(text_box.text()[:-1])
    else:
        text_box.setText(text_box.text() + text)


clear_button.clicked.connect(button_click)
delete_button.clicked.connect(button_click)


for button_text in button_name_list:
    # tworzymy button, nie zachowujemy jego obieku, za kazdym razem nadpisujemy
    # taka sama obiektu wszystkie kolejne obiekty
    button = QPushButton(button_text)

    #łaczymy każdy przycisk z wykonywana funkcja
    button.clicked.connect(button_click)

    # dodajemy ten przycisk do siatki layoutu
    grid_layout.addWidget(button, row, col)
    col += 1

    if col>3:
        col = 0
        row += 1



# 4. Design - Set layout
master_layout = QVBoxLayout()
master_layout.addWidget(text_box)

master_layout.addLayout(grid_layout)

row_layout = QHBoxLayout()
row_layout.addWidget(delete_button)
row_layout.addWidget(clear_button)
master_layout.addLayout(row_layout)

main_window.setLayout(master_layout)


# 5. Connect events, signal and slots

# 6. Show and run the application
main_window.show()
app.exec_()
