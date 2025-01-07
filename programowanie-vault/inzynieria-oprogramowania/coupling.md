---
Utworzono: 2024-11-11T07:06:00
Zmodyfikowano: 2024-11-11T07:06:00
Źródło: chatGPT
tags:
  - "#Coupling"
---

Coupling, czyli **sprzężenie** (często stosowane bez tłumaczenia jako "coupling") w kontekście programowania i inżynierii oprogramowania, odnosi się do stopnia powiązania lub zależności między różnymi modułami lub klasami w systemie. Oznacza, jak bardzo jedna część kodu jest powiązana z innymi i jak mocno na siebie wzajemnie oddziałują. To istotne pojęcie przy projektowaniu oprogramowania, ponieważ poziom coupling wpływa na łatwość utrzymania, testowania i skalowalności kodu.

### Typy Coupling
Coupling można podzielić na różne poziomy, od słabego do mocnego (ang. "loose" do "tight coupling"), gdzie:

- **Loose Coupling (słabe sprzężenie)**: Moduły są zaprojektowane tak, aby były jak najbardziej niezależne od siebie. Zmiana w jednym module nie wpływa lub ma niewielki wpływ na inne moduły. Słabe sprzężenie jest preferowane, ponieważ pozwala na łatwiejsze modyfikowanie, testowanie i ponowne użycie kodu.

- **Tight Coupling (mocne sprzężenie)**: Moduły są ze sobą mocno powiązane, co oznacza, że zmiana w jednym module często wymaga zmian w innych. Takie powiązanie może ograniczać elastyczność i sprawiać, że modyfikacje i testowanie kodu są bardziej złożone i ryzykowne.

### Przykłady Coupling w praktyce

1. **Kod zależny od szczegółów implementacji** — jeżeli klasa `A` bezpośrednio korzysta z metod klasy `B`, wtedy każda zmiana w `B` może wymagać zmian w `A`.
  
2. **Połączenie przez interfejs** — jeżeli klasa `A` korzysta z klasy `B` poprzez interfejs lub abstrakcję (np. zdefiniowanej przez `interface` w językach takich jak Java czy C#), wtedy `A` nie musi znać szczegółów `B`, co zmniejsza coupling.

3. **Wstrzykiwanie zależności (Dependency Injection)** — gdy obiekty są dostarczane przez zewnętrzne mechanizmy zamiast być bezpośrednio tworzone w kodzie, sprzężenie między nimi jest słabsze, co poprawia elastyczność systemu.

### Dlaczego coupling jest ważny?

Kontrolowanie poziomu coupling jest kluczowe dla dobrego projektowania oprogramowania. Zbyt mocne sprzężenie może prowadzić do kodu trudnego do utrzymania i testowania, a także podatnego na błędy podczas modyfikacji. Luźne sprzężenie, natomiast, sprzyja tworzeniu modułowego, skalowalnego kodu, który łatwiej się rozwija i dostosowuje do zmian.

### Coupling a Cohesion
Coupling często omawia się razem z **cohesion** (kohezją), która odnosi się do stopnia spójności funkcji wewnątrz pojedynczego modułu. Dobre projektowanie kodu dąży do niskiego coupling i wysokiej cohesion — czyli słabego powiązania między modułami oraz wysokiej spójności wewnątrz każdego z modułów.


# Przykłady

Oczywiście! Przejdźmy przez przykłady różnych poziomów *coupling* (sprzężenia) w kodzie Pythona. Będzie to obejmować zarówno **mocne (tight coupling)**, jak i **słabe sprzężenie (loose coupling)**, co pomoże zrozumieć, jak zaprojektować elastyczniejszy kod.

### Przykład 1: Mocne sprzężenie (Tight Coupling)

W przypadku mocnego sprzężenia, jedna klasa lub funkcja silnie zależy od konkretnej implementacji innej klasy. Zmiana tej klasy często wymaga zmiany kodu zależnego.

```python
class Database:
    def connect(self):
        # Implementacja połączenia z bazą danych
        print("Connecting to the database...")

    def fetch_data(self):
        # Symulacja pobierania danych z bazy
        return {"data": "example data"}

class ReportGenerator:
    def __init__(self):
        self.database = Database()  # Mocne powiązanie (tight coupling)

    def generate_report(self):
        self.database.connect()
        data = self.database.fetch_data()
        print("Generated report with data:", data)
```

Tutaj klasa `ReportGenerator` jest mocno powiązana z klasą `Database`, ponieważ tworzy jej instancję wewnątrz własnego konstruktora. W efekcie każda zmiana w implementacji `Database` może wymagać modyfikacji w `ReportGenerator`. Dodatkowo, jeśli będziemy chcieli zmienić źródło danych (np. z `Database` na `API`), będzie to trudne do wykonania.

---

### Przykład 2: Słabe sprzężenie (Loose Coupling) z Dependency Injection

Przykład poniżej pokazuje słabsze sprzężenie, w którym stosujemy wzorzec *dependency injection*. Klasa `ReportGenerator` jest zaprojektowana tak, aby nie była zależna od konkretnej klasy bazy danych — możemy dostarczyć dowolny obiekt, który posiada metodę `connect` i `fetch_data`.

```python
class Database:
    def connect(self):
        print("Connecting to the database...")

    def fetch_data(self):
        return {"data": "example data"}

class APIService:
    def connect(self):
        print("Connecting to the API...")

    def fetch_data(self):
        return {"data": "example API data"}

class ReportGenerator:
    def __init__(self, data_source):  # data_source jest wstrzykiwany (injected)
        self.data_source = data_source

    def generate_report(self):
        self.data_source.connect()
        data = self.data_source.fetch_data()
        print("Generated report with data:", data)

# Przykład użycia
db = Database()
report_with_db = ReportGenerator(db)
report_with_db.generate_report()

api = APIService()
report_with_api = ReportGenerator(api)
report_with_api.generate_report()
```

Tutaj `ReportGenerator` jest teraz niezależny od implementacji `Database`. Zamiast tego przyjmuje `data_source`, który musi implementować metody `connect` i `fetch_data`. Dzięki temu możemy użyć zarówno `Database`, jak i `APIService`, a nawet łatwo dodać inne źródła danych w przyszłości, nie modyfikując kodu `ReportGenerator`.

---

### Przykład 3: Poluzowane sprzężenie z interfejsami (Protokołami)

Python pozwala na stosowanie protokołów (od wersji 3.8, wprowadzonych w module `typing`), które mogą wspierać słabe sprzężenie poprzez definiowanie kontraktu metodowego, który klasy muszą implementować. Dzięki temu `ReportGenerator` zależy tylko od struktury (interfejsu), a nie od konkretnej implementacji.

```python
from typing import Protocol

class DataSource(Protocol):
    def connect(self) -> None:
        pass

    def fetch_data(self) -> dict:
        pass

class Database(DataSource):
    def connect(self):
        print("Connecting to the database...")

    def fetch_data(self):
        return {"data": "example data"}

class APIService(DataSource):
    def connect(self):
        print("Connecting to the API...")

    def fetch_data(self):
        return {"data": "example API data"}

class ReportGenerator:
    def __init__(self, data_source: DataSource):  # Typowanie interfejsu
        self.data_source = data_source

    def generate_report(self):
        self.data_source.connect()
        data = self.data_source.fetch_data()
        print("Generated report with data:", data)

# Przykład użycia z różnymi źródłami
report_with_db = ReportGenerator(Database())
report_with_db.generate_report()

report_with_api = ReportGenerator(APIService())
report_with_api.generate_report()
```

W tym przykładzie `DataSource` jest protokołem (czyli interfejsem), który wymaga, by każda klasa implementująca go posiadała metody `connect` i `fetch_data`. Dzięki temu `ReportGenerator` może pracować z dowolną klasą, która spełnia te wymagania, bez bezpośredniego wiązania z konkretną implementacją. Jest to rozwiązanie z jeszcze słabszym sprzężeniem niż w poprzednim przykładzie.

---

### Podsumowanie
* **Mocne sprzężenie** (tight coupling) występuje, gdy klasy są bezpośrednio powiązane, np. poprzez tworzenie obiektu innej klasy wewnątrz konstruktora.
* **Słabe sprzężenie** (loose coupling) można osiągnąć, stosując *dependency injection* lub wzorce projektowe, takie jak protokoły (interfejsy), które definiują wymagane metody.

Luźne sprzężenie ułatwia testowanie i modyfikację kodu, podczas gdy mocne sprzężenie może prowadzić do trudności w utrzymaniu, zwłaszcza w dużych projektach.