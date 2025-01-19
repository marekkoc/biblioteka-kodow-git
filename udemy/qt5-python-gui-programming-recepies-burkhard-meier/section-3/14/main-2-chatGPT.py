"""
Udemy.com
Kurs: Python GUI programming Recipies using PyQt5
url: https://www.udemy.com/course/python-gui-programming-recipes-using-pyqt5/?couponCode=KEEPLEARNING

       
Sekcja 14: 

Created: 2025.01.16
Modified: 2025.01.16
"""

import sys
from PyQt5 import QtCore, QtWidgets
from MainWindow_14 import Ui_MainWindow


class MainWindow:
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
        self.ui.treeWidget.headerItem().setText(1, "Header 2")

    # ----- CALENDAR ------------------------------------------------
    def update_calendar(self):
        self.ui.calendarWidget.selectionChanged.connect(self.update_date)

    def update_date(self):
        self.ui.dateEdit.setDate(self.ui.calendarWidget.selectedDate())

    # -- PROGRESS BAR -------------------------------------------------------
    def update_progressbar(self):
        self.ui.radioButton_start.clicked.connect(self.start_progressbar)
        self.ui.radioButton_stop.clicked.connect(self.stop_progressbar)
        self.ui.radioButton_reset.clicked.connect(self.reset_progressbar)

        self.progress_value = 0
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.increment_progressbar)

    def start_progressbar(self):
        """Rozpoczyna postęp paska przy użyciu QTimer."""
        if not self.timer.isActive():
            self.timer.start(100)  # Odświeżanie co 100 ms (wolniejsze ładowanie)

    def stop_progressbar(self):
        """Zatrzymuje postęp paska bez resetowania."""
        if self.timer.isActive():
            self.timer.stop()

    def reset_progressbar(self):
        """Resetuje pasek postępu do wartości początkowej."""
        self.timer.stop()
        self.progress_value = 0
        self.ui.progressBar.setValue(0)

    def increment_progressbar(self):
        """Zwiększa wartość paska postępu."""
        if self.progress_value < 100:
            self.progress_value += 1
            self.ui.progressBar.setValue(self.progress_value)
        else:
            self.timer.stop()  # Zatrzymanie, gdy osiągnie 100%

    def print_tree(self):
        header0 = self.ui.treeWidget.headerItem().text(0)
        header1 = self.ui.treeWidget.headerItem().text(1)
        print(f"\nOriginally: {header0}\nUpdated: {header1}\n")


if __name__ == "__main__":
    app = MainWindow()