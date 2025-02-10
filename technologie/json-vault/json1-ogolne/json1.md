Przedstawię Ci kilka praktycznych przykładów obsługi plików JSON w Pythonie, wykorzystując dane o produktach żywnościowych.

```python
import json

# Przykład 1: Tworzenie i zapisywanie danych do pliku JSON
produkty = {
    "produkty_spozywcze": [
        {
            "nazwa": "Jabłko",
            "kategoria": "Owoce",
            "cena": 2.50,
            "jednostka": "kg",
            "wartosci_odzywcze": {
                "kalorie": 52,
                "bialko": 0.3,
                "weglowodany": 14,
                "tluszcze": 0.2
            }
        },
        {
            "nazwa": "Chleb pszenny",
            "kategoria": "Pieczywo",
            "cena": 4.99,
            "jednostka": "szt",
            "wartosci_odzywcze": {
                "kalorie": 265,
                "bialko": 8.5,
                "weglowodany": 49,
                "tluszcze": 3.2
            }
        }
    ]
}

# Zapisywanie do pliku
with open('produkty.json', 'w', encoding='utf-8') as f:
    json.dump(produkty, f, ensure_ascii=False, indent=4)

# Przykład 2: Odczytywanie danych z pliku JSON
with open('produkty.json', 'r', encoding='utf-8') as f:
    wczytane_produkty = json.load(f)

# Przykład 3: Dodawanie nowego produktu
nowy_produkt = {
    "nazwa": "Mleko",
    "kategoria": "Nabiał",
    "cena": 3.99,
    "jednostka": "l",
    "wartosci_odzywcze": {
        "kalorie": 42,
        "bialko": 3.4,
        "weglowodany": 4.8,
        "tluszcze": 2.0
    }
}

wczytane_produkty["produkty_spozywcze"].append(nowy_produkt)

# Przykład 4: Wyszukiwanie produktów
def znajdz_produkt(nazwa):
    for produkt in wczytane_produkty["produkty_spozywcze"]:
        if produkt["nazwa"].lower() == nazwa.lower():
            return produkt
    return None

# Przykład 5: Aktualizacja ceny produktu
def aktualizuj_cene(nazwa, nowa_cena):
    produkt = znajdz_produkt(nazwa)
    if produkt:
        produkt["cena"] = nowa_cena
        return True
    return False

# Przykład użycia funkcji
znalezione = znajdz_produkt("Jabłko")
if znalezione:
    print(f"Znaleziony produkt: {znalezione['nazwa']}, cena: {znalezione['cena']} zł/{znalezione['jednostka']}")

# Aktualizacja ceny
if aktualizuj_cene("Chleb pszenny", 5.49):
    print("Zaktualizowano cenę chleba")
```

Ten kod pokazuje podstawowe operacje na plikach JSON:
- Tworzenie struktury danych i zapisywanie do pliku JSON
- Odczytywanie danych z pliku JSON
- Dodawanie nowych elementów
- Wyszukiwanie produktów
- Aktualizację danych

Warto zwrócić uwagę na:
- Używanie `encoding='utf-8'` przy operacjach na pliku dla poprawnej obsługi polskich znaków
- Parametr `ensure_ascii=False` przy zapisie, który pozwala na zapisywanie znaków Unicode
- Parametr `indent=4` dla czytelnego formatowania pliku JSON
- Zagnieżdżoną strukturę danych z informacjami o wartościach odżywczych

Możesz dostosować ten kod do swoich potrzeb, dodając więcej produktów lub rozszerzając strukturę danych o dodatkowe informacje, jak np. data ważności, producent, czy kod kreskowy.

# json2

### Opis na podstawie katalogu:
 /Loek-van-den-Ouveland/OOP-with-Python-for-beginners-vault/mk-202502-json


Świetne pytanie! Wyjaśnię strukturę JSON na przykładach:

1. **Podstawowa składnia JSON**:
```json
{
    "imie": "Jan",
    "wiek": 30,
    "aktywny": true,
    "wzrost": 1.85
}
```
- Każdy wpis składa się z pary `"klucz": wartość`
- Klucze zawsze muszą być stringami (w cudzysłowach)
- Wpisy są oddzielone przecinkami
- Całość jest otoczona nawiasami klamrowymi `{}`

2. **Typy danych w JSON**:
```json
{
    "string": "tekst",
    "number": 42,
    "float": 3.14,
    "boolean": true,
    "null": null,
    "array": [1, 2, 3],
    "object": {
        "key": "value"
    }
}
```

1. **Zagnieżdżone struktury**:
```json
{
    "pracownik": {
        "dane_osobowe": {
            "imie": "Anna",
            "nazwisko": "Kowalska"
        },
        "umiejetnosci": ["Python", "Java", "SQL"],
        "projekty": [
            {
                "nazwa": "Projekt A",
                "rola": "Developer"
            },
            {
                "nazwa": "Projekt B",
                "rola": "Team Lead"
            }
        ]
    }
}
```

2. **Tablice (Arrays)**:
```json
{
    "liczby": [1, 2, 3, 4, 5],
    "imiona": ["Jan", "Anna", "Piotr"],
    "mieszane": [1, "dwa", true, null],
    "obiekty": [
        {"id": 1, "nazwa": "A"},
        {"id": 2, "nazwa": "B"}
    ]
}
```

3. **Konwencje nazewnictwa plików**:
- Pliki JSON mają rozszerzenie `.json`
- Popularne nazwy to:
  - `config.json` (dla konfiguracji)
  - `data.json` (dla danych)
  - `package.json` (w projektach Node.js)
  - `manifest.json` (dla metadanych)
  - `settings.json` (dla ustawień)

4. **Formatowanie**:
```json
{
    "bez_wcięć": "wszystko może być w jednej linii",
    "z_wcięciami": {
        "jest": "bardziej czytelne",
        "gdy": "używamy wcięć"
    }
}
```

5. **Ważne zasady**:
- JSON nie obsługuje komentarzy
- Ostatni element nie może mieć przecinka na końcu
- Stringi muszą być w podwójnych cudzysłowach `""`
- Nazwy kluczy muszą być stringami
- Wartości mogą być tylko: string, number, object, array, boolean lub null

6. **Przykład praktyczny**:
```json
{
    "firma": {
        "nazwa": "Tech Corp",
        "rok_zalozenia": 2020,
        "pracownicy": [
            {
                "id": 1,
                "imie": "Jan",
                "aktywny": true,
                "wynagrodzenie": 5000.50,
                "umiejetnosci": ["Python", "SQL"]
            },
            {
                "id": 2,
                "imie": "Anna",
                "aktywny": false,
                "wynagrodzenie": null,
                "umiejetnosci": []
            }
        ]
    }
}
```

JSON jest bardzo popularnym formatem ze względu na:
- Prostą składnię
- Czytelność dla człowieka
- Łatwość przetwarzania przez programy
- Wsparcie w większości języków programowania
- Powszechne użycie w API i konfiguracji
