"""
Udemy.com

Object Oriented Programming with Python for beginners.

Skcja 7. Composition, Recap

19. Schedule Report

C: 2024.11.13
M: 2024.11.14
"""

from employee import Manager
from employee import Attendant
from employee import Cook
from employee import Mechanic
from reporting import AccountingReport
from reporting import StaffingReport
from reporting import ScheduleReport
 
import datetime as dt

          
print()         
###################
employees = [
    Manager("Vera", "Schmidt", 2000, dt.time(8,00), dt.time(14,00)),
    Attendant("Chuck", "Norris", 1800, dt.time(8,00), dt.time(14,00)), 
    Attendant("Samantha", "Carrington", 1800, dt.time(12,00), dt.time(20, 00)), 
    Cook("Roberto", "Jacketti", 2100, dt.time(8,00), dt.time(14,00)),
    Mechanic("Dave", "Dreibig", 2200, dt.time(8,00), dt.time(14,00)),  
    Mechanic("Tina", "River", 2300, dt.time(8,00), dt.time(14,00)), 
    Mechanic("Ringo", "Rama", 1900,dt.time(12,00), dt.time(20, 00)),
    Mechanic("Chack", "Rainey", 1800,dt.time(12,00), dt.time(20, 00))  
]

reports = [
    AccountingReport(employees),
    StaffingReport(employees),
    ScheduleReport(employees)
]

for r in reports:
    r.print_report()
    print()