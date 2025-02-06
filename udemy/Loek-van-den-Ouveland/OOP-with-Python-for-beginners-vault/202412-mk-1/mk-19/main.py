"""
c: 2024.12.18
M: 2024.12.18

19. SCHEDULE REPORT

1. Let's take the same approach as before.
"""
import re
import datetime as dt
from employee import Manager
from employee import Attendant
from employee import Cook
from employee import Mechanic
from reporting import AccountingReport
from reporting import StaffingReport
from reporting import ScheduleReport



employees  = [
    Manager("Vera", "Schmidt", 2000, dt.time(8, 00), dt.time(14, 00)),
    Attendant("Chuck", "Norris", 1800, dt.time(8, 00), dt.time(14, 00)),
    Attendant("Samantha", "Carrington", 1800, dt.time(12, 00), dt.time(20, 00)),
    Cook("Roberto", "Jacketti", 2100, dt.time(8, 00), dt.time(14, 00)),
    Mechanic("Dave", "Deribig", 2200, dt.time(8, 00), dt.time(14, 00)),
    Mechanic("Tina", "River", 2300, dt.time(8, 00), dt.time(14, 00)),
    Mechanic("Ringo", "Rama", 1900, dt.time(12, 00), dt.time(20, 00)),
    Mechanic("Chuck", "Rainey", 1800, dt.time(12, 00), dt.time(20, 00))
]

reports = [
    AccountingReport(employees),
    StaffingReport(employees),
    ScheduleReport(employees),
]

for r in reports:
    r.print_report()
    print()