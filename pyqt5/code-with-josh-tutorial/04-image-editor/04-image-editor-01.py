#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 11:12:11 2024

@author: marek

Image editor

1h58min

C: 2024.10.18
M: 2024.10.19
"""

# 1. Main imports
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QComboBox, QListWidget, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt

# 2.Main application and settings
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("PhotoQt")
main_window.resize(900,700)

# 3. all widgets and app elemtnes
btn_folder = QPushButton("Folder")
file_list = QListWidget()
btn_left = QPushButton("Left")
btn_right = QPushButton("Right")
btn_mirror = QPushButton("Mirror")
btn_sharpness = QPushButton("Sharpness")
btn_gray = QPushButton("Gray")
btn_saturation = QPushButton("Saturation")
btn_contrast = QPushButton("Contrast")
btn_blur = QPushButton("Blur")

#Dropdown box
filter_box = QComboBox()
filter_box.addItem("Oryginal")
filter_box.addItems(["Left", "Right", "Mirror","Sharpness","Gray", "Saturation", "Contrast", "Blur"])

picture_box = QLabel("Image will appear here")

# 4. Design
master_layout = QHBoxLayout()
col1 = QVBoxLayout()
col2 = QHBoxLayout()

col1.addWidget(btn_folder)
col1.addWidget(file_list)
col1.addWidget(filter_box)
col1.addWidget(btn_left)

col1.addWidget(btn_right)
col1.addWidget(btn_mirror)
col1.addWidget(btn_sharpness)
col1.addWidget(btn_gray)
col1.addWidget(btn_saturation)
col1.addWidget(btn_contrast)
col1.addWidget(btn_blur)

col2.addWidget(picture_box)


master_layout.addLayout(col1, 20)
master_layout.addLayout(col2, 80)

main_window.setLayout(master_layout)

# 5. Events

# 6. show and run our app
main_window.show()
app.exec_()
