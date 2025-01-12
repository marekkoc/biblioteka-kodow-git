"""
Udemy.com
Kurs: Python GUI programming Recipies using PyQt5
url: https://www.udemy.com/course/python-gui-programming-recipes-using-pyqt5/?couponCode=KEEPLEARNING

Sekcja 1: Introduction to PyQt5 Framework
3: Creating our first GUI
    url: https://www.udemy.com/course/python-gui-programming-recipes-using-pyqt5/learn/lecture/8486470#overview




Created: 2025.01.11
Modified: 2025.01.11
"""
# Imports
import sys
from PyQt5.QtWidgets import QApplication, QWidget

# Create an Application (by creating the instance of QApplicaton class)
# We pass sys.argv to pass the arguments of a command line
app: QApplication = QApplication(sys.argv)

# Create a Window
win: QWidget = QWidget()

# Add widgets and change properties
win.setWindowTitle("PyQt5 Gui. The first example!")
win.resize(1040, 480) # set the window size: width, height

# Show the constructed Qt window
# By default the window is hidden
win.show()


# app.exec_( ) # Qt exec_ ends with underscore; it is for a main loop
# app.exec() # it is a Python function

# a good practice is as follows: sys.exit(app.exec_())
# this ensure that any exceptions that can be thrown by the application
#  would be properly handled by Python

# Execute (run) the application
sys.exit(app.exec_())