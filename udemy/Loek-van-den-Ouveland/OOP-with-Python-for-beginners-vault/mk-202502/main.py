#!/usr/bin/env python3
from employee import (
    Employee,
    Manager, 
    StationAttendant, 
    Cook, 
    Mechanic
)
from reporting import(
    AccountingReport,
    StaffingReport,
    ScheduleReport
)
from datetime import time

if __name__ == "__main__":
    employees: list[Employee]   = [
        Manager("Vera", "Schmidt", 2000, time(8,00), time(14,00)),
        StationAttendant("Chuck", "Norris", 1800, time(8,00), time(14,00)),
        StationAttendant("Samantha", "Carrginton", 1800, time(12,00), time(20,00)),
        Cook("Roberto", "Jacketti", 2100, time(8,00), time(14,00)),
        Mechanic("Dave", "Drebig", 2200, time(8,00), time(14,00)),
        Mechanic("Tina", "River", 2300, time(8,00), time(14,00)),
        Mechanic("Ringo", "Rama", 1900, time(12,00), time(20,00)),
        Mechanic("Chuck", "Rainey", 1800, time(12,00), time(20,00)),
    ]
    reports = [
        AccountingReport(employees),
        StaffingReport(employees),
        ScheduleReport(employees)
    ]
    for r in reports:
        r.print_report()
        print()

