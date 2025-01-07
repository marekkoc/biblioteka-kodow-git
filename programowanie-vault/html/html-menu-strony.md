---
Utworzono: 2024-10-21T10:42:00
Zmodyfikowano: 2024-10-21T10:42:00
Źródło: chatGPT
tags:
  - "#HTML-menu"
---

# Prosta wersja menu strony z użyciem HTML

To jest uproszczona wersja menu, jakie miał zamieszczone AM na swojej stronie, oraz jakie ja miałem na swojej stronie w pierwszej próbie.



Oto uproszczony kod HTML dla menu z trzema elementami: **Home**, **Doktoranci**, **Dydaktyka**. Jest to prostsza wersja, bez dodatkowych klas CSS i bez zagnieżdżonych elementów, ale z podstawowymi linkami:

```html
<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Menu nawigacyjne</title>
    <style>
        /* Prosty styl dla menu */
        nav {
            background-color: #f2f2f2;
            padding: 10px;
        }
        ul {
            list-style-type: none; /* Usuń punktor z listy */
            margin: 0;
            padding: 0;
            display: flex; /* Ustaw pozycje w jednej linii */
        }
        li {
            margin-right: 20px; /* Odstęp między elementami */
        }
        a {
            text-decoration: none; /* Usuń podkreślenie z linków */
            color: #000; /* Kolor tekstu */
        }
        a:hover {
            color: #007BFF; /* Kolor linku po najechaniu myszką */
        }
    </style>
</head>
<body>

    <nav>
        <ul>
            <li><a href="index.html">Home</a></li>
            <li><a href="doktoranci.html">Doktoranci</a></li>
            <li><a href="dydaktyka.html">Dydaktyka</a></li>
        </ul>
    </nav>

</body>
</html>
```

### Wyjaśnienie:

1. **HTML**:
    - Kod znajduje się w znaczniku `<nav>`, co wskazuje, że zawiera on element nawigacyjny.
    - Wewnątrz znajduje się lista nieuporządkowana (`<ul>`), a każdy element listy (`<li>`) zawiera odnośnik (`<a>`).
    - Każdy link (`<a>`) prowadzi do innej strony (np. `"doktoranci.html"` dla strony "Doktoranci").

2. **CSS**:
    - Prosty styl dla menu: 
        - Menu ma szary pasek tła (`background-color: #f2f2f2`) i lekkie wcięcie (`padding: 10px`).
        - Elementy listy wyświetlane są w jednej linii dzięki `display: flex;`.
        - Linki są stylizowane, aby były bez podkreślenia, a po najechaniu myszką zmieniają kolor na niebieski (`color: #007BFF`).

To menu jest prostsze i łatwiejsze do zrozumienia na początek, a jednocześnie można łatwo rozbudować je o dodatkowe funkcjonalności.