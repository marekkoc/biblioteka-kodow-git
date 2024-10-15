# -*- coding: utf-8 -*-
"""
Spyder Editor

Code with Josh
QT tutorial
1. Qt widger

C: 2024.10.14
M: 2024.10.14
"""

### 1. Import modules
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout

### 2. Create Main App object(s) and settings

# App settings
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("Random word maker")
main_window.resize(800, 600)


### 3. Create all app widgets and objects

title_text = QLabel(("Random keywords"))

text1 = QLabel("1?")
text2 = QLabel("2?")
text3 = QLabel("3?")

button1 = QPushButton("Click me")
button2 = QPushButton("Click me")
button3 = QPushButton("Click me")

### 4. Designing a Layout is here
master_layout = QVBoxLayout()
row1 = QHBoxLayout()
row2 = QHBoxLayout()
row3 = QHBoxLayout()

row1.addWidget(title_text, alignment=Qt.AlignCenter)

row2.addWidget(text1, alignment=Qt.AlignCenter)
row2.addWidget(text2, alignment=Qt.AlignCenter)
row2.addWidget(text3, alignment=Qt.AlignCenter)

row3.addWidget(button1, alignment=Qt.AlignCenter)
row3.addWidget(button2, alignment=Qt.AlignCenter)
row3.addWidget(button3, alignment=Qt.AlignCenter)

master_layout.addLayout(row1)
master_layout.addLayout(row2)
master_layout.addLayout(row3)

main_window.setLayout(master_layout)


### 4. Events
from random import choice
from typing import List
my_words: List[str] = ["Hello", "Goodbye", "Test", "Python", "Qt", "Codde", "Pandas", "Dupa"]


def display_word(button: QPushButton) -> None:
    button = app.sender()
    word: str = choice(my_words)

    if button == button1:
        text1.setText(word)
    if button == button2:
        text2.setText(word)
    if button == button3:
        text3.setText(word)

button1.clicked.connect(display_word)
button2.clicked.connect(display_word)
button3.clicked.connect(display_word)

### 5. Show& execute our app
main_window.show()
app.exec_()
