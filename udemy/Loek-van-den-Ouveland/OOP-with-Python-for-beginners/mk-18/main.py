"""
c: 2024.12.17
M: 2024.12.17

18. POLYMORPHISM

1. Obie klasy maja wspolny kod --->>> czyli konstruktor. W obu klasach konstruktor jest taki sam.
2. Obie klasy maja ten sam konstruktor i ten sam atrybut (employee_list) --->>> jest to DUPLICATE CODE!
3. DUPLICATE CODE --->>>  jest to KOD OGOLNY (GENERIC CODE) ktory moze byc wydzielony (isolated) 
     od kodu charakterystycznego dla danej klasy (SPECIFIC CODE)
4. Zrobmy klase nadrzedna, klase rodzica i uzyjmy DZIEDZICZENIA do wydzielenia kodu ogolnego, wspolnego.
5. Chcemy wydrukowac kilka raportow w petli for.
6. 

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