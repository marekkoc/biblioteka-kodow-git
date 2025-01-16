"""
Udemy.com
Kurs: Python GUI programming Recipies using PyQt5
url: https://www.udemy.com/course/python-gui-programming-recipes-using-pyqt5/?couponCode=KEEPLEARNING

       
Sekcja 12: Separation Python code from automatically generated UI code.

Created: 2025.01.14
Modified: 2025.01.14
"""

from MainWindow import Ui_MainWindow

from PyQt5 import QtCore, QtGui, QtWidgets


def set_table_items(item1="item 1", item2="item 2", item3="item 3"):
    ### tu możemy wprowadzać zmiany i one nie znikiną! ###
    row = 0
    ui.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(item1))
    ui.tableWidget.setItem(1, 1, QtWidgets.QTableWidgetItem(item2))
    ui.tableWidget.setItem(2, 2, QtWidgets.QTableWidgetItem(item3))


def button_clicked(): 
    #ui.pushButton.setText("Button was clicked")
    set_table_items(item2=str(100))

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    # insert items into the table
    set_table_items()

    # connect a button with a function
    ui.pushButton.clicked.connect(button_clicked)
    ui.pushButton.clicked.connect(lambda: ui.pushButton.setText("Button was clicked!"))



    MainWindow.show()
    sys.exit(app.exec_())