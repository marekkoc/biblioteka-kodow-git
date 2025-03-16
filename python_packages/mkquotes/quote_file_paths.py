"""
Created: 2025.03.12
Modified: 2025.03.15
Author: MK
"""

from pathlib import Path
from mkenvs import EnvVars

class FilePaths:
    def __init__(self, base_name: str, base_folder: str | None = None) -> None:
        self.home_folder = Path.home()
        self.base_folder = Path(base_folder) if base_folder else Path(EnvVars.get_python_quotes())
        self.base_name = base_name
        self.txt_extension = 'txt'
        self.json_extension = 'json'
        self.file_path_txt = self.base_folder / f"{self.base_name}.{self.txt_extension}"
        self.file_path_json = self.base_folder / f"{self.base_name}.{self.json_extension}"


if __name__ == "__main__":

    def main():
        names = ["dawka-motywacji", "52-notatki", "2007_Ruiz_Cztery-umowy"]
        print()
        for name in names:
            file_paths = FilePaths(name)
            print(f"Plik txt: {file_paths.file_path_txt},   istnieje: {file_paths.file_path_txt.exists()}")
            print(f"Plik json: {file_paths.file_path_json}, istnieje: {file_paths.file_path_json.exists()}")
            print()

    main()
