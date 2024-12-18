"""
c: 2024.12.17
M: 2024.12.17

19. COMPOSITION

1.

"""
import re
from employee import Manager
from employee import Attendant
from employee import Cook
from employee import Mechanic
from reporting import AccountingReport
from reporting import StaffingReport


employees  = [
    Manager("Vera", "Schmidt", 2000),
    Attendant("Chuck", "Norris", 1800),
    Attendant("Samantha", "Carrington", 1800),
    Cook("Roberto", "Jacketti", 2100,),
    Mechanic("Dave", "Deribig", 2200),
    Mechanic("Tina", "River", 2300),
    Mechanic("Ringo", "Rama", 1900),
    Mechanic("Chuck", "Rainey", 1800)
]

reports = [
    AccountingReport(employees),
    StaffingReport(employees),
]

for r in reports:
    r.print_report()
    print()