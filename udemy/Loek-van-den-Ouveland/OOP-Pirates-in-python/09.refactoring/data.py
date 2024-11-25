"""
Udemy.com

Object Oriented (Programming) Pirates in Python.

Skcja 4. Inheritance

8. Refactoring

C: 2024.11.24
M: 2024.11.24

Zmiana
"""
from pirates import Capitan
from pirates import Quartermaster
from pirates import Officer
from pirates import CannonOperator

class DataLoader:
    def load_pirates(self):
        return [
        Capitan("Harry"),
        Quartermaster("Isabel"),
        Officer("Bootstrap Bill"),
        CannonOperator("Powder Joe"),
        Officer("Four Finger Fritz"),
        CannonOperator("Lady Joice")
        ]