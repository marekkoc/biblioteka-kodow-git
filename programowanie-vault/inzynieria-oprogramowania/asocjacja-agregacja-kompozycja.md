---
Utworzono: 2024-11-16T17:17:00
Zmodyfikowano: 2024-11-16T17:17:00
Źródło: chatGPT
tags:
---

**Agregacja**, **asocjacja** i **kompozycja** to terminy z zakresu modelowania obiektowego, które opisują relacje między obiektami w programowaniu obiektowym. Wszystkie trzy odnoszą się do sposobów, w jakie obiekty mogą być ze sobą powiązane, ale różnią się pod względem stopnia "związania" między nimi. Poniżej wyjaśnię, czym się różnią.

---

### 1. **Asocjacja (Association)**

Asocjacja to **najbardziej ogólna relacja między obiektami**, która oznacza, że jeden obiekt może znać lub używać innego obiektu. W asocjacji obiekty mogą współpracować, ale żaden z nich nie jest właścicielem drugiego.

- **Przykład**: Obiekt klasy `Student` może być w relacji asocjacji z obiektem klasy `Course`. Student może uczestniczyć w różnych kursach, a kurs może mieć różnych studentów.
- **Słaba zależność**: Obiekty są powiązane, ale mogą istnieć niezależnie od siebie.

---

### 2. **Agregacja (Aggregation)**

Agregacja to **specjalny rodzaj asocjacji**, w którym jeden obiekt jest częścią drugiego, ale może istnieć niezależnie od niego. Agregacja opisuje relację "część-całość" lub "jest częścią", ale nie oznacza silnej zależności.

- **Przykład**: Obiekt klasy `Department` (wydział) może agregować obiekty klasy `Professor` (profesor). Profesor może należeć do wydziału, ale nadal może istnieć jako niezależny obiekt.
- **Relacja całość-część**: Obiekt całości (np. wydział) zawiera części (profesorów), ale części mogą istnieć niezależnie.
- **Graficzne oznaczenie w UML**: Zwykle przedstawiana jako linia z pustym rombem po stronie obiektu całości (np. `Department` →◦ `Professor`).

---

### 3. **Kompozycja (Composition)**

Kompozycja to **silniejsza forma agregacji** i wskazuje na jeszcze silniejszą zależność "część-całość". W kompozycji części są **ściśle powiązane z całością** i nie mogą istnieć samodzielnie – ich istnienie jest całkowicie zależne od obiektu całości.

- **Przykład**: Obiekt klasy `House` (dom) może składać się z obiektów klasy `Room` (pokój). Pokój nie może istnieć bez domu, a kiedy dom przestaje istnieć, pokój także zostaje usunięty.
- **Relacja całość-część (ścisła zależność)**: Jeśli obiekt całości (np. dom) zostaje usunięty, to również wszystkie jego części (pokoje) zostają zniszczone.
- **Graficzne oznaczenie w UML**: Linia z wypełnionym rombem po stronie obiektu całości (np. `House` →◆ `Room`).

---

### Podsumowanie różnic

| Rodzaj relacji | Znaczenie | Istnienie obiektu części | Przykład |
|----------------|-----------|--------------------------|----------|
| **Asocjacja**  | Obiekty są powiązane, mogą współpracować | Niezależne od siebie | `Student` ↔ `Course` |
| **Agregacja**  | Całość posiada części, ale części mogą istnieć samodzielnie | Może istnieć niezależnie | `Department` ◦→ `Professor` |
| **Kompozycja** | Całość składa się z części, które nie mogą istnieć samodzielnie | Uzależnione od całości | `House` ◆→ `Room` |

Asocjacja jest więc najluźniejszą formą powiązania, agregacja jest bardziej zależna, a kompozycja stanowi najściślejszy związek między obiektami.