"""
Created: 2025.03.10
Modified: 2025.03.19
Author: MK
"""

import json
import datetime
import random

from .quote import Quote
from .quote_file_paths import FilePaths
from .json_loader import JsonLoader
from .json_saver import JsonSaver
from .quote_manager import QuoteManager


class QuoteSelector(QuoteManager):
    """
    Klasa selektująca motta w pliku JSON.
    """
    def __init__(self) -> None:
        super().__init__()       

        self.autor_quote_count = self._count_quotes_for_autor()    
        self.autor_quote_list = self._get_autor_with_quotes()
        self.autors = list(self.autor_quote_count.keys())

    def _count_quotes_for_autor(self) -> dict[str, int]:
        """
        Tworzy słownik, w którym kluczem jest autor, a wartością liczba mott autora.
        """
        autor_quote_count: dict[str, int] = {}
        for quote in self.quotes:
            if quote.autor not in autor_quote_count:
                autor_quote_count[quote.autor] = 1
            else:
                autor_quote_count[quote.autor] += 1
        return autor_quote_count

    def _get_autor_with_quotes(self) -> dict[str, list[str]]:
        """
        Tworzy słownik, w którym kluczem jest autor, a wartością lista wszystkich mott danegoautora.
        """
        dct: dict[str, list[str]] = {}
        for quote in self.quotes:
            if quote.autor not in dct:
                dct[quote.autor] = [quote.tekst]
            else:
                if quote.tekst not in dct[quote.autor]:
                    dct[quote.autor].append(quote.tekst)               
        return dct 

    def sort_by_autor(self) -> None:
        """
        Sortuje autory po autorze.
        """    
        self.autors.sort()
    
    def sort_by_count(self) -> None:
        """
        Sortuje autorow po liczbie mott.
        """    
        self.autors = sorted(self.autors, key=lambda x: self.autor_quote_count[x], reverse=True)

    def shuffle_autors(self) -> None:
        """
        Losowo miesza listę autorów.
        """        
        random.shuffle(self.autors)
    
    def random_autor(self) -> str:
        """
        Zwraca losowego autora.
        """
        return random.choice(self.autors)

    def random_quote(self) -> Quote:
        """
        Zwraca losowe motto.
        """
        return random.choice(self.quotes)
    
    def get_quotes(self) -> list[Quote]:
        return self.quotes
    
   

if __name__ == "__main__":

    def main():
        print()
        file_paths = FilePaths("2007_Ruiz_Cztery-umowy", create="json")
        quote_selector = QuoteSelector()
        quote_selector.set_json_loader(JsonLoader(file_paths))
        print(quote_selector.random_quote())
        print()
    def test():
        file_paths = FilePaths("2007_Ruiz_Cztery-umowy")
        quote_selector = QuoteSelector()
     
        print()
        print(f"Liczba autorów: {quote_selector.get_number_of_autors()}")
        print(f"Liczba mott: {quote_selector.get_number_of_quotes()}")
        print("-"*100)

        for autor in quote_selector.autors[:5]:
            print(f"{autor}: {quote_selector.autor_quote_count[autor]}")
        print("-"*100)

        quote_selector.sort_by_autor()
        for autor in quote_selector.autors[:5]:
            print(f"{autor}: {quote_selector.autor_quote_count[autor]}")
        print("-"*100)

        quote_selector.sort_by_count()
        for autor in quote_selector.autors[:5]:
            print(f"{autor}: {quote_selector.autor_quote_count[autor]}")
        print("-"*100)

        quote_selector.shuffle_autors()
        for autor in quote_selector.autors[:5]:
            print(f"{autor}: {quote_selector.autor_quote_count[autor]}")
        print("-"*100)

        print(quote_selector.random_quote())
        print("-"*100)

        autor = quote_selector.random_autor()    
        cytaty = quote_selector.autor_quote_list[autor]
        print(f"{autor}:{quote_selector.autor_quote_count[autor]}")
        for k, cytat in enumerate(cytaty):
            print(f"   {k+1}. {cytat}")
        print("-"*100)


    main()
    




