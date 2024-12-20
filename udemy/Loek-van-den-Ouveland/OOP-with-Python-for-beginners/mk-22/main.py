"""
c: 2024.12.19
M: 2024.12.19

22. Unit testing

1. Testing code is important part of software engineering
2. We can test if:
    A. function woks
    B. class works
    C. the whole app works
3. There are 3 types of tests:
    A. Unit tests => test of individual part of the code (like functions and classes). Has two possible outcoms: SUCCESS or FAIL
    B. INTEGRATION TESTS - combines modules and tests grups of functionality
    C. SYSTEM TESTS ->> test complite system
4. We'll look at unit tests

"""
import datetime as dt
from employee import Manager
from employee import Attendant
from employee import Cook
from employee import Mechanic
from reporting import AccountingReport
from reporting import StaffingReport
from reporting import ScheduleReport
from shift import MorningShift, NightShift
from shift import AfternoonShift


employees  = [
    Manager("Vera", "Schmidt", 2000, MorningShift()),
    Attendant("Chuck", "Norris", 1800, MorningShift()),
    Attendant("Samantha", "Carrington", 1800, AfternoonShift()),
    Cook("Roberto", "Jacketti", 2100, MorningShift()),
    Mechanic("Dave", "Deribig", 2200, MorningShift()),
    Mechanic("Tina", "River", 2300, MorningShift()),
    Mechanic("Ringo", "Rama", 1900, AfternoonShift()),
    Mechanic("Chuck", "Rainey", 1800, NightShift())
]

reports = [
    AccountingReport(employees),
    StaffingReport(employees),
    ScheduleReport(employees),
]

for r in reports:
    r.print_report()
    print()