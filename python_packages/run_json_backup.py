#! /usr/bin/env python3
"""
Skrypt testujący. Tworzy kopie zapasowe plików JSON.

Created: 2025.03.20
Modified: 2025.03.22

Author: MK
"""

from mkquotes.json_backup import JsonBackup
from mkquotes.quote_file_paths import FilePaths

def main():
    for file_name in ["dawka-motywacji", "52-notatki", "2007_Ruiz_Cztery-umowy"]:
        file_paths = FilePaths(file_name, create="json")
        json_backup = JsonBackup(file_paths)
        json_backup.backup()

if __name__ == "__main__":
    main()