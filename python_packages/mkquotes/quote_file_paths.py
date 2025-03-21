"""
Created: 2025.03.12
Modified: 2025.03.18
Author: MK
"""

from pathlib import Path
from mkenvs import EnvVars

class QuotePaths:
    def __init__(self, base_name: str, base_folder: Path | str | None = None) -> None:
        self.base_folder: Path  = Path(base_folder) if base_folder else Path(EnvVars.get_python_quotes())
        self.base_name = base_name
        
        
class ODTPaths(QuotePaths):
    extension = 'odt'
    
    def __init__(self, base_name: str, base_folder: Path | str | None = None) -> None:
        super().__init__(base_name, base_folder)
        
        self.odt_folder = Path(self.base_folder) / 'odt'
        self.odt_file = self.odt_folder / f"{self.base_name}.{ODTPaths.extension}"


class TXTPaths(QuotePaths):
    extension = 'txt'

    def __init__(self, base_name: str, base_folder: Path | str | None = None) -> None:
        super().__init__(base_name, base_folder)
        
        self.txt_folder = Path(self.base_folder) / 'txt'
        self.txt_file = self.txt_folder / f"{self.base_name}.{TXTPaths.extension}"       

class JSONPaths(QuotePaths):
    extension = 'json'

    def __init__(self, base_name: str, base_folder: Path | str | None = None) -> None:
        super().__init__(base_name, base_folder)
        
        self.json_folder = Path(self.base_folder) 
        self.json_file = self.json_folder / f"{self.base_name}.{JSONPaths.extension}"
        self.json_backup_folder = Path(self.base_folder) / 'json_backup'
               
        
class FilePaths:
    """
    Klasa agregująca wszystkie typy ścieżek do plików.
    Używa klas specjalistycznych do obsługi poszczególnych typów plików.
    """
    def __init__(self, base_name: str, base_folder: Path | str | None = None, create: str = "json-txt-odt") -> None:
        """
        Inicjalizuje obiekt FilePaths.

        Args:
            base_name (str): Nazwa podstawowa pliku.
            base_folder (str | None, optional): Ścieżka do folderu bazowego. Domyślnie None.
        """
        self.base_name = base_name
        self.base_folder = Path(base_folder) if base_folder else Path(EnvVars.get_python_quotes())  
        
        # Inicjalizacja poszczególnych typów ścieżek w zależności od parametrów
        
        self.odt = ODTPaths(base_name, base_folder) if "odt" in create else None
        self.txt = TXTPaths(base_name, base_folder) if "txt" in create else None
        self.json = JSONPaths(base_name, base_folder) if "json" in create else None
        
        # Dla zachowania kompatybilności wstecznej
        self.file_path_txt = self.txt.txt_file if self.txt else None
        self.file_path_json = self.json.json_file if self.json else None


if __name__ == "__main__":

    def main():
        names = ["dawka-motywacji", "52-notatki", "2007_Ruiz_Cztery-umowy"]        
        
        for name in names:
            file_paths = FilePaths(name)
            if file_paths.txt:
                print(f"Plik txt:\t{file_paths.txt.txt_file.name},    (istnieje: {file_paths.txt.txt_file.exists()})")
            if file_paths.json:
                print(f"Plik json:\t{file_paths.json.json_file.name}, (istnieje: {file_paths.json.json_file.exists()})")
            print()
            

    main()
