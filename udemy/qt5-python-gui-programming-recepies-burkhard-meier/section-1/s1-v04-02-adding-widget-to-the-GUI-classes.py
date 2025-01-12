"""
Udemy.com
Kurs: Python GUI programming Recipies using PyQt5
url: https://www.udemy.com/course/python-gui-programming-recipes-using-pyqt5/?couponCode=KEEPLEARNING

Sekcja 1: Introduction to PyQt5 Framework
4: Adding widgets to the GUI
    url: https://www.udemy.com/course/python-gui-programming-recipes-using-pyqt5/learn/lecture/8486478#overview


We will:  
    1. refactore our code to use Python classes,
    2. inherit from a PyQt5 QMainWindow class. Classess better organizes our code,
(!)  3. add a fully functioned status bar, 
(!) 4. add a menu bar with menu items, 
(!) 5. connect an action to a menu item to close the GUI window. 


Created: 2025.01.11
Modified: 2025.01.11
"""
# Imports
import sys
from PyQt5.QtWidgets import QApplication, QWidget

class GUI():
    def __init__(self) -> None:

        self.initUI()

    
    def initUI(self) -> None:
        self.win: QWidget = QWidget() # create a Window
        self.win.setWindowTitle("PyQt5 GUI") # add widgets and change properties


if __name__ == "__main__":
    app: QApplication = QApplication(sys.argv)  # create Application
    gui: GUI = GUI()                            # create instance of class
    gui.win.show()                              # show the constructed PyQt windowa
    sys.exit(app.exec_())                       # execute the application

    