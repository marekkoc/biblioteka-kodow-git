#! /home/marek/miniconda3/envs/py38/bin/python
# -*- coding: utf-8 -*-
"""
Spyder Editor

Code with Josh
QT tutorial
1. Qt widger

C: 2024.10.14
M: 2024.10.14
"""

# 1. Import modules
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout

# 2. Main App objects and settings

# App settings
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("Random word maker")
main_window.resize(800, 600)


# 2. Create all app objects

# 3. All design here

# 4. Events


# 5. Show/run our app
# Create all objects inside
main_window.show()
app.exec_()
