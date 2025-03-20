"""
Created: 2025.03.14
Modified: 2025.03.19
Author: MK
"""

from .quote import Quote
from .quote_file_paths import FilePaths
from .json_loader import JsonLoader
from .json_saver import JsonSaver

class QuoteManager:
    """
    Klasa zarządzająca mottami.

    Zawiera listę mott, metadane, liczbę autorów i liczbę mott.
    """
    def __init__(self) -> None:
        self.json_loader: JsonLoader | None = None
        self.json_saver: JsonSaver | None = None
        self.quotes: list[Quote] = []
        self.meta_data: dict = {}
        self.number_of_autors = 0
        self.number_of_quotes = 0

    def set_json_loader(self, json_loader: JsonLoader) -> None:
        self.json_loader = json_loader
        self.quotes = self.json_loader.get_quotes()
        self.meta_data = self.json_loader.get_meta_data()
        self.number_of_autors = self.json_loader.get_number_of_autors()
        self.number_of_quotes = self.json_loader.get_number_of_quotes()

    def set_json_saver(self, json_saver: JsonSaver) -> None:
        self.json_saver = json_saver  
        self.json_saver.set_meta_data(self.meta_data)
        self.json_saver.set_quotes(self.quotes)

    def save_to_json(self) -> None:
        if self.json_saver is None:
            raise ValueError("JsonSaver is not set")          
        self.json_saver.save_to_json()

    def get_number_of_autors(self) -> int:
        return self.number_of_autors

    def get_number_of_quotes(self) -> int:
        return self.number_of_quotes
    
if __name__ == "__main__":

    for name in ["dawka-motywacji", "52-notatki", "2007_Ruiz_Cztery-umowy"]:

        file_paths = FilePaths(name)
        json_loader = JsonLoader(file_paths)
        json_saver = JsonSaver(file_paths)

        quote_manager = QuoteManager()

        quote_manager.set_json_loader(json_loader)
        quote_manager.set_json_saver(json_saver)
        quote_manager.save_to_json()
