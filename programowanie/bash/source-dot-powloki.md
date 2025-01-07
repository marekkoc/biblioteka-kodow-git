---
Utworzono: 2024-10-31T13:58:00
Zmodyfikowano: 2024-10-31T13:58:00
Źródło: chatGPT
tags:
---

Polecenia `source` oraz `.` (`dot command`) w Bashu pozwalają na wykonanie skryptu w bieżącej powłoce zamiast w osobnym procesie. Dzięki temu wszelkie zmiany wprowadzone przez skrypt – takie jak przejście do innego katalogu, zmiana zmiennych środowiskowych, funkcji i aliasów – zostają zachowane po zakończeniu skryptu. 

Oto jak to działa:

### Jak działa `source` i `.`
1. **Standardowe uruchomienie skryptu (np. `bash skrypt.sh`)**:
   - Gdy uruchamiasz skrypt w ten sposób, system tworzy *nową instancję* powłoki, która wykonuje wszystkie polecenia skryptu.
   - Po zakończeniu skryptu ta nowa instancja powłoki jest usuwana, a wszystkie zmiany wprowadzone w tym procesie (np. `cd ..`) *nie wpływają na powłokę główną*.
   
2. **Uruchomienie skryptu za pomocą `source skrypt.sh` lub `. skrypt.sh`**:
   - Uruchomienie skryptu w ten sposób sprawia, że wykonywane są jego polecenia bezpośrednio w bieżącej powłoce.
   - Dzięki temu zmiany dokonane w trakcie wykonywania skryptu, takie jak:
     - przejście do innego katalogu (`cd`),
     - ustawienie lub modyfikacja zmiennych środowiskowych,
     - definiowanie nowych aliasów i funkcji
     
     zostają zapisane w bieżącej sesji powłoki.
   - `source` i `.` działają identycznie – są to po prostu dwa różne sposoby na osiągnięcie tego samego rezultatu.

### Przykład użycia

Załóżmy, że mamy skrypt `zmiana_sciezki.sh` o treści:

```bash
#!/bin/bash
cd /home
echo "Teraz jesteś w katalogu: $(pwd)"
```

#### Standardowe uruchomienie:

```bash
bash zmiana_sciezki.sh
echo "Po uruchomieniu skryptu jesteś w katalogu: $(pwd)"
```

Wynik:
1. Skrypt przejdzie do katalogu `/home` i wyświetli `Teraz jesteś w katalogu: /home`.
2. Jednak po zakończeniu skryptu powracasz do katalogu, w którym zaczynałeś, ponieważ `cd` wykonane w skrypcie nie ma wpływu na katalog bieżącej powłoki.

#### Uruchomienie z `source` lub `.`:

```bash
source zmiana_sciezki.sh
echo "Po uruchomieniu skryptu jesteś w katalogu: $(pwd)"
```

Wynik:
1. Skrypt przejdzie do katalogu `/home` i wyświetli `Teraz jesteś w katalogu: /home`.
2. Po zakończeniu skryptu bieżąca powłoka również będzie w katalogu `/home`.

### Kiedy używać `source`?
Polecenie `source` jest przydatne wtedy, gdy:
- Chcesz, by zmiany dokonane w skrypcie były dostępne w bieżącej sesji (np. zmiana katalogu lub ustawienie zmiennych środowiskowych).
- Potrzebujesz załadować ustawienia lub funkcje do bieżącej sesji powłoki (np. przez załadowanie `.bashrc` lub innego skryptu inicjującego).

### Uwagi
- Nie zaleca się używania `source` dla skryptów, które wykonują zadania niezależne od bieżącej sesji powłoki, ponieważ mogą zmieniać środowisko powłoki w nieprzewidywalny sposób.
- `source` jest bardziej powszechnie używane w systemach UNIX/Linux, a w skryptach Basha jest to preferowany sposób na załadowanie ustawień bez opuszczania bieżącej powłoki.