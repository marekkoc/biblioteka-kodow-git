Aby usunąć wybrane środowisko w Conda, możesz postępować zgodnie z poniższymi krokami:

---

### 1. **Lista dostępnych środowisk**
Najpierw upewnij się, jakie środowiska są zainstalowane. Użyj polecenia:

```bash
conda env list
```

To wyświetli listę wszystkich środowisk, np.:

```
# conda environments:
#
base                  *  /home/user/anaconda3
my_env                   /home/user/anaconda3/envs/my_env
data_env                 /home/user/anaconda3/envs/data_env
```

Zapamiętaj nazwę środowiska, które chcesz usunąć (np. `my_env`).

---

### 2. **Usunięcie środowiska**
Aby usunąć wybrane środowisko (np. `my_env`), użyj polecenia:

```bash
conda env remove --name my_env
```

---

### 3. **Sprawdzenie, czy środowisko zostało usunięte**
Ponownie wyświetl listę środowisk:

```bash
conda env list
```

Jeśli środowisko zostało poprawnie usunięte, nie będzie go na liście.

---

### Dodatkowe uwagi
- **Usuwanie środowisk zajmujących dużo miejsca**  
  Jeśli chcesz dodatkowo oczyścić pamięć, możesz uruchomić polecenie:

  ```bash
  conda clean --all
  ```

  To usunie wszystkie tymczasowe pliki, nieużywane pakiety i cache.

- **Usunięcie środowiska z pliku YAML**  
  Jeśli środowisko było utworzone z pliku YAML, usunięcie środowiska za pomocą `conda env remove` również usuwa wszystkie jego zależności.

- **Środowisko `base` nie może być usunięte**  
  Środowisko bazowe (`base`) jest domyślnym środowiskiem Conda i nie może zostać usunięte.
