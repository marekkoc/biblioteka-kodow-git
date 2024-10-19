#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 11:12:11 2024

@author: marek

Image editor

1h58min

C: 2024.10.18
M: 2024.10.18
"""

# 1. Main imports
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QComboBox, QListWidget, QVBoxLayout, QHBoxLayout

# 2.Main application and settings
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("My Image editor")
main_window.resize(800,700)

# 3. all widgets and app elemtnes
col_left_layout = QVBoxLayout()
col_right_layou = QHBoxLayout()
main_window_layout = QHBoxLayout()

select_button = QPushButton("Select folder")
image_list = QListWidget()
operation_list = QComboBox()

col_left_layout.addWidget(select_button)
col_left_layout.addWidget(image_list)
col_left_layout.addWidget(operation_list)

image = QLabel("obrazek")
col_right_layou.addWidget(image)





# 4. Design
main_window_layout.addLayout(col_left_layout)
main_window_layout.addLayout(col_right_layou)
main_window.setLayout(main_window_layout)

# 5. Events

# 6. show and run our app
main_window.show()
app.exec_()
