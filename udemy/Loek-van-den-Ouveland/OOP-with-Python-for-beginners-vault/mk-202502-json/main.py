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
    ScheduleReport,
    JSONReport,
    DetailedJSONReport
)
from shift import(
    MorningShift,
    AfternoonShift,
    NightShift
)

if __name__ == "__main__":
    employees: list[Employee]   = [
        Manager("Vera", "Schmidt", 2000, MorningShift()),
        StationAttendant("Chuck", "Norris", 1800, MorningShift()),
        StationAttendant("Samantha", "Carrginton", 1800, AfternoonShift()),
        Cook("Roberto", "Jacketti", 2100, MorningShift()),
        Mechanic("Dave", "Drebig", 2200, MorningShift()),
        Mechanic("Tina", "River", 2300, MorningShift()),
        Mechanic("Ringo", "Rama", 1900, AfternoonShift()),
        Mechanic("Chuck", "Rainey", 1800, NightShift()),
        
    ]
    reports = [
        AccountingReport(employees),
        StaffingReport(employees),
        ScheduleReport(employees),
        JSONReport(employees),
        DetailedJSONReport(employees)
    ]
    for r in reports:
        r.print_report()
        print()

