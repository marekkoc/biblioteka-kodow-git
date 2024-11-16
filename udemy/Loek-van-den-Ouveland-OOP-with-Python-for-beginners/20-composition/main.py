"""
Udemy.com

Object Oriented Programming with Python for beginners.

Skcja 7. Composition, Recap

20. Composition

C: 2024.11.14
M: 2024.11.14
"""

from employee import Manager
from employee import Attendant
from employee import Cook
from employee import Mechanic
from reporting import AccountingReport
from reporting import StaffingReport
from reporting import ScheduleReport
from shift import MorningShift
from shift import AfternoonShift
from shift import NightShift
 
          
print()         
###################
employees = [
    Manager("Vera", "Schmidt", 2000, MorningShift()),
    Attendant("Chuck", "Norris", 1800, MorningShift()), 
    Attendant("Samantha", "Carrington", 1800,  AfternoonShift()), 
    Cook("Roberto", "Jacketti", 2100, MorningShift()),
    Mechanic("Dave", "Dreibig", 2200, MorningShift()),  
    Mechanic("Tina", "River", 2300, MorningShift()), 
    Mechanic("Ringo", "Rama", 1900, AfternoonShift()),
    Mechanic("Chack", "Rainey", 1800, NightShift())  
]

reports = [
    AccountingReport(employees),
    StaffingReport(employees),
    ScheduleReport(employees)
]

for r in reports:
    r.print_report()
    print()