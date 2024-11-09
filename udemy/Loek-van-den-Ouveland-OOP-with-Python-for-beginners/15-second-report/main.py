"""
Udemy.com

Object Oriented Programming with Python for beginners.

Skcja 5. Refactor, Reports, Encapsulation

15. Second report

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
    Manager("Vera", "Schmidt", 2000 ),
    Attendant("Chuck", "Norris", 1800), 
    Attendant("Samantha", "Carrington", 1800), 
    Cook("Roberto", "Jacketti", 2100),
    Mechanic("Dave", "Dreibig", 2200),  
    Mechanic("Tina", "River", 2300), 
    Mechanic("Ringo", "Rama", 1900),
    Mechanic("Chack", "Rainey", 1800)  
]

def pring_accounting_report():
    print('Accounting')
    print("==========")
    for e in employees:
        print(f"{e.first_name} {e.last_name}, ${e.salary}")

def print_staffing_report():
    print("Staffing")
    print("========") 
    for e in employees:
        print(f"{e.first_name} {e.last_name}, {e.job_title}")

pring_accounting_report()
print() # empty line
print_staffing_report()
print() # empty line