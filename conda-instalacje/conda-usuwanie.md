Aby całkowicie usunąć Condę z systemu Linux, musisz usunąć jej pliki i katalogi oraz zaktualizować konfigurację systemową, aby usunąć zmienne środowiskowe dodane przez Condę. Oto szczegółowe kroki:

---

### 1. **Dezaktywuj Condę (jeśli jest aktywna)**
Jeśli jesteś w aktywnym środowisku Conda, dezaktywuj je:

```bash
conda deactivate
```

---

### 2. **Zlokalizuj katalog instalacyjny Condy**
Domyślnie Conda jest instalowana w katalogu domowym użytkownika, np. w:

```plaintext
~/anaconda3
```

lub

```plaintext
~/miniconda3
```

Jeśli masz pewność, gdzie została zainstalowana Conda, przejdź do tego kroku. Jeśli nie, możesz znaleźć jej lokalizację, używając polecenia:

```bash
which conda
```

To zwróci ścieżkę do pliku binarnego Condy, np. `/home/user/miniconda3/bin/conda`. Oznacza to, że katalog instalacyjny to `/home/user/miniconda3`.

---

### 3. **Usuń katalog instalacyjny**
Usuń cały katalog instalacyjny Condy, np.:

```bash
rm -rf ~/anaconda3
```

lub

```bash
rm -rf ~/miniconda3
```

---

### 4. **Usuń wpisy Condy z plików konfiguracyjnych**
Conda modyfikuje pliki konfiguracyjne powłoki (np. `.bashrc`, `.zshrc`) podczas instalacji, dodając ścieżki do zmiennych środowiskowych. Usuń te wpisy:

1. Otwórz plik konfiguracyjny w edytorze, np.:

   ```bash
   nano ~/.bashrc
   ```

   lub dla Zsh:

   ```bash
   nano ~/.zshrc
   ```

2. Znajdź sekcje dodane przez Condę, np.:

   ```bash
   # >>> conda initialize >>>
   # !! Contents within this block are managed by 'conda init' !!
   __conda_setup="$('/home/user/miniconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
   ...
   # <<< conda initialize <<<
   ```

3. Usuń te linie.

4. Zapisz zmiany i zamknij edytor.

5. Zaktualizuj konfigurację powłoki:

   ```bash
   source ~/.bashrc
   ```

   lub dla Zsh:

   ```bash
   source ~/.zshrc
   ```

---

### 5. **Usuń cache Condy**
Aby upewnić się, że wszystkie tymczasowe pliki Condy zostały usunięte, usuń katalog `.conda` i `.continuum` w katalogu domowym:

```bash
rm -rf ~/.conda ~/.continuum
```

---

### 6. **Usuń dowiązania symboliczne i binaria (opcjonalnie)**
Jeśli Conda była dodana do `/usr/local/bin` lub innej globalnej lokalizacji, usuń dowiązania:

```bash
sudo rm /usr/local/bin/conda
sudo rm /usr/local/bin/conda-env
```

---

### 7. **Sprawdź, czy Conda została usunięta**
Upewnij się, że Conda nie jest już dostępna w systemie:

```bash
which conda
```

Powinno zwrócić pusty wynik.

---

### 8. **(Opcjonalnie) Usuń plik instalacyjny**
Jeśli masz plik instalacyjny Condy (np. instalator `.sh`), możesz go usunąć, aby zwolnić miejsce:

```bash
rm ~/Downloads/Miniconda3-latest-Linux-x86_64.sh
```

---

Po wykonaniu tych kroków Conda zostanie całkowicie usunięta z Twojego systemu Linux.
