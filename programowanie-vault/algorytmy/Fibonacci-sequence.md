---
Data utworzenia: 2024-10-12
Data modyfikacji: 2024-10-12T23:24:00
Opis: Algorytm Fibonacciego
tags:
  - "#Fibonacci-algorytm"
Uwagi: 
To do: 
"Skrypt:": kody/fib1.py
---


Żródło: Książka 
Tytuł : #book-2019-kopec-classic-computer-science-problems-in-python , Rozdział 1


# Algorytm

W ciągu liczb Fibonacciego każda kolejna liczba (oprócz dwóch pierwszych) jest równa sumie dwóch liczb poprzednich:

$0, 1, 1, 2, 3, 5, 8, 13, 21, ...$

Zatem ogólne równianie które opisuje ciąg Fibonacciego jest następujące:

$$ fib(n) = fib(n-1) + fib(n-2) $$

Aby zaimplementować funkcję która oblicza dowolny element kodu Fibonacciego, możemy użyć **funkcji rekursywnej**. Funkcja **rekursywna** to taka funkcja, która wywołuje samą siebie.

```Python
def fib1(n: int) -> int:
	return fib(n-1) + fib(n-2)
```

W funkcji rekursywnej musimy zdefiniować **warunek bazowy**, taki warunek, który w odpowiednim miejscu przerwie wykonywanie się funkcji.

It is the duty of the programmer to avoid infinite recursion, not the compiler or the interpreter. The reason for the infinite recursion is that we never specified a base case. In a recursive function, a base case serves as a stopping point.

In the case of the Fibonacci function, we have **natural base cases** in the form of the
special first two sequence values, 0 and 1. **Neither 0 nor 1 is the sum of the previous**
**two numbers** in the sequence. Instead, **they are the special first two values.**