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


Created: 2025.01.13
Modified: 2025.01.14
"""
# Imports
from email.charset import QP
import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QAction, QWidget, QGridLayout)
from PyQt5.Qt import QLabel, QPushButton
from PyQt5.QtGui import QIcon           
from PyQt5.QtCore import Qt    

class GUI(QMainWindow):                     
    def __init__(self) -> None:
        super().__init__()                  
        self.initUI()                      

    def initUI(self) -> None:
        self.setWindowTitle("PyQt5 GUI")      
        self.resize(1100, 600)               
        self.add_menus_and_status() 
        self.layout_using_grid()  
        
    def layout_using_grid(self):
        label_1: QLabel = QLabel("First layout", self)
        label_2: QLabel = QLabel("Second layout", self)
        label_span: QLabel = QLabel("Label spanning columns span span span")

        button_1: QPushButton = QPushButton("Click 1")
        button_2: QPushButton = QPushButton("Click 2")

        grid_layout: QGridLayout = QGridLayout()
        grid_layout.addWidget(label_1, 0, 0)
        grid_layout.addWidget(button_1, 0, 1)
        grid_layout.addWidget(label_2, 1, 0)
        grid_layout.addWidget(button_2, 1, 1)
        grid_layout.addWidget(label_span, 2,0,1,3) #row=2, col=0, rowspan=1, colspan=3

        grid_layout.setAlignment(Qt.AlignTop | Qt.AlignLeft) # align grid to the bottom
        grid_layout.setAlignment(label_1, Qt.AlignRight)
        grid_layout.setAlignment(label_2, Qt.AlignRight)


        layout_widget: QWidget = QWidget()
        layout_widget.setLayout(grid_layout)

        self.setCentralWidget(layout_widget)
    
        

    


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
    
