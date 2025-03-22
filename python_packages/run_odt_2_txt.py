#! /usr/bin/env python3
"""
Skrypt testujący działanie klasy Odt2TxtConverter.

Created: 2025.03.22
Modified: 2025.03.22
Author: MK
"""

from mkquotes.odt_2_txt import Odt2TxtConverter
from mkquotes.quote_file_paths import FilePaths


def main():
        names = ["dawka-motywacji", "52-notatki", "2007_Ruiz_Cztery-umowy"] 
        for name in names:
            print(f"\n\"{name}\":")
            file_paths = FilePaths(name, create="odt-txt")
            
            odt_converter = Odt2TxtConverter(file_paths)
            odt_converter.odt_2_txt()

if __name__ == "__main__":
    main()