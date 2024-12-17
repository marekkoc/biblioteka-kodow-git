class Employee:
    def __init__(self, name:str, salary:int, job_title:str):
        self.name: str = name
        self.salary: int = salary
        self.job_title: str = job_title


employees: list[Employee] = [
    Employee("Vera", 2000, "Manager"),
    Employee("Chuck", 1800, "Attendant"),
    Employee("Samantha", 1800, "Attendant"),
    Employee("Roberto", 2100, "Cook"),
    Employee("Dave", 2200, "Car Repair"),
    Employee("Tina", 2300, "Car Repair"),
    Employee("Ringo", 1900, "Car Repair"),
]
print()
for e in employees:
    print(f"{e.name}, ${e.salary}, {e.job_title}")
print()