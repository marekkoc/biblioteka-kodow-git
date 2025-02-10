#!/usr/bin/env conda run -n py38 python
#%%
import json
#%%
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

# Dodawanie nowego produktu do listy
wczytane_produkty['produkty_spozywcze'].append(nowy_produkt)

# Zapisywanie zaktualizowanych danych do pliku
with open('produkty.json', 'w', encoding='utf-8') as f:
    json.dump(wczytane_produkty, f, ensure_ascii=False, indent=4)


print("Dane zapisane do pliku produkty.json")


# Przykład 4: Wyszukiwanie produktów
def znajdz_produkt(nazwa):
    for produkt in wczytane_produkty['produkty_spozywcze']:
        if produkt['nazwa'].lower() == nazwa.lower():
            return produkt
    return None
    
    # Przykład 5: Aktualizacja ceny produktu
def aktualizuj_cene(nazwa, nowa_cena):
    produkt = znajdz_produkt(nazwa)
    if produkt:
        produkt['cena'] = nowa_cena
        return True
    return False    

# Przykład 6: Usuwanie produktu
def usun_produkt(nazwa):
    produkt = znajdz_produkt(nazwa)
    if produkt:
        wczytane_produkty['produkty_spozywcze'].remove(produkt)
        with open('produkty.json', 'w', encoding='utf-8') as f:
            json.dump(wczytane_produkty, f, ensure_ascii=False, indent=4)
        return True
    return False

# Przykład 7: Wyświetlanie wszystkich produktów
def wyswietl_wszystkie_produkty():
    for produkt in wczytane_produkty['produkty_spozywcze']:
        print(f"Nazwa: {produkt['nazwa']}, Cena: {produkt['cena']} zł")

# Przykład 8: Wyświetlanie produktów w kategorii    
def wyswietl_produkty_w_kategorii(kategoria):
    for produkt in wczytane_produkty['produkty_spozywcze']:
        if produkt['kategoria'].lower() == kategoria.lower():
            print(f"Nazwa: {produkt['nazwa']}, Cena: {produkt['cena']} zł")

# %%
wyswietl_produkty_w_kategorii("Owoce")



# %%
