---
Utworzono: 2024-10-28T10:25:00
Zmodyfikowano: 2024-10-28T10:25:00
Źródło: chatGPT
tags:
  - "#Pep8"
---

W Pythonie nazewnictwo zmiennych i innych elementów kodu jest określone przez[ **PEP 8**](https://peps.python.org/pep-0008/) — dokument z wytycznymi dotyczącymi stylu kodu, zatytułowany "Style Guide for Python Code". To jest oficjalny dokument, który opisuje konwencje i dobre praktyki programistyczne dla języka Python.

Oto główne zasady nazewnictwa według PEP 8:

1. **Nazwy zmiennych i funkcji**:
   - Używaj małych liter z podkreśleniami dla czytelności: `my_variable`, `calculate_sum()`.
   
2. **Nazwy klas**:
   - Stosuj format "CamelCase" (bez podkreśleń): `MyClass`, `EmployeeDetails`.
   
3. **Nazwy stałych**:
   - Pisane wielkimi literami, oddzielone podkreśleniami: `MAX_SPEED`, `DEFAULT_TIMEOUT`.
   
4. **Nazwy modułów i pakietów**:
   - Małe litery, ewentualnie z podkreśleniami: `my_module`, `data_processing`.

### Główne wskazówki z PEP 8:

- Unikaj skrótów i nazw jednowyrazowych, chyba że są one oczywiste, np. `i` w pętlach.
- Używaj prefiksu `_` dla nazw prywatnych lub wewnętrznych (np. `_my_internal_variable`).
- Dla zmiennych, które nie powinny być nadpisywane, stosuj podwójne podkreślenia przed nazwą klasy (np. `__my_var`), aby zmniejszyć ryzyko przypadkowego nadpisania.