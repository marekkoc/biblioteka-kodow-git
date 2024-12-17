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