---
Utworzono: 2024-11-02T17:42:00
Zmodyfikowano: 2024-11-02T17:42:00
Źródło: 
tags:
---
# Ignorowanie katalogu  .ipynb_checkpoints we wszystkich podkatalogach?

Aby w repozytorium Git zignorować wszystkie katalogi `.ipynb_checkpoints` niezależnie od ich lokalizacji, wystarczy dodać odpowiednią regułę do pliku `.gitignore`. 

Oto jak to zrobić:

1. Otwórz lub utwórz plik `.gitignore` w głównym katalogu repozytorium.
2. Dodaj poniższą linię, aby zignorować wszystkie foldery `.ipynb_checkpoints` we wszystkich podkatalogach:

   ```
   **/.ipynb_checkpoints/
   ```

   Ta reguła zignoruje wszystkie katalogi `.ipynb_checkpoints`, bez względu na to, w którym miejscu drzewa katalogów się znajdują.

3. Zapisz zmiany w pliku `.gitignore`.
4. Jeśli katalogi `.ipynb_checkpoints` zostały już wcześniej dodane do repozytorium, musisz je usunąć z indeksu Git:

   ```bash
   git rm -r --cached .ipynb_checkpoints
   ```

5. Na koniec zatwierdź zmiany i wypchnij je do repozytorium:

   ```bash
   git add .gitignore
   git commit -m "Ignore .ipynb_checkpoints directories in all subdirectories"
   git push origin main
   ```

Po wykonaniu tych kroków katalogi `.ipynb_checkpoints` będą ignorowane w całym repozytorium.