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

Zmiany:
    1. add MenyBar
    2. use QAction (!)
    3. icons in menu items. Icon must be created before QAction, as it is passed 
        to the QAction constructor.
    4. add a separator menu line
    5. we connect a function to an event! To order to a menu do something.
    6. add a keyboard shortcut to close the application

Created: 2025.01.11
Modified: 2025.01.12
"""
# Imports
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction
from PyQt5.QtGui import QIcon               # nowy improt

class GUI(QMainWindow):                     # inherit from QMainWindow
    def __init__(self) -> None:
        super().__init__()                  # initialize super class, whitch creates the instance of QWidget
        
        self.initUI()                       # refer to Window as self

    
    def initUI(self) -> None:
        self.setWindowTitle("PyQt5 GUI")                    # add widgets and change properties
        self.resize(1100, 600)               # resize the window (width, heigth)

        self.add_menus_and_status()         # set menus, actions, shortcuts in a separate function



    def add_menus_and_status(self):
        self.statusBar().showMessage("Text in statusbar!")  # status bar
        
        # New action               
        new_icon: QIcon = QIcon('icons/new_icon.png')           # create an icon
        new_action: QAction = QAction(new_icon, "New", self)    # create an Action        
        new_action.setStatusTip("New File")                     # statusBar updatet
        
        # Exit action
        exit_icon: QIcon = QIcon("icons/exit_icon.png")
        exit_action: QAction = QAction(exit_icon, "Exit", self)
        exit_action.setStatusTip("Click to exit the application")
        exit_action.triggered.connect(self.close)   # close application with built-in function
        exit_action.setShortcut("Ctrl+Q")           # keyboard shortcut to close the window
        
        # The main Menu bar
        menubar  = self.menuBar()               # create a menu bar

        # File menu
        file_menu = menubar.addMenu("File")     # add menu to menu bar
        file_menu.addAction(new_action)              # add New Action to menu        
        file_menu.addSeparator()                     # add separator line
        file_menu.addAction(exit_action)             # add Exit Action to menu
     
        # --------------------------------------
        # Edit menu
        edit_menu = menubar.addMenu("Edit")     # edd second menu        

        


if __name__ == "__main__":
    app: QApplication = QApplication(sys.argv)  # create Application
    gui: GUI = GUI()                            # create instance of class
    gui.show()                                  # show the constructed PyQt windowa
    sys.exit(app.exec_())                       # execute the application

    