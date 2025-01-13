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
    1. hvboxes


Created: 2025.01.12
Modified: 2025.01.12
"""
# Imports
from email.charset import QP
import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QAction, QPushButton, QLabel,
    QHBoxLayout, QVBoxLayout, QWidget)
from PyQt5.QtGui import QIcon               

class GUI(QMainWindow):                     
    def __init__(self) -> None:
        super().__init__()                  
        self.initUI()                      

    def initUI(self) -> None:
        self.setWindowTitle("PyQt5 GUI")      
        self.resize(1100, 600)               
        self.add_menus_and_status() 
        self.horizontal_vertical_box_layout()  
        
    
    def horizontal_vertical_box_layout(self):
        label_1: QLabel = QLabel("First label", self)
        label_2: QLabel = QLabel("Second label", self)
        label_3: QLabel = QLabel("Thirst label", self)
        label_4: QLabel = QLabel("Fourth label", self)
        label_5: QLabel = QLabel("Fifth label", self)
        
        

        button_1: QPushButton = QPushButton("Click 1")
        button_2: QPushButton = QPushButton("Click 2")
        button_3: QPushButton = QPushButton("Click 3")
        button_4: QPushButton = QPushButton("Click 4")
        button_5: QPushButton = QPushButton("Click 5")

        hbox_1: QHBoxLayout = QHBoxLayout()
        hbox_1.addStretch()   # push/stretch the components to the right
        hbox_1.addWidget(label_1)
        hbox_1.addWidget(button_1)
                
        hbox_2: QHBoxLayout = QHBoxLayout()        
        hbox_2.addWidget(label_2)        
        hbox_2.addWidget(button_2)
        hbox_2.addStretch() # push/stretch the components to the left
        

        hbox_3: QHBoxLayout = QHBoxLayout()        
        hbox_3.addWidget(label_3)    
        hbox_3.addStretch()   # push/stretch the components to the right    
        hbox_3.addWidget(button_3)
        
                
        hbox_4: QHBoxLayout = QHBoxLayout()
        hbox_4.addStretch() # push/stretch the components to the left
        hbox_4.addWidget(label_4)
        hbox_4.addWidget(button_4)

        hbox_5: QHBoxLayout = QHBoxLayout()
        hbox_5.addStretch()   # push/stretch the components to the right
        hbox_5.addWidget(label_5)
        hbox_5.addWidget(button_5)
                
    

        vbox: QVBoxLayout = QVBoxLayout()        
        vbox.addLayout(hbox_1)
        vbox.addLayout(hbox_2)
        vbox.addLayout(hbox_3)
        vbox.addStretch()   # push/stretch the widgets down
        vbox.addLayout(hbox_4)
        vbox.addLayout(hbox_5)
       

        layout_widget: QWidget = QWidget()  # QWidget object
        layout_widget.setLayout(vbox)       # set layout to the widget

        self.setCentralWidget(layout_widget) # make QWidget the central widget

        

    


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
    