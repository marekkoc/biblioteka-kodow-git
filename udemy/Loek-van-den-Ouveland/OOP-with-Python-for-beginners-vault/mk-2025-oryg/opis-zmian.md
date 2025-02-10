# Opis zmian:
1. Wydrukowanie wszystkich pracowników wraz z ich zarobkami.

1. Zastosowano: Dwie niezależne listy pracowników i zarobkw. Wada: każda zmiana na jednej liście wymagała zmiany w drugiej. Zatem dodanie, usuniecie mogło powodować błędy. Był to tzw "fragile code". Jedna zmiana powodowała pospucie działania kodu w innych miejscach.
Dostaliśmy inforację o fukcji każdego pracownika na stacji w osobnym pliku. Aby wydrukować imię, zarobki i funkcję pracownika zstosowano blof if/else w który sprawdzano imie pracownika. W zależności od imienia wypisywano jego funkcję i zarobki.

1. Zastosowano: Klasa Employee zawierająca w sobie zarówno imię jak i zarobki.

1. Ddodano **funkcję pracownika** do klasy Employee. Dzięki czemu pozbyliśmy się bloku if/else. Zatem dodanie jednego atrybutu do klasy spowodowało usunięcie wielu lini kodu w których porównywano imie pracownika (duży blok if/else).

1. Zadanie: Chcemy **zmienić nazwy funkcji niektórych pracowników**. Zamiast "Attendant" wypisać "Station Attendant", a "Car Repair" zaminieć na "Mechanic". Te dwie nazwy pojawiają się w kodzie wielokrotnie (u 5 pracowników). Zatem dwie zmiany wymagają zmiany 5 linii kodu. Zatem w tym miejscu mamy **powtarzalność kodu (duplicate code)**.

1. Aby zapobiec powtarzalności kodu, zastosujemy **dziedziczenie**. Zatem każdy zawód będzie dziedziczył po klasie Employee i będzie automatycznie zawierał wtrybut klasy który określa jego funkcję. Wszycy pracownicy są typu Employee, ale niektorzy są typu StationAttendant lub Mechanic.  

1. Organizaowanie i zarządznie będzie łatwiejsze gdy przeniesiemy **informacje i cechy wspólne** dla danej funkcji pracowniak np. dla Mechanika do osobnej klasy. Wtedy oddzielimy **część wspólną** od **części specyficznej**. Przyniesie to nam sporo korzyści, jako że każda zmiana dotycząca klasy Machanika będzie robiona w jednym miejscu. Gdy w przyszłości zmienimy nazwę zawodu, to wystarczy zmienić tylko w jednym miejscu. Zastosujemy **dziedziczenie** (ang. inheritance) oznaczone **otwartą strzałką** w diagramie UML (ang. Unified Modeling Language).

1. **Dziedziczenie** oznacza, że klasa Mechanik zawiera w sobie wszystkie atrybuty i metody klasy Employee oraz **dodakowe atrybuty i metody specyficzne** dla Mechanika.

1. W dziedziczniu rzeczy które są **ogólne-wspólne** umieszczamy w klasie nadrzędnej (ang. superclass). Rzeczy **specyficzne-szczegółowe** umieszczamy w klasach podrzędnych (ang. subclass).

1. **Bezpośredio w klasach dziediczących** zdefioniowaliśmy **zmienną klasową** określającą nazwę zawodu pracownika. W tych klasach **nie zdefinowaliśmy metody konstruktora**. Zatem została użyta metoda konstruktora z klasy nadrzędnej.

1. **Zmienna klasowa (class variable)** jest zmienną, która jest wspólna dla wszystkich obiektów tej klasy. Jest to zmienna, która należy do klasy, a nie do pojedynczego obiektu. Wtedy za pomocą zmiany tej zmiennej w klasie np. Mechanika, zostają zmienione wszystkie zmienne klasowe dla wszystkich obiektów tej klasy. W diagramie UML zmienne klasowe oznaczamy przez **podkreślenie**.

1. Bez zdefinowania klasy dziedziczącej dla każedog zawodu, przy wypisywaniu infromacji o pracowniku, za każdym razem musieliśmy wpisaywać recznie nazwę zawodu, co powodowało **powtarzalność kodu (duplicate code)**.

### 14. Refactor

1. Na początku **bardzo ważne kilka zdań dotyczących refakatoringu**, poprawengo projektowania kodu, tego że gdy kod jest zły, to z czasem wiecej czasu poświecamy na szukaniu błędów niż na impolementowaniu nowych funkcji.

1. W tym miejscu robimy **refaktorowanie**. Nasz kod składa się z 3 bloków kodu:
    - definicji klas,
    - tworzenia blku z danymi (pracownikami),
    - wydrukowania danych (raportem).

1. Teraz main.py zależy (depends on) od employee.py. Zatem musimy zaimportować wszystkie klasy zdefioniowane w employee.py do main.py.

1. Wprowadzamy pojęcie **bazwej klasy abstrakcyjnej**. Jest to klasa, która nie ma implementacji. Jest to tylko definicja, która ma być implementowana w klasach podrzędnych.

### 15. Second report

1. Mamy podzielić bierżacy raport na dwie części:
    - raport z informacjami o pracownikach (Staffing report),
    - raport z informacjami o zarobkach (Accounting report).

1. Dodajemy nowego pracownika o imieniu Chuck. Prpblem w tym, że na liście już mamy pracownika o imieniu Chuck. Zatem musimy zacząć używać nazwisk. Ten Chucka nazywa sie Chuck Rainey. 

1. Musimy zmienić implementacje klasy Employee aby zawiarała także nazwisko.

### 16. Encapsulation

1. Cały czas mamy problem z powtarzającym się kodem w obu raportach, w linii z printem imienia i nazwiska pracownika. Gdy bedziemy chciali wydrukować imię i nazwisko w innej kolejności to musimy zmienić kod w obu raportach. Zatem musimy zmienić kod w dwóch miejscach. W takiej sytuacji zawsze istnieje ryzyko że popełnimy błąd i zmienimy kod w jednym miejscu, a nie w obu.

1. Innym problemem jest to, że "report" musi "rozumie" jak wewnetrznie są przechowywane dane pracownika takie jak imię i nazwisko. Zatem jest to problem **wjawnienia wiedzy o implementacji (implementation details)**. Rapot nie powinien wiedzieć jak są przechowywane dane pracownika.

1. Klasa Employee może nam udstępnić pełne imię i nazwisko pracownika. Zatem dodamy funkcję **get_full_name()** do klasy Employee. To rowziązuje nam oba problemy na raz. Teraz zmieniajac funkcje get_full_name() w klasie Employee nie musimy zmieniać kodu w obu raportach. 

1. To jest **encapsulation**. Jest to mechanizm, który pozwala nam ukryć implementację klasy. Zapewnia to, że wybrane atrybuty klasy nie powinny być dostępne z zewnątrz klasy.

### 17. Dependency injection

1. Czas abyt dokonaś spokojnej ewaluacji naszego kodu. Trzeba zastanowić się co do tej pory zrobiliśmy i co osiągnęliśmy.

1. Mam klssy związane z pracownikami w osobnych plikach. Jedank nadal w main.py tworzymy dwie funkcje które są odpowiedzialne za wydrukowanie raportów. **Funkcja main nie powinna tworzyć i drukować raportów**. Powinna tylko przyjmować funkcje drukujące raporty.

1. Przenieśmy funkcje drukujące raporty do osobnego modułu. Każdy z raportów bedzie osobnym obiektem. Zatem musimy stworzyć dwie klasy.

1. Jednak klasy raportów zależą od listy pracwników, która jest zdefiniowana w main.py. Gdy jedna część kodu zależy od drugiej, to mówimy, że istnieje **zależność (dependency)**.
Gdy część kodu nie może być odseparowana od drugiej cześci kodu, to mówimy że **kod jest powiązany (coupled)**. A to jest symptomem **rigid code**. Gdy mamy rygid code to nie możemy zmieniać jednej części kodu bez zmiany o drugiej części kodu.

1. Zatem mysimy przekazać liste pracowników do obiektów raportów. Jest to **dependency injection**. Dependency injection jest to mechanizm, który pozwala nam przekazać obiekt do obiektu drugiego i jest świetnym narzędziem które zapobiega powiązaniu kodu (coupling)

### 18. Polymorphism

1. Obie klasy raportów mają wspólną funkcję __init__(). Zatem jest to **powtarzalność kodu (duplicate code)**. Zatem jest to **wspólny kod który można wyciągnąć do wspólnej klasy**. W tym przpadku mamy klasy dziedziczące i potrzebujemy zaimplementować klasę nadrzędną. 

1. Chcemy mieć kilka raportów w liście i drukować wyniki za pomocę jednej pętli for.

1. Polimrfizm poznawal współdzielić wspólną nazwę metod w różnych klasach, ale te klasy mogą mieć różne implementacje i zachowywać się inaczej.

### 19. Schedule Report - Composition (ważne-dokonczyc opis)

1. Composition to mechanizm, który pozwala nam tworzyć złożone obiekty z prostych obiektów. Nie jest to dziedziczenie. Nie jest to też agregacja. Jest to **kompozycja**.

1. Chcemy dodać do raporty godziny pracy pracowników.


### 20. Composition - Schedule Report

1. Przy podawaniu godzin pracy wygenerowaliśmy znowu powtarzjący się kod **duplicate code**. Przez co jest badzo łatwo popełnić błąd podczaw wpisywania godzin pracy.

1. Do tej pory porblem z powtarzającym się kodem rozwiązywaliśmy poprzez dziediczenie. Teraz zastosujemy **kompozycję**.

1. **Kompozycja** to mechanizm, który pozwala nam tworzyć złożone obiekty z prostych obiektów. Nie jest to dziedziczenie. Nie jest to też agregacja. Jest to pewien sposob zbudowania obiektu z innych obiektów, associacji, zbudowania pewnych zależności.

1. **Kompozycja** pozwala zbudować zależność pomiędzy obiektem Employee a obiektem a obiektem Shift. Nie ma tu dziedziczenia.

1. Musimy stworzyć klasę Shift, która będzie zawierała informacje o godzinach pracy pracownika. Klasa Shift nie będzie miałą konstruktora, a godziny pracy będą stałe, zdefiowane jako zmienne klasowe.

1. Kompozycja w diagramie UML oznaczana jest jako **wypełniony rąb**.

1. W klasie Employee dodajemy atrybut **shift** typu **Shift**.