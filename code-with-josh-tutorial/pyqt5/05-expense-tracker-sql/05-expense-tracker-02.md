### Refaktoryzacja kodu

Poniżej przedstawiam zrefaktoryzowany kod oraz opis dokonanych zmian.

#### Zmiany wprowadzone:
1. **Usunięcie zbędnych importów**:
   - Usunięto `from email.charset import QP`, ponieważ nie był używany.
   - Pozostawiono tylko te importy, które są faktycznie potrzebne.

2. **Zastąpienie magicznych wartości stałymi**:
   - Dodano stałe dla stylów oraz niektórych wartości (np. nagłówki tabeli), aby poprawić czytelność i łatwiej wprowadzać zmiany.

3. **Refaktoryzacja stylów**:
   - Styl CSS przeniesiono do oddzielnej metody, aby ułatwić modyfikacje i zwiększyć czytelność.

4. **Podział kodu na mniejsze metody**:
   - Wyodrębniono konfigurację widżetów i układów do osobnych metod.
   - Ułatwia to debugowanie i czytanie kodu.

5. **Dodanie komentarzy i logiki debugowania**:
   - Rozszerzono logikę debugowania przy korzystaniu z bazy danych.

6. **Obsługa błędów**:
   - Dodano obsługę błędów dla metod SQL, by uniknąć potencjalnych problemów podczas pracy z bazą.

7. **Poprawki w formatowaniu i nazewnictwie**:
   - Zmieniono nazwy zmiennych na bardziej czytelne i zgodne z PEP8.
   - Uporządkowano wcięcia i podzielono kod na logiczne sekcje.

8. **Usprawnienie metody `load_table`**:
   - Dodano logikę obsługi pustych wyników z bazy danych.

Poniżej zrefaktoryzowany kod:

Kod został zrefaktoryzowany, aby był bardziej czytelny, modularny i zgodny z dobrymi praktykami programistycznymi. Jeśli masz pytania lub potrzebujesz dalszych modyfikacji, daj znać! 😊