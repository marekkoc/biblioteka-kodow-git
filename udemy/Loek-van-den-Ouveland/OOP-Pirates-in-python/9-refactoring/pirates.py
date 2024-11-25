"""
Udemy.com

Object Oriented (Programming) Pirates in Python.

Skcja 4. Inheritance

8. Refactoring

C: 2024.11.24
M: 2024.11.24

Zmiana: Splitting code up
"""

class Pirate:
    def __init__(self, name):
        self.name = name
        
class Capitan(Pirate):
    # class variables are hard coded
    title = "Capitan"
    rank = 10      

class Quartermaster(Pirate):
    title = "Quartermaster"
    rank = 9

class Officer(Pirate):
    title = "Officer"
    rank = 7

class CannonOperator(Pirate):
    title = "Cannon Operator"
    rank = 6
