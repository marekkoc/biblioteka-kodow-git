---
Utworzono: 2025-01-09T21:00:00
Zmodyfikowano: 2025-01-09T21:00:00
Źródło: chatGPT
tags: 
Katalog:
---

FastAPI i REST API to dwa różne, ale powiązane ze sobą pojęcia. Oto ich różnice:

---

### 1. **REST API:**
   - **Definicja:** REST API (Representational State Transfer Application Programming Interface) to styl architektury dla tworzenia interfejsów API. Określa zasady i wzorce, które powinny być przestrzegane, aby stworzyć skalowalne i łatwe do zrozumienia API.
   - **Kluczowe cechy:**
     - Opiera się na protokole HTTP.
     - Wykorzystuje standardowe metody HTTP, takie jak `GET`, `POST`, `PUT`, `DELETE`.
     - Używa zasobów identyfikowanych przez unikalne URI (np. `/users`, `/products`).
     - Dane są zwykle przesyłane w formacie JSON lub XML.
   - **Przykład:**
     ```plaintext
     GET /users - Pobierz listę użytkowników.
     POST /users - Dodaj nowego użytkownika.
     ```

---

### 2. **FastAPI:**
   - **Definicja:** FastAPI to framework w Pythonie służący do budowy interfejsów API, szczególnie tych opartych na zasadach REST.
   - **Kluczowe cechy:**
     - **Szybkość:** Bardzo wydajny dzięki zastosowaniu ASGI i bibliotek takich jak `Starlette` i `Pydantic`.
     - **Łatwość użycia:** Automatyczne generowanie dokumentacji API (OpenAPI, Swagger UI).
     - **Walidacja danych:** Automatyczna walidacja danych wejściowych i wyjściowych dzięki `Pydantic`.
     - **Asynchroniczność:** Pełne wsparcie dla operacji asynchronicznych (`async`/`await`).
   - **Przykład:**
     ```python
     from fastapi import FastAPI

     app = FastAPI()

     @app.get("/users")
     async def read_users():
         return [{"name": "John"}, {"name": "Jane"}]
     ```

---

### **Podsumowanie różnic:**

| **Kryterium**        | **REST API**                            | **FastAPI**                             |
|-----------------------|-----------------------------------------|-----------------------------------------|
| **Czym jest**         | Styl architektury API.                 | Framework do budowy API.                |
| **Technologia**       | Nie jest przypisane do konkretnej technologii. | Framework w Pythonie oparty na REST.    |
| **Wydajność**         | Zależy od implementacji.               | Bardzo szybki dzięki asynchroniczności. |
| **Walidacja danych**  | Wymaga ręcznego kodowania walidacji.   | Automatyczna walidacja dzięki Pydantic. |
| **Dokumentacja API**  | Ręczna lub zewnętrzne narzędzia.       | Automatyczna (Swagger UI, OpenAPI).     |

---

### **W skrócie:**
- REST API to styl, zasada działania interfejsów API.
- FastAPI to narzędzie (framework) do tworzenia API, które często implementuje zasady REST.