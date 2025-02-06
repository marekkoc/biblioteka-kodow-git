#!/bin/bash

# Skrytp wyszukuje katalogi .obsidian i tworzy plik znacznika z datą utworzenia.
# Skrypt powinien być uruchamiany z katalogu głównego projektu.
# Jeśli nie podano argumentu, używany jest katalog bieżący (".").
# Jeśli podano argument, sprawdzane jest czy katalog istnieje

# C:2025-02-06
# M:2025-02-06

#!/bin/bash

# Sprawdź czy podano argument (katalog startowy)
if [ $# -eq 0 ]; then
    start_dir="."  # Domyślnie użyj bieżącego katalogu
else
    start_dir="$1" # Użyj katalogu podanego jako argument
    # Sprawdź czy podany katalog istnieje
    if [ ! -d "$start_dir" ]; then
        echo "Błąd: Katalog '$start_dir' nie istnieje!"
        exit 1
    fi
fi

echo "Rozpoczynam wyszukiwanie vault'ów Obsidian w: $start_dir"
echo "----------------------------------------"

# Licznik znalezionych i zaktualizowanych vault'ów
found_count=0
updated_count=0

# Przetwarzaj każdy znaleziony katalog .obsidian
while IFS= read -r dir; do
    ((found_count++))
    vault_dir=$(dirname "$dir")
    marker_file="$vault_dir/tu-jest-obsidian-vault.txt"
    
    if [ ! -f "$marker_file" ]; then
        current_datetime=$(date "+%Y-%m-%d %H:%M:%S")
        echo "Utworzono $current_datetime" > "$marker_file"
        echo "✓ Utworzono plik znacznika w: $vault_dir"
        ((updated_count++))
    else
        echo "• Plik znacznika już istnieje w: $vault_dir"
    fi
done < <(find "$start_dir" -type d -iname .obsidian)

echo "----------------------------------------"
echo "Zakończono przeszukiwanie."
echo "Znaleziono vault'ów: $found_count"
echo "Utworzono nowych plików znaczników: $updated_count"


