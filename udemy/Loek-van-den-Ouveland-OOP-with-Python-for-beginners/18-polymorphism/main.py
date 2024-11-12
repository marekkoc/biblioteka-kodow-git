"""
Udemy.com

Object Oriented Programming with Python for beginners.

Skcja 6. Dependency Injection, Polymorphism

18. Polymorphism

C: 2024.11.10
M: 2024.11.11
"""

from employee import Manager
from employee import Attendant
from employee import Cook
from employee import Mechanic
from reporting import AccountingReport
from reporting import StaffingReport

          
print()         
###################
employees = [
    Manager("Vera", "Schmidt", 2000 ),
    Attendant("Chuck", "Norris", 1800), 
    Attendant("Samantha", "Carrington", 1800), 
    Cook("Roberto", "Jacketti", 2100),
    Mechanic("Dave", "Dreibig", 2200),  
    Mechanic("Tina", "River", 2300), 
    Mechanic("Ringo", "Rama", 1900),
    Mechanic("Chack", "Rainey", 1800)  
]

reports = [
    AccountingReport(employees),
    StaffingReport(employees)
]

for r in reports:
    r.print_report()
    print()