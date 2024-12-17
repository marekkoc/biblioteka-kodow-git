"""
c: 2024.12.16
M: 2024.12.16

16. ENCAPSULATION

1. Gdy mamy zmienic ten sam kod w dwoch miejscach, zawsze jest ryzyko ze zmienimy w jednym a zapomnimy w drugim,
    lub ze popelnimy jakis balad.
2. Kolejnym problemem jest to ze funkcja do raportu musi wiedziec jak zabudowany jest obiekt e wewnetrznie, jakie posiada atrybuty.
    Raport nie musi znac takich detali jak wewnetrzna budowa obiektu.
3. Zatem mamy tutaj dwa problemy:
    A. Powtarzajacy sie kod
    B. Szczegoly implementacji
4.

"""
from employee import Manager
from employee import Attendant
from employee import Cook
from employee import Mechanic


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

def print_accounting_report():
    print("Accounting")
    print("==========")
    for e in employees:
        print(f"{e.get_full_name()}, ${e.salary}")

def print_staffing_report()-> None:
    print("Staffing")
    print("========")
    for e in employees:
        print(f"{e.get_full_name()}, {e.job_title}")

print()
print_accounting_report()
print()
print_staffing_report()
print()