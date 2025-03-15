"""
Created: 2025.03.10
Modified: 2025.03.15
Author: MK
"""

import subprocess
from pathlib import Path

from .quote_file_paths import FilePaths

class Odt2TxtConverter:
        
    def __init__(self, file_paths: FilePaths):
        self.file_paths = file_paths
        
    def odt_2_txt(self):
        """
        Konwertuje cytaty z pliku odt na txt.
        Wykorzystuje LibreOffice w trybie headless do konwersji.
        """        
        
        base_name = self.file_paths.base_name
        base_folder = self.file_paths.base_folder
        input_file = base_folder / f"{base_name}.odt"
        
        # Sprawdzenie czy plik istnieje
        if not input_file.exists():
            raise FileNotFoundError(f"Plik {input_file} nie znaleziony")
        
        try:
            # Wykonanie komendy konwersji
            cmd = ["libreoffice", "--headless", "--convert-to", "txt", str(input_file)]
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            
            # Przeniesienie pliku do katalogu cytaty, jeśli został utworzony w bieżącym katalogu
            output_file = Path(f"{base_name}.txt")
            if output_file.exists():
                target_path = base_folder / output_file.name
                output_file.rename(target_path)
                print(f'Plik: \"{input_file}\" -----> \"{target_path}\"')
            else:
                print("Konwersja zakończona, ale nie znaleziono pliku wyjściowego")
                
        except subprocess.CalledProcessError as e:
            print(f"Błąd podczas konwersji pliku: {e}")
            print(f"Wyjście błędu: {e.stderr}")
        except Exception as e:
            print(f"Wystąpił nieoczekiwany błąd: {e}")


if __name__ == "__main__":

    names = ["dawka-motywacji", "52-notatki", "2007_Ruiz_Cztery-umowy"] 
    for name in names:
        print(f"\n\"{name}\":")
        file_paths = FilePaths(name)

        odt_converter = Odt2TxtConverter(file_paths)
        odt_converter.odt_2_txt()







