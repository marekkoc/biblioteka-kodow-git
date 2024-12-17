"""
c: 2024.12.16
M: 2024.12.16

REFACTORIN

1. Gdy napiszemy jakas czesc kodu, powinnismy usiasc i ocenic nasz kod. Najwiekasza przyczyna tego ze kod staje sie
    bardzo zawily i trudny do zminy, jest presja czasowa.
2. Jesli napisany kod jest nieoptymalny (problematyczny) to nowy kod tez bedzie nieoptymalny (nawet bardziej problematyczny). To
    zmusi programistow do poswiecenia wiekszej ilosci czasu na implementowanie nowych rzeczy.
3. Jednym z sympotomow problematycznego kodu, jest to ze boimy sie wprowadzac nowych zmian do oprogramowania.
4. Najwazniesza rzecza jaka powinien zrobic programist jest refactoring codu ktory jest problematyczny

5.                                       CODE GROWS & CODE CHANGES

6. Bad code slows us down, bad code breaks things.--->>>> fix bad code

7.                          IF YOU THINK GOOD DESIGN IS EXPENSIVE, TRY BAD DESIGN

8. Now, we have some refactoring to do.
9. Let's split the code to a smaller files.
10. Our main function is as follows:
    A. classes
    B. data creation
    C. printing report
11. Good idea is to extrac a classes to a new file.
12 now: main.py module DEPENDS ON employee.py module
13. Nie importujemy klasy Employee, poniewaz jawnie nie tworzymy jej obiektow. Tworzymy obiekty ktore dziedzicza z Employee,
    dlatego wystarczy ze zaimprtujemy klasy obiektow dziedziczacych
14. Klasa ktora sluczy tylko do dziedziczenia, i nie jest przewidziane tworzenie jej obiektow jest nazywana klasa ABSTRAKCYJNA
15. 

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
print()
for e in employees:
    print(f"{e.name}, ${e.salary}, {e.job_title}")
print()