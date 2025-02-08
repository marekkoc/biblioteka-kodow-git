#!/usr/bin/env conda run -n py312 
from employee import (
    Employee,
    Manager, 
    StationAttendant, 
    Cook, 
    Mechanic
)


if __name__ == "__main__":
    employees: list[Employee]   = [
        Manager("Vera", "Schmidt", 2000),
        StationAttendant("Chuck", "Norris", 1800),
        StationAttendant("Samantha", "Carrginton", 1800),
        Cook("Roberto", "Jacketti", 2100),
        Mechanic("Dave", "Drebig", 2200),
        Mechanic("Tina", "River", 2300),
        Mechanic("Ringo", "Rama", 1900),
        Mechanic("Chuck", "Rainey", 1800)
    ]

    def print_accounting_report(employees: list[Employee]):
        print("Accounting report")
        print("-" * 40)
        for emp in employees:
            print(f"{emp.get_full_name()}, ${emp.salary}")

    def print_staffing_report(employees: list[Employee]):
        print("Staffing report")
        print("-" * 40)
        for emp in employees:
            print(f"{emp.get_full_name()},  {emp.job_title}")

    print()
    print_accounting_report(employees)
    print()
    print_staffing_report(employees)


