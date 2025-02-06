"""
c: 2024.12.16
M: 2024.12.16

INHERITANCE

1. Chcemy zminić nazwy zawodów:
    - Attendatn -> Station Attendant
    - Mechanic -> Mechanic
2. Zmiana dwóch nazw zawodów wymaga zmiany kodu w 5 miejscach, ---> Zatem jest to "duplicate code"
3. Zróbmy typ pracownika (Employee type), ktory automatycznie wie/rozpoznaje typ pracownika:
     jeden dla mechanika, jeden dal kuchrza, jeden dla menadzera, itp. Aby to zrobić wykorzystamy DZIEDZICZENIE.
4. Oddzielamy rzeczy SPECYFICZNE/CHARAKTERYSTYCZNE dla danej klasy (zawodu) od rzeczy OGOLNYCH
     ktore sa takie same dla wszystkich zawodów 
5. W przyszłośći jeżeli będziemy musieli zmienić nazwę zawodu, to zrobimy to TYLKO w klasie opiującej ten zawód. Oddzielamy
    rzeczy CHARAKTERYSTYCZNE dla MECHANIKA do oddzielnej klasy! Grupujemy charakterystyczne cechy mechanika w jednej klasie,
    a rzeczy wspólne dla wszystkich pozostają w klasie EMPLOYEE.
6. The MECHANIC class is SPLIT of EMPLOYEE ---> MECHANIC inherits from EMPOLOYEE
7. INHERITING means that MECHANIC has all attributes from EMPLOYEE (name, salary) plus one more a job_title
8. The EMPLOYEE is a SUPERCLASS while MECHANIC and ATTENDANT are SUBCLASSES of EMPLOYEE
9. W klasach dziedziczących nie musimy implementowac konstruktora, jako że klasy dziedziczące dziedziczą wszystkie atrybuty
    z klasy rodzica, zatem dziedziczą również konstruktor.
10. Zmienna job_title jest zdefinowana bezpośrednio w klasi ->> zmienna klasowa (statyczna), taka zmienna nie jest definiowana dla 
    poszczególnego obiektu (nie posiada wskaznika self), ale jest wspolna dla wszystkich obiektow danej klasy. 
11. Zmienne lub metody defionowane bezposrednio w klasie, za nazywane atrybutami lub metodami klasowymi.
12. Zmienne ze wskaznikiem self (name, salary) maja inna wartoasc w kazdej instancji (obiekcie) danej klasy, a zmienne klasowe
    maja taka sama wartosc (wspoldziela ta wartosc) dla wszyskich obiektow (instancji) danej klasy
13. W diagramie UML zmienne klasowe sa podkreslone.     
"""

class Employee:
    def __init__(self, name:str, salary:int):
        self.name: str = name
        self.salary: int = salary
    
class Mechanic(Employee):
    job_title = "Mechanic"

class Attendant(Employee):
    job_title = "Station Attendant"

class Cook(Employee):
    job_title = "Cook"

class Manager(Employee):
    job_title = "Manager"



employees: list[Employee] = [
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
