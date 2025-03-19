#!/home/marek/miniconda3/envs/py312/bin/python
"""
Program do zarzadzania cytatami.

Created: 2025.03.18
Modified: 2025.03.18
Author: MK
"""
import sys

from PyQt5 import QtWidgets, Qt
from MainWindow import Ui_MainWindow


from mkquotes import FilePaths
from mkquotes import Odt2TxtConverter
from mkquotes import Txt2JsonConverter
from mkquotes import QuoteSelector

if __name__ == "__main__":
   
    def losuj_cytat():
        quote_selector = QuoteSelector(FilePaths("dawka-motywacji"))
        cytat = quote_selector.random_quote()
        ui.label_cytat.setText(cytat.tekst)
        ui.label_autor.setText(cytat.autor)

    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")  # Lub inny styl: "Windows", "WindowsVista", itp.
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    ui.button_random.clicked.connect(losuj_cytat)



    MainWindow.show()
    sys.exit(app.exec_())

 
    print()
    quote_selector = QuoteSelector(FilePaths("dawka-motywacji"))
    print(quote_selector.random_quote())
    print()

