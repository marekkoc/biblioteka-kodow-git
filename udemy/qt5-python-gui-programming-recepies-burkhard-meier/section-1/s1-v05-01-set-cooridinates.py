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

Created: 2025.01.12
Modified: 2025.01.12
"""
# Imports
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction
from PyQt5.Qt import QLabel
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
            #label0 = QLabel(self)        # label w/out text, widnow is the parent
            label:QLabel = QLabel("Our first label!", self) # default position: overlays menubar
            label.move(10, 50)          # postion label below menubar
                                        #(to the right of the parent -> x,
                                        # x50 pixels to the down of the parent ---> y)

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
    