#! /usr/bin/env python3
"""
Skrypt testujący działanie klasy QuoteManager.

Created: 2025.03.22
Modified: 2025.03.22
Author: MK
"""

from mkquotes.quote_manager import QuoteManager
from mkquotes.quote_file_paths import FilePaths
from mkquotes.json_loader import JsonLoader
from mkquotes.json_saver import JsonSaver

def main():
    file_paths = FilePaths("dawka-motywacji", create="json")
    quote_manager = QuoteManager()

    json_loader = JsonLoader(file_paths)
    json_saver = JsonSaver(file_paths)

    quote_manager.set_json_loader(json_loader)
    quote_manager.set_json_saver(json_saver)

    quote_manager.save_to_json(test_mode=True)


if __name__ == "__main__":
    main()