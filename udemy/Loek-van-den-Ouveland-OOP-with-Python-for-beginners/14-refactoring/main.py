"""
Udemy.com

Object Oriented Programming with Python for beginners.

Skcja 5. Refactor, Reports, Encapsulation

14. Refactoring

C: 2024.11.08
M: 2024.11.08
"""

from employee import Manager
from employee import Attendant
from employee import Cook
from employee import Mechanic

          
print()         
###################
employees = [
    Manager("Vera", 2000 ),
    Attendant("Chuck", 1800), 
    Attendant("Samantha", 1800), 
    Cook("Roberto", 2100),
    Mechanic("Dave", 2200),  
    Mechanic("Tina", 2300), 
    Mechanic("Ringo", 1900)  
]

for e in employees:
    print(f"{e.name}, ${e.salary}, {e.job_title}")
print()