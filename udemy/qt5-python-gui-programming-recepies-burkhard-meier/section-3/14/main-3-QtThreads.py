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

    # ---- PRINT TREE ------------------------------------------------
    def print_tree(self):
        header0 = self.ui.treeWidget.headerItem().text(0)
        header1 = self.ui.treeWidget.headerItem().text(1)
        print(f"\nOriginally: {header0}\nUpdated: {header1}\n")

    
    # -- PROGRES BAR -------------------------------------------------------

    def update_progressbar(self):
        self.ui.radioButton_start.clicked.connect(self.start_progressbar)
        self.ui.radioButton_stop.clicked.connect(self.stop_progressbar)
        self.ui.radioButton_reset.clicked.connect(self.reset_progressbar)
        self.progras_value = 0
        self. stop_progress = False


    def progressbar_counter(self, start_value = 0):
        self.run_thread = RunThread(parent=None, counter_start=start_value)
        self.run_thread.start()
        self.run_thread.counter_value.connect(self.set_progressbar)

    def set_progressbar(self, counter):
        if not self.stop_progress:
            self.ui.progressBar.setValue(counter)
    
    def start_progressbar(self):
        self.stop_progress = False
        self.progras_value = self.ui.progressBar.value()
        self.progressbar_counter(self.progras_value)


    def stop_progressbar(self):
        self.progras_value = True
        try:
            self.run_thread.stop()
        except: pass

    def reset_progressbar(self):        
        self.stop_progressbar()
        self.progras_value = 0
        self.stop_progress = False
        self.ui.progressBar.reset()


class RunThread(QtCore.QThread):
    counter_value = QtCore.pyqtSignal(int) # define a new signal

    def __init__(self, parent=None, counter_start=0):
        super(RunThread, self).__init__(parent)
        self.counter = counter_start
        self.is_running = True

    def run(self):
        while self.counter < 100 and self.is_running == True:
            sleep(0.1)
            self.counter += 1
            print(self.counter, end='\r')
            self.counter_value.emit(self.counter) # emit a new Signal with value

    def stop(self):
        self.is_running = False
        print('stopping thread...')
        self.terminate()










if __name__ == "__main__":
    
    app = MainWindow()
    
