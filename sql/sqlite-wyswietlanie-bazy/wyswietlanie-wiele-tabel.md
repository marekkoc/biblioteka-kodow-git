Obecny program domyślnie ładuje dane z **pierwszej tabeli** znalezionej w bazie danych, co może być niewystarczające w przypadku bazy danych zawierającej wiele tabel. Aby obsłużyć sytuację, gdy baza danych zawiera więcej niż jedną tabelę, możesz dodać funkcję wyboru tabeli.

### Propozycja zmian:
1. **Dodanie rozwijanej listy (QComboBox)**:
   - Lista wyświetlająca wszystkie dostępne tabele w bazie danych.
   - Użytkownik wybiera tabelę do wyświetlenia.

2. **Przeładowanie tabeli po wyborze**:
   - Po zmianie tabeli w rozwijanej liście, dane z wybranej tabeli zostaną załadowane do widoku tabeli.

### Zaktualizowany kod:
Dodam funkcjonalność wyboru tabeli do obecnego programu.

Program został zmodyfikowany, aby umożliwić użytkownikowi wybór tabeli z bazy danych za pomocą listy rozwijanej (**QComboBox**). Teraz użytkownik może zmieniać widok tabeli, wybierając różne tabele w bazie danych. 

### Kluczowe zmiany:
1. **Dodano `QComboBox`** do wyświetlania listy tabel.
2. **Przeładowanie widoku tabeli po wyborze tabeli**: Obsłużono zmianę tabeli przez użytkownika.

Jeśli masz dodatkowe pytania lub potrzebujesz dalszych zmian, daj znać! 😊
