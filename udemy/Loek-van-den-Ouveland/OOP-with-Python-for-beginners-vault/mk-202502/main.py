#!/usr/bin/env conda run -n py312 

class Employee:
    def __init__(self, name:str, salary:int):
        self.name: str = name
        self.salary: int = salary

    def __str__(self):
        return f" {self.name}, ${self.salary}"
        

if __name__ == "__main__":
    employees: list[Employee] = [
        Employee("Vera", 2000),
        Employee("Chuck", 1800),
        Employee("Samantha", 1800),
        Employee("Roberto", 2100),
        Employee("Dave", 2200),
        Employee("Ethan", 2000),
        Employee("Tina", 2300),
        Employee("Ringo", 1900)
    ]
    for emp in employees:
        print(emp)
