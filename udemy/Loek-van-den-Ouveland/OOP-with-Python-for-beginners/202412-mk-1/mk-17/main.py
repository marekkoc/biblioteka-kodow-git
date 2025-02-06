"""
c: 2024.12.17
M: 2024.12.17

17. DEPENDENCY INJECTION

1. Time to evaluate our code again. Our DEPENDENCY DIAGRAM goes in a good direction, from top to down.
2. Ale w funckcji main mamy dwie funkcje ktore drukuja raporty.
     Czy funkcja main.py powinna byc odpowiedzialna za drukowanie raportow? --->>>> NIE!!!!
3. Our reporting calsses depend on employee list.
4. When code can not be separated from other code, we say it is COUPLED!
5. COUPLING is a symptom of RIGIDE CODE! 
6. RIGID CODE is when we can not change parts of the code without changing other parts of the code.
7. DECOUPLING  jest to usuniecie dostepu do employee list jako zmiennej globalnej i przekazanie jej jako
     argumentu do konstrukora klass. --->>>> to sie nazywa DEPENDENCY INJECTION !!! We inject the things an object needs
     to work with.
8. DEPENDENCY INJECTION ---> to przekazaywanie zaleznosci podczas tworzenia obiektu (nie wiem czy tylko podczas tworzenia).
9. The accountint report has a DEPENDENCY on the list of employees. We inject this DEPENDENCY when we INSTANTIATE the OBJECT.
10. 


"""
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

accounting_report: AccountingReport = AccountingReport(employees)
accounting_report.print_accounting_report()
print()

staffing_report: StaffingReport = StaffingReport(employees)
staffing_report.print_staffing_report()
print()