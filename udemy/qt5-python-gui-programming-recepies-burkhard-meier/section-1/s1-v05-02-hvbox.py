"""
Udemy.com
Kurs: Python GUI programming Recipies using PyQt5
url: https://www.udemy.com/course/python-gui-programming-recipes-using-pyqt5/?couponCode=KEEPLEARNING

Sekcja 1: Introduction to PyQt5 Framework
4: Layout of Widgets
    url: https://www.udemy.com/course/python-gui-programming-recipes-using-pyqt5/learn/lecture/8486484#overview


We will:  
    1. add many widgets to GUI,
    2. lay out the widgets,
    3. learn several lauout techniques,
    4. learn about: 
        - positional layout,
        - box layout (horizontal and vertical boxes),
        - grid layout.

Zmiany:
    1. new method: positional_widget_layout()
    2. get size of a widget

Created: 2025.01.12
Modified: 2025.01.12
"""
# Imports
from email.charset import QP
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QPushButton, QLabel
from PyQt5.QtGui import QIcon               

class GUI(QMainWindow):                     
    def __init__(self) -> None:
        super().__init__()                  
        self.initUI()                      
    
    def initUI(self) -> None:
        self.setWindowTitle("PyQt5 GUI")      
        self.resize(1100, 600)               
        self.add_menus_and_status()   
        self.positional_widget_layout()

    def positional_widget_layout(self):
        label_1: QLabel = QLabel("Our first label, bla bla bla", self)
        label_1.adjustSize()
        print(label_1.size())
        print(self.size())

        print()
        print(self.menuBar().size())    # Default size: PyQt5.QtCore.Qsize(100,30)    
        mbar_height: int = self.menuBar().height()
        print(mbar_height)
        label_1.move(10, mbar_height)   # position label below mbar

        label_2: QLabel = QLabel("Another label", self)
        label_2.adjustSize()
        label_2.move(10, mbar_height*2) # align and position belo label_1

        button_1: QPushButton = QPushButton("Click 1", self)
        button_2: QPushButton = QPushButton("Click 2", self)

        print(f"Label_1 width:{label_1.width()}, height: {label_1.height()}")
        button_1.move(label_1.width()+2*10, label_1.height())
        button_2.move(label_1.width()+2*10, label_1.height() *2)


    def add_menus_and_status(self):
        self.statusBar().showMessage("Text in statusbar!")  
        
        # New action               
        new_icon: QIcon = QIcon('icons/new_icon.png')           
        new_action: QAction = QAction(new_icon, "New", self)           
        new_action.setStatusTip("New File")                     
        
        # Exit action
        exit_icon: QIcon = QIcon("icons/exit_icon.png")
        exit_action: QAction = QAction(exit_icon, "Exit", self)
        exit_action.setStatusTip("Click to exit the application")
        exit_action.triggered.connect(self.close)   
        exit_action.setShortcut("Ctrl+Q")           
        
        # The main Menu bar
        menubar  = self.menuBar()              

        # File menu
        file_menu = menubar.addMenu("File")     
        file_menu.addAction(new_action)                  
        file_menu.addSeparator()                     
        file_menu.addAction(exit_action)             
     
        # --------------------------------------
        # Edit menu
        edit_menu = menubar.addMenu("Edit")           

        


if __name__ == "__main__":
    app: QApplication = QApplication(sys.argv)  
    gui: GUI = GUI()                            
    gui.show()                                  
    sys.exit(app.exec_())                        
    