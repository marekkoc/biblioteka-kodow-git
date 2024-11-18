"""
Project: Daily weight analysis.

Copyright: Marek


Created: 2024.11.17
Modified: 2024.11.18
"""
import os
import pandas as pd
from folders import Folders


class ExcelFile:    

    def __init__(self, pth_to_excel_file):
        self._pth_to_excel_file = pth_to_excel_file
        self._year_list = [str(y) for y in range(2017, 2025)]
        self._year_dct = {}
    
        self._load_excel_data()
        self._set_sheets()

    def _load_excel_data(self):
        # open excel spreadsheet and read sheets with data for each year
        try:
            with open(self._pth_to_excel_file, "r") as file:
                self._excel = pd.read_excel(self._pth_to_excel_file, sheet_name=self._year_list, index_col=0)
        except FileNotFoundError:
            print("Plik nie został znaleziony. Sprawdź ścieżkę dostępu.")
            self._excel = None

    def _set_sheets(self):
        for year in self._year_list:
            self._year_dct[year] =  self._excel[year].iloc[:31,:12]
            self._year_dct[year] = self._year_dct[year].replace(',', '.', regex=True)
            self._year_dct[year] = self._year_dct[year].apply(pd.to_numeric, errors='coerce')

            cols = ['styczen', 'luty', 'marzec', 'kwiecien', 'maj', 'czerwiec',
            'lipiec', 'sierpien', 'wrzesien', 'pazdziernik', 'listopad', 'grudzien']
            old = list(range(1,13))
            dct = dict(zip(old, cols))
            self._year_dct[year].rename(columns=dct, inplace=True)

    def get_sheet(self, key):
        return self._year_dct[str(key)]



if __name__ == "__main__":
    f = Folders()
    e = ExcelFile(f.get_excel_file_path())
    print(e._year_dct.keys())
    print(e.get_sheet(2017).shape)
    