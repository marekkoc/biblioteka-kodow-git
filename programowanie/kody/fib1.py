#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 00:15:48 2024
Modified: 2024.10.13

Algorytm fibonacciego na podstawie książki:
    2019#Kopec_Classic-computer-science-problems

@author: marek
"""

"""
# Ta funkcja wygeneruje rekurencję nieskończoną,
# ponieważ nie ma warunku bazowego (ograniczenia)
def fib1(n: int) -> int:
return fib1(n - 1) + fib1(n - 2)
"""
import sys

def fib2(n:int)->int:
    if n<2: # base case
        return n
    else:
        return fib2(n-1) + fib2(n-2) # recursive case

def fib2A(n:int)->int:
    """
    To jest moja modyfikacja, aby wypisać wartość kolejnego elementu, oraz obliczona wartosc ciągu dla tego elementu.
    C: 2024.10.13
    M: 2024.10.13
    """

    if n < 2: # warunek bazowy
        return n
    else:
        result= fib2A(n-1) + fib2A(n-2)
        print(f"F({n}) -> {result}")
        return result

def fibonacci(n):
    # kod wygenerowany przez chatGPT
    # Dodaj `print` do rekurencyjnej funkcji, aby śledzić każdy krok
    print(f"Calculating Fibonacci of {n}")
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Wywołanie rekursywne z `print`
        result = fibonacci(n - 1) + fibonacci(n - 2)
        print(f"Fibonacci({n}) = {result}")
        return result







if __name__ == "__main__":

    #fib2A(7)

    # Wywołanie funkcji
    fibonacci(5)
