#! /usr/bin/env python3
"""
Skrypt testujący działanie klasy Txt2JsonConverter.

Created: 2025.03.22
Modified: 2025.03.22
Author: MK
"""

from mkquotes.txt_2_json import Txt2JsonConverter
from mkquotes.quote_file_paths import FilePaths
from mkquotes.json_saver import JsonSaver
from mkquotes.quote import Quote
from mkquotes.old.quote_instances import DAWKA, NOTATKI, UMOWY, ALL_QUOTE_FILE_NAMES

if __name__ == "__main__":

    def main():

        print()
        for name in ["dawka-motywacji", "52-notatki", "2007_Ruiz_Cztery-umowy"]:
            print(f"\"{name}\":")
            
            file_paths = FilePaths(name, create="json-txt")
            json_saver = JsonSaver(file_paths)
            raw_file = Txt2JsonConverter(json_saver) 
            
            print()
        print()

    main()