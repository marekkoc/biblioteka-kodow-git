import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from MainWindow_13 import Ui_MainWindow



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
    
    def update_calendar(self):
        self.ui.calendarWidget.selectionChanged.connect(self.update_date)

    def update_date(self):
        self.ui.dateEdit.setDate(self.ui.calendarWidget.selectedDate())

    
    def update_progressbar(self):
        radio_3 = self.ui.radioButton_3.text()
        self.ui.radioButton_3.setText("Set Progresbar :p")
        radio_3_upd = self.ui.radioButton_3.text()
        print(radio_3, radio_3_upd)

        self.ui.radioButton_3.clicked.connect(self.set_progressbar)

    
    def set_progressbar(self):
        progress_value = self.ui.progressBar.value()
        print(f"Old progressBar: {progress_value}")

        new_value = self.ui.lcdNumber.value()
        self.ui.progressBar.setValue(int(new_value))
        print(f"New progressBar: {progress_value}\n")




    def print_tree(self):
        header0 = self.ui.treeWidget.headerItem().text(0)
        header1 = self.ui.treeWidget.headerItem().text(1)
        print(f"\nOriginally: {header0}\nUpdated: {header1}\n")






if __name__ == "__main__":
    
    app = MainWindow()
    
