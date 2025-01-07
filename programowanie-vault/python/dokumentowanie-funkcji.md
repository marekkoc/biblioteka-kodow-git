W Pythonie dokumentowanie funkcji najczęściej odbywa się poprzez dodawanie docstringów. Docstringi to specjalne komentarze w formie łańcuchów znaków, które umieszcza się bezpośrednio pod nagłówkiem funkcji. Przechowują one opis działania funkcji, jej parametrów i zwracanych wartości. Istnieje kilka popularnych konwencji formatowania docstringów, a najczęściej stosowanymi są [**PEP 257**](https://peps.python.org/pep-0257/), #pep-257 )**Google style** ([example](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html#example-numpy)), oraz **reStructuredText (reST)**.

Oto kilka przykładów dokumentowania funkcji zgodnie z różnymi konwencjami:

### 1. Prosty docstring
To najkrótsza forma docstringa, zawierająca opis funkcji.

```python
def add(a, b):
    """Return the sum of a and b."""
    return a + b
```

### 2. Docstring z opisem parametrów i typu zwracanej wartości (Google style)

```python
def add(a: int, b: int) -> int:
    """Add two numbers.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The sum of a and b.
    """
    return a + b
```

### 3. Docstring w stylu reStructuredText (reST)

```python
def add(a: int, b: int) -> int:
    """
    Add two numbers.

    :param a: The first number.
    :type a: int
    :param b: The second number.
    :type b: int
    :return: The sum of a and b.
    :rtype: int
    """
    return a + b
```

### 4. Przykład docstringa z opisem wyjątków (Google style)

```python
def divide(a: float, b: float) -> float:
    """Divide two numbers.

    Args:
        a (float): Numerator.
        b (float): Denominator.

    Returns:
        float: Result of division.

    Raises:
        ValueError: If the denominator `b` is zero.
    """
    if b == 0:
        raise ValueError("The denominator cannot be zero.")
    return a / b
```

### Dobre praktyki przy pisaniu docstringów:

- **Opisuj działanie funkcji zwięźle i precyzyjnie**.
- **Pisz w czasie teraźniejszym** (np. „Return” zamiast „Returns”).
- **Dokumentuj parametry i typ zwracanej wartości**, aby kod był bardziej czytelny dla innych użytkowników.
- **Używaj konwencji Google lub reST**, jeśli dokumentacja będzie generowana automatycznie (np. przez narzędzia jak Sphinx).