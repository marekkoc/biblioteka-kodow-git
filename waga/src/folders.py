"""
Project: Daily weight analysis.
Class Folders, to deal with folder pahts and file names.

Copyright: Marek


Created: 2024.11.18
Modified: 2024.11.19
"""

from pathlib import Path

class Folders:
    def __init__(self, excel_file_name = '20241113_waga.xlsx'):

        # paths to project folders
        self._project_folder_pth = Path.home() / "biblioteka-repozytoriow-git" / 'biblioteka-kodow-git' / 'waga'
        self._data_folder_pth =  self._project_folder_pth / 'data'
        self._result_folder_path = self._project_folder_pth / "results"   
        
        # source excel spreadsheet    
        self._excel_file_name = excel_file_name
        self._excel_file_pth = self._data_folder_pth / excel_file_name

        # check if result folder exists, if not create it
        if not self._result_folder_path.exists(): os.mkdir(self._result_folder_path)          

    def get_result_folder(self):
        return self._result_folder_path 
    
    def get_excel_file_name(self):
        return self._excel_file_name
    
    def get_excel_file_path(self):
        return self._excel_file_pth





if __name__ == "__main__":
     f = Folders()
     print()
     print(f.get_result_folder())
     print(f._project_folder_pth)
     print(f.get_excel_file_name())
     print(f.get_excel_file_path())
     print()