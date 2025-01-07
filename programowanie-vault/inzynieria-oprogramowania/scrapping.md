---
Utworzono: 2024-12-28T06:40:00
Zmodyfikowano: 2024-12-28T06:40:00
Źródło: chatGPT
tags:
  - "#scrapping"
Katalog: /biblioteka-repozytoriow-git/biblioteka-kodow-git/mk/rozne
---
### Dodatkowe źródła
1. Python & PowerShell for Absolute Beginners - [Scrape Text from PDF and DOCX](https://www.youtube.com/watch?v=XekG31KigPw) - całkiem fajny tutorial
2. 
   
   
### **Co oznacza słowo "scraping" w programowaniu?**

**Scraping** (pełna nazwa: **web scraping**) w programowaniu odnosi się do procesu automatycznego pobierania danych z witryn internetowych. Jest to technika, dzięki której program lub skrypt odczytuje i wyodrębnia zawartość stron internetowych (np. tekst, obrazy, tabele), przekształcając ją na dane, które mogą być przechowywane lub przetwarzane w innych aplikacjach.

---

### **Kontekst użycia scraping**

Scraping najczęściej dotyczy pobierania danych z sieci, ale może być również używany w innych kontekstach, takich jak:

1. **Web scraping**:
    
    - Automatyczne zbieranie informacji z witryn internetowych.
    - Narzędzia do scrapingu "czytają" kod HTML strony, szukają określonych elementów (np. tagów `div`, `table`, `img`), a następnie zapisują znalezione dane w formatach takich jak CSV, JSON lub bazy danych.
2. **Data scraping**:
    
    - Ogólniejszy termin oznaczający wyodrębnianie danych z dowolnego źródła, np. plików PDF, API lub dokumentów tekstowych.
3. **Screen scraping**:
    
    - Pobieranie danych z interfejsów użytkownika (np. ekranów terminalowych lub aplikacji), w sytuacjach, gdy nie ma dostępu do danych w formacie maszynowym.

---

### **W jakich sytuacjach używa się scrapingu?**

#### **1. Automatyzacja zbierania danych**

- Pobieranie danych z katalogów produktów (np. ceny, recenzje, specyfikacje techniczne).
- Zbieranie danych o pogodzie, giełdowych, czy wyników sportowych.

#### **2. Analiza danych**

- Pobieranie opinii użytkowników z forów, blogów lub platform społecznościowych (np. Twitter, Reddit).
- Monitorowanie konkurencji (np. zmiany cen w sklepach internetowych).

#### **3. Budowanie aplikacji**

- Tworzenie własnych wyszukiwarek na podstawie danych zebranych z wielu źródeł.
- Generowanie agregatorów treści (np. z wiadomościami, blogami, przepisami).

#### **4. Edukacja i prototypowanie**

- Nauka przetwarzania danych lub prototypowanie systemów, które korzystają z realnych danych.

---

### **Przykład działania web scrapingu**

#### **Przykładowa strona HTML:**

```html
<html>
  <body>
    <h1>Produkty</h1>
    <div class="product">
      <h2>Produkt 1</h2>
      <p>Cena: 100 PLN</p>
    </div>
    <div class="product">
      <h2>Produkt 2</h2>
      <p>Cena: 200 PLN</p>
    </div>
  </body>
</html>
```

#### **Kod w Pythonie (z użyciem BeautifulSoup):**

```python
from bs4 import BeautifulSoup

html = """
<html>
  <body>
    <h1>Produkty</h1>
    <div class="product">
      <h2>Produkt 1</h2>
      <p>Cena: 100 PLN</p>
    </div>
    <div class="product">
      <h2>Produkt 2</h2>
      <p>Cena: 200 PLN</p>
    </div>
  </body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")
products = soup.find_all("div", class_="product")

for product in products:
    name = product.find("h2").text
    price = product.find("p").text
    print(f"{name} - {price}")
```

**Wynik:**

```
Produkt 1 - Cena: 100 PLN
Produkt 2 - Cena: 200 PLN
```

---

### **Narzędzia używane do scrapingu**

1. **Biblioteki w Pythonie**:
    
    - **BeautifulSoup**: Parsowanie i przetwarzanie HTML i XML.
    - **Scrapy**: Framework do scrapingu, oferujący większe możliwości (np. zarządzanie sesjami).
    - **Selenium**: Automatyzacja przeglądarek, przydatna w przypadku dynamicznych stron.
2. **API i narzędzia zewnętrzne**:
    
    - Puppeteer (JavaScript).
    - Playwright (obsługa dynamicznych stron).
    - Narzędzia takie jak Octoparse czy ParseHub.

---

### **Prawne i etyczne aspekty scrapingu**

1. **Legalność**:
    
    - Wiele witryn posiada regulaminy zabraniające scrapingu.
    - Jeśli witryna udostępnia API, preferowane jest korzystanie z niego.
2. **Etyka**:
    
    - Nie obciążaj witryn nadmierną liczbą żądań.
    - Sprawdź, czy witryna ma plik `robots.txt` – choć nie jest prawnie wiążący, określa zasady dotyczące automatycznego dostępu.

---

### **Podsumowanie**

**Scraping** jest potężnym narzędziem w programowaniu, które pozwala na zbieranie danych z różnych źródeł. Jego zastosowanie wymaga jednak odpowiedzialności, zarówno technicznej (minimalizacja obciążenia serwera), jak i prawnej (zgodność z regulaminem witryn). Z pomocą odpowiednich narzędzi i podejścia scraping może być kluczowy w analizie danych, budowie aplikacji czy monitorowaniu trendów.