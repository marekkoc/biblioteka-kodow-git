"""
c: 2024.12.16
M: 2024.12.16

SECOND REPORT

1. Dwa nowe raporty: 
    A. Accunting report
    B. Stuffing report
2. Obecnie raport jest drukowany w funkcji main. Teraz mamy go podzielic na dwa osobne raporty z odpowiednimi nagłówkami.
3. Utworzymy dwie nowe funkcje
    A. print_accounting_report()
    B. print_staffing_report()
4. Zatrudniamy nowego pracownika: Chuck Rainey. Problem jest taki ze juz jeden Chuck pracuje na stacji.
5. Aby rozróżnić pracowników, musimy dodać nazwiska.
6. Modyfikujemy klase Employee, zamiast atrybutu "name" towrzymy "first_name" i "last_name"

7. moduly:
    A. main.py --------> main2.py
    B employee.py -------->> employee2.py

"""
from employee import Manager
from employee import Attendant
from employee import Cook
from employee import Mechanic


employees  = [
    Manager("Vera", 2000),
    Attendant("Chuck", 1800),
    Attendant("Samantha", 1800),
    Cook("Roberto", 2100,),
    Mechanic("Dave", 2200),
    Mechanic("Tina", 2300),
    Mechanic("Ringo", 1900),
]

def print_accounting_report():
    print("Accounting")
    print("==========")
    for e in employees:
        print(f"{e.name}, ${e.salary}")

def print_staffing_report()-> None:
    print("Staffing")
    print("========")
    for e in employees:
        print(f"{e.name}, {e.job_title}")

print()
print_accounting_report()
print()
print_staffing_report()
print()