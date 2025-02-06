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