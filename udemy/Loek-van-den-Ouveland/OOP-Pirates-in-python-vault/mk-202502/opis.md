Created: 2025.02.14 <br>
Modified: 2025.02.14

# Sekcja 2: Introudction
## 2. Introduction
## 3. First version

1. Wartość udziału powinna być przydzielana według wagi ważności kazdego pirata (pirate rank)

## 4. Tuples
1. Problem: Piraci i ich waga (ranks) nie są na stałe połączeni w systemie, to powoduje fragile code... Jedna zmiana może spowodować błędne działanie kodu w innym miejscu.
2. Tak naprawdę każdy pirat jest kombinacją "Imienia oraz jego wagi (rank)"
3. Tworzymy liste piratów w której każdy element jest krotką (Imie, rank)

## 5. Pirate union

# Sekcja 3: Classes and objects
## 6. Classes and objects
1. Classess group data that belongs together

## 7. UML

# Sekcja 4: Inheritance
## 8. Inheritance
## 9. Refactoring
1. Przeniesienie danych (listy piratów) do osobnej klasy, a zarazem do osobnego modułu.


# Sekcja 5: Polymorphysm
## 10. Extra Officer and Cannon Operator
1. Łatwo dodać nowych piratów, i łatwo zmienić wartość łupu.
2. Problem: Zmian trzeba cały czas dokonywać manualnie. Chcemy to zautomatyzować. Chcemy automatycznie wczytać listę piratów jaką dostniemy od kapitana.

## 11. Importing JSON
1. Wczytujemy listę piratów z pliku. Musimy zaprojektować format pliku który będzie nam przetwarzał dane piratów.
2. Nie zmieniamy klasy **DataLoader** ponieważ to byłaby duża zmiana, a do tego chcemy aby kod był funkcjonalny podczas naszych zmian. Dlatego tworzymy nową klasę **JSONDataLoader**. To również zadziała, gdy dane pobierzemy z kompletnie innego źródła, np z bazy danych.
3. Wazny wytłumacznie **Polimorfizmu** oraz zasady **OPEN-CLOSE** --->>> Open for extention and close for modification.

## 12. Add Cook and Deck Scrubber
1. Dodjemy dwie klasy, ale kodu musimy zmieniac w wielu miejscach.
	1. dodac implementacje klas
	2. zmienic dane w pliku JSON
	3. zmienic JSONDataLoader
	3. zaktualizowac importy
4. Takie zmiany są spowodowane poprzez **złamanie zasady OPEN-CLOSE** Problemem jest to że cały czas mamy **switch** zależny od typu klasy (zawodu) pirata podczas wczytywania danych w JSONDataLoader.
5. Problemem jest to, że liczba zawodów (klas potomnych) nie jest stała.  Możemy dodawać nowe klasy zawodów w nieskończoność. Zatem cały czas będziemy musieli aktualizowć **switch** wczytujący oraz inne miejsca (kilka) w kodzie. To jest właśnie **ograniczenie dziedziczenia**.
6. Kod nie jest wystarczająco  **elastyczny** dlatego wrpowadziy nowe pojęcie: **KOMPOZYCJE**.

# Sekcja 6. Kompozycja

## 13. Kompozycja ponad dziedziczenie
1. Nadal chcemy aby rola pirata i jego rank byly razem powioazne, ale jest za duzo mozliwosci dziedziczenia i za duzo zmian
2. Dlatego wprowadzamy nowa klase **Role** ktora łączy role pirata razem z jego rankiem i da nam dużą elastyczność.
3. Teraz gdy pojawi sie nowy pirat to dodajemy go **TYLKO** w pliku JSON!!!

## 14. Test with TestDataLoader


# Sekcja 7. Payroll

## 15. Payroll

1. Diagram zależności (dependency diagram) pokazuje logiczny podzial funkcjonalności systemu. main -> data -> piraci
2. **Czystość i przejrzystość** kodu daje nam założenie przestrzeganie **pojedyńczej odpowiedzialności (single responsibility)** 
3. Moduły i klasy powinny mieć jasno zdefionowane swoje **zadanie (single responsibility**:
	-  main:
		1. kotroluje wykonywanie zadań w aplikacji (the flow in the app)
		2. tworzy drzwo obiektów używanych w aplikacji (object tree)
		3. wywołuje kolejne funkcje i działania aplikacji(triggers functionality)
		4. wyświetla wyniki (outputs the results)
5.  Nietety obecnie main.py oblicza również udziały pieniężne poszczególnych piratów (pirate shares)
6.  Zrefaktoryzowanie tego nie jest łatwym zadaniem, bo kod który oblicza udziały piratów i który wyświetla wyniki jest ściśle ze sobą powiązany (tight togeter).
7.  Powinniśmy oddzielić tę funkcjonalność: moduł do obliczania udziałów powinien być odpowiedzialny tylko za obliczenia, a moduł odpowiedzialny za drukowanie raportu, powinien być odpowiedzialny tylko za drukowanie raportu.
8.  Ogólna zasada: <br><br>
  **NIGDY NIE ZAMIESZCZAJ FUNKCJI print()  WEWNĄTRZ KALAS ANI WEWNĄTRZ FUNKCJI!!!** <br><br> **KLASY I FUNKCJE WYKONUJA OBLICZENIA I ZWARACAJA WYNIK (TYLKO WYNIK)!!! NIC NIE DRUKUJĄ**<br><br>
9.  Zatem tworzymy klase **Payroll** która oblicza udziały piratów, oraz metodę która to wyliczy 
10.  Potrzebujemy też klasę, która obliczy kombinację Pirata i jego udziałów: **Share**
11.  Teraz main jest opowiedzialny za:
	1.  importowanie i inicjalizowanie klas
	2.  użycie klas
	3.  wykruk wyników w terminalu
	4.  NIE MA: wczytywania danych ani żadnych obliczeń w funkcji/pliku main.
5.  Wszystkie tutaj dokonane zmiany były w plikach **main** i **payrol**, pliki data i prates zostały nieznienione -> zadziałała zasada single responsibility.
6.  Wprowadzenie pojecia **Agregacji**

## 16. Missions
1. Zwiększa się lista piratów, nie wszyscy uczestniczą w każdej misji. Dltatego chcemy zrobić podział.
2. System potrzebuje **misji (Missjons)**, które określą zarówno nazwe misji, łup oraz lisę piratów.
3. Zacznijmy to porojektować od danych testowych.
4. Tworzymy moduł i klasę związaną z miją.
5. W TestDataLoader tworzymy metode która zwaraca misję testową.
6. Pomimo, że main ma sporo kodu, to nie ma tam zawartej żadnej logiki. Jest tam tylko iterowanie po misjach i wydruk wyników.

## 17. Missions JSON
1. Mamy dane misji w pliku JSON
2. Aktualizujemy klasę JSONDataLoader
3. Teraz możemy zaktualizować diagram zależności kodu (Dependency Diagram), w tym celu podążamy za importami w kodzie

# Sekcja 8: Bank Exhange

## 18. Exhange Loot.
1. 
