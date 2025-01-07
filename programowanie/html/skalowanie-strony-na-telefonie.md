---
Utworzono: 2024-11-05T08:14:00
Zmodyfikowano: 2024-11-05T08:14:00
Źródło: 
tags:
---

Aby Twoja statyczna strona internetowa dobrze skalowała się na urządzeniach mobilnych, możesz zastosować kilka technik:

### 1. Dodaj Meta Tag dla Widoku Mobilnego
Dodaj poniższy kod w sekcji `<head>` swojej strony. Ten meta tag instruuje przeglądarki na urządzeniach mobilnych, by wyświetlały stronę dopasowaną do szerokości ekranu.

```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```

### 2. Użyj CSS Flexbox lub Grid
Flexbox i Grid pozwalają tworzyć elastyczne układy, które automatycznie dostosowują się do rozmiaru ekranu. Na przykład:

```css
.container {
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
}
```

### 3. Dodaj Style CSS dla Różnych Rozdzielczości (Media Queries)
Media Queries pozwalają ustalić różne style dla różnych rozdzielczości ekranu. Oto przykład, który dostosowuje układ do ekranów o szerokości mniejszej niż 768px:

```css
/* Style dla urządzeń mobilnych */
@media (max-width: 768px) {
  .container {
    flex-direction: column;
  }
  .content {
    font-size: 14px;
  }
}
```

### 4. Ustaw Elementy na Procentach Zamiast Pikselach
Aby uzyskać większą elastyczność, ustaw szerokości, marginesy i paddingi elementów na procentach, a nie na stałych wartościach.

```css
.container {
  width: 100%;
}
.column {
  width: 50%; /* Działa dobrze na większych ekranach */
}
@media (max-width: 768px) {
  .column {
    width: 100%; /* Na urządzeniach mobilnych kolumny zajmują całą szerokość */
  }
}
```

### 5. Użyj Ram Głównych (Frameworks) jak Bootstrap
Jeśli nie chcesz pisać kodu od podstaw, możesz użyć frameworka CSS, np. **Bootstrap**. Bootstrap zawiera gotowe klasy i komponenty, które automatycznie skalują się na różnych urządzeniach.