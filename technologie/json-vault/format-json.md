---
Utworzono: 2025-02-10T16:46:00
Zmodyfikowano: 2025-02-10T16:46:00
Źródło: "#Claude"
tags: 
Katalog:
---


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
