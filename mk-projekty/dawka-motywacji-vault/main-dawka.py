"""
Klasa do zarządzania plikiem dawka motywacji, np. do konwersji na plik json.

To do: 
	1. dodać losowanie cytatu do konsoli linuxa
	2. zmodyfikowac GUI  (losuj-cytat-?-qt.py)

Created: 2025.03.04
Modified: 2025.03.11
Author: MK
"""

from file_paths import FilePaths
from odt_2_txt import Odt2TxtConverter
from txt_2_json import Txt2JsonConverter
from motto_selector import MottoSelector

if __name__ == "__main__":

    names = ["dawka-motywacji", "52-notatki", "2007_Ruiz_Cztery-umowy"]
    for name in names:
        print("*"*100)
        print(f"Przetwarzanie pliku: {name}")

        file_paths = FilePaths(name)
        odt_converter = Odt2TxtConverter(file_paths)    
        odt_converter.odt_2_txt()        
        
        txt_json_converter = Txt2JsonConverter(file_paths)
        txt_json_converter.save_to_json()

        motto_selector = MottoSelector(file_paths)
        print()
        print(f"Liczba autorów: {motto_selector.get_number_of_autors()}")
        print(f"Liczba mott: {motto_selector.get_number_of_mottoes()}")
        print("-"*100)

        print(motto_selector.random_motto())
        print("-"*100)

        autor = motto_selector.random_autor()    
        cytaty = motto_selector.autor_motto_list[autor]
        print(f"{autor}:{motto_selector.autor_motto_count[autor]}")
        for k, cytat in enumerate(cytaty):
            print(f"   {k+1}. {cytat}")
        print("-"*100)
        print()
