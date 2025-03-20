"""
Created: 2025.03.19
Modified: 2025.03.19
Author: MK
"""

import json 
import datetime

from .quote import Quote
from .quote_file_paths import FilePaths

class JsonSaver:
    """
    Klasa zapisująca dane do pliku JSON.
    """
    def __init__(self, file_paths: FilePaths) -> None:
        self.file_paths = file_paths
        self.meta_data = {}
        self.quotes = []
        
    def set_meta_data(self, meta_data: dict) -> None:
        self.meta_data = meta_data

    def set_quotes(self, quotes: list[Quote]) -> None:
        self.quotes = quotes
        self.number_of_autors = len(set([quote.autor for quote in self.quotes]))     
        self.number_of_quotes = len(self.quotes)  
    
    def save_to_json(self, **kwargs) -> None:
        """
        Zapisuje metadane i motta do pliku JSON.
        
        Args:
            **kwargs: Opcjonalne argumenty słownikowe, które zostaną dodane do meta_data.
            
        Returns:
            None: Funkcja nie zwraca wartości, ale wyświetla komunikat o powodzeniu lub błędzie.
        """
        # Sprawdzenie czy quotes nie jest pustą listą
        if not self.quotes:
            print("Błąd: Nie można zapisać pliku - lista cytatów jest pusta.")
            return
            
        # Dodanie aktualnej daty i godziny do meta_data
        meta_data = self.meta_data.copy()
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        meta_data['Modified'] = current_time
        meta_data['Number_of_autors'] = self.number_of_autors
        meta_data['Number_of_quotes'] = self.number_of_quotes
        
        # Dodanie opcjonalnych argumentów słownikowych do meta_data
        for key, value in kwargs.items():
            meta_data[key] = value
            
        # Sprawdzenie czy meta_data zawiera tylko klucz 'Modified'
        if len(meta_data) == 1 and 'Modified' in meta_data:
            print("Błąd: Nie można zapisać pliku - metadane zawierają tylko datę aktualizacji.")
            return

        data = {
            "meta_data": meta_data,
            "quotes": [quote.to_dict() for quote in self.quotes]
        }        
        try:
            with open(self.file_paths.file_path_json, 'w', encoding='utf-8') as plik:
                json.dump(data, plik, ensure_ascii=False, indent=4)
            print(f'Dane zapisane do pliku \"{self.file_paths.file_path_json}\"')
        except Exception as e:
            print(f"Wystąpił błąd podczas zapisywania do pliku: {e}")


