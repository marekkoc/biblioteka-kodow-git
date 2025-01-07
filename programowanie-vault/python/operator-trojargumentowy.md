---
Utworzono: 2024-11-09T14:01:00
Zmodyfikowano: 2024-11-09T14:01:00
Źródło: 
tags:
---

W Pythonie taka składnia to **wyrażenie warunkowe** (conditional expression) lub potocznie **operator trójargumentowy** (ternary operator). Umożliwia ona przypisanie wartości do zmiennej na podstawie warunku w pojedynczej linii.

Składnia wygląda tak:

```python
x = wartość_jeśli_prawda if warunek else wartość_jeśli_fałsz
```

### Przykład

Przypisanie wartości do zmiennej `x` w zależności od tego, czy liczba jest parzysta:

```python
x = "parzysta" if zmienna % 2 == 0 else "nieparzysta"
```

Tutaj:

- Jeśli `zmienna % 2 == 0` jest prawdą, `x` otrzyma wartość `"parzysta"`.
- Jeśli nie, `x` przyjmie wartość `"nieparzysta"`.

### Wyjaśnienie składni

- `wartość_jeśli_prawda` – wartość przypisywana do zmiennej, gdy warunek jest prawdziwy.
- `if warunek` – warunek, który jest oceniany.
- `else wartość_jeśli_fałsz` – wartość przypisywana do zmiennej, gdy warunek jest fałszywy.

Wyrażenia warunkowe w jednej linii są użyteczne, gdy warunki są proste i kod jest bardziej przejrzysty dzięki tej formie zapisu.