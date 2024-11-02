"""
Udemy.com

Object Oriented Programming with Python for beginners.

11. UML, Inheritence

C: 2024.11.01
M: 2024.11.01
"""

class Employee:
    def __init__(self, name, salary, job_title):
        self.name = name
        self.salary = salary
        self.job_title = job_title

e = Employee("Vera", 2000, "Manager")
print(e)
print(f"{e.name}, ${e.salary}, {e.job_title}\n\n")

###################
employees = [
    Employee("Vera", 2000, "Manager"),
    Employee("Chuck", 1800, "Attendant"),
    Employee("Samantha", 1800, "Attendant"),
    Employee("Roberto", 2100, "Cook"),
    Employee("Dave", 2200, "Car Repair"),
    Employee("Tina", 2300, "Car Repair"),
    Employee("Ringo", 1900, "Car Repair")
]

for e in employees:
    print(f"{e.name}, ${e.salary}, {e.job_title}")
