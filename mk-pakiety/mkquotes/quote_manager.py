"""
Created: 2025.03.14
Modified: 2025.03.15
Author: MK
"""
from .quote import Quote

class QuoteManager:
    """
    Klasa zarządzająca mottami.

    Zawiera listę mott, metadane, liczbę autorów i liczbę mott.
    """
    def __init__(self) -> None:
        self.quotes: list[Quote] = []
        self.meta_data: dict = {}
        self.number_of_autors = 0
        self.number_of_quotes = 0

    def get_number_of_autors(self) -> int:
        return self.number_of_autors

    def get_number_of_quotes(self) -> int:
        return self.number_of_quotes
    

