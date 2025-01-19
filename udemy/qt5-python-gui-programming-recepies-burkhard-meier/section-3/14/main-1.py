"""
Udemy.com
Kurs: Python GUI programming Recipies using PyQt5
url: https://www.udemy.com/course/python-gui-programming-recipes-using-pyqt5/?couponCode=KEEPLEARNING

       
Sekcja 14: 

Created: 2025.01.16
Modified: 2025.01.16
"""

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from MainWindow_14 import Ui_MainWindow



class MainWindow():
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(MainWindow)

        self.update_tree()
        self.update_calendar()
        self.update_progressbar()

        MainWindow.show()
        sys.exit(app.exec_())

    def update_tree(self):
        #self.print_tree()
        self.ui.treeWidget.headerItem().setText(1, "Header 2")
        #self.print_tree()

        #self.ui.treeWidget.topLevelItem(0).setText(0, "Kol 1")    
        #self.ui.treeWidget.topLevelItem(0).setText(1, "Kolumna 2")    

        #print(self.ui.treeWidget.topLevelItem(0).text(0))
        #print(self.ui.treeWidget.topLevelItem(0).child(0).text(0))
    
    #----- CALENDAR ------------------------------------------------
    def update_calendar(self):
        self.ui.calendarWidget.selectionChanged.connect(self.update_date)

    def update_date(self):
        self.ui.dateEdit.setDate(self.ui.calendarWidget.selectedDate())
    
    # -- PROGRES BAR -------------------------------------------------------

    def update_progressbar(self):
        self.ui.radioButton_start.clicked.connect(self.start_progressbar)
        self.ui.radioButton_stop.clicked.connect(self.stop_progressbar)
        self.ui.radioButton_reset.clicked.connect(self.reset_progressbar)
        self.progras_value = 0
        self. stop_progress = False
    
    def start_progressbar(self):
        #self.stop_progress = False
        self.progras_value = self.ui.progressBar.value()

        while (self.progras_value < 100) and not (self.ui.radioButton_stop.isChecked()):
            self.ui.progressBar.setValue(self.progras_value)
            #self.progras_value += 1
            self.progras_value += 0.0001
            QtWidgets.QApplication.processEvents()


    def stop_progressbar(self):
        self.progras_value = True

    def reset_progressbar(self):
        self.progras_value = 0
        self.ui.progressBar.reset()
        self.stop_progress = False

    def print_tree(self):
        header0 = self.ui.treeWidget.headerItem().text(0)
        header1 = self.ui.treeWidget.headerItem().text(1)
        print(f"\nOriginally: {header0}\nUpdated: {header1}\n")






if __name__ == "__main__":
    
    app = MainWindow()
    
