#! /usr/bin/env python3

"""
Skrypt testujący. Sprawdza działanie klsy do losowego wyboru cytatu.

Created: 2025.03.20
Modified: 2025.03.22

Author: MK
"""

from mkquotes.quote_selector import QuoteSelector
from mkquotes.quote_file_paths import FilePaths
from mkquotes.json_loader import JsonLoader

def main():
    print()
    file_paths = FilePaths("2007_Ruiz_Cztery-umowy", create="json")
    quote_selector = QuoteSelector()
    quote_selector.set_json_loader(JsonLoader(file_paths))
    print(quote_selector.random_quote())
    print()

def test():
    file_paths = FilePaths("dawka-motywacji", create="json")
    
    quote_selector = QuoteSelector()
    quote_selector.set_json_loader(JsonLoader(file_paths))
    print(quote_selector.random_quote())

if __name__ == "__main__":
    main() 
    test()