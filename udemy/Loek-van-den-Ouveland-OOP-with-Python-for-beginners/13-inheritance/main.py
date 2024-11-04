"""
Udemy.com

Object Oriented Programming with Python for beginners.

Skcja 4. UML, Inheritance

13. Inheritance

C: 2024.11.03
M: 2024.11.03 
"""

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Mechanic(Employee):
    job_title = "Mechanic"  

class Attendant(Employee):
    job_title = "Station Attendant"

class Cook(Employee):
    job_title = "Cook"

class Manager(Employee):
    job_title = "Manager"
          
print()         
###################
employees = [
    Manager("Vera", 2000 ),
    Attendant("Chuck", 1800), 
    Attendant("Samantha", 1800), 
    Cook("Roberto", 2100),
    Mechanic("Dave", 2200),  
    Mechanic("Tina", 2300), 
    Mechanic("Ringo", 1900)  
]

for e in employees:
    print(f"{e.name}, ${e.salary}, {e.job_title}")
print()