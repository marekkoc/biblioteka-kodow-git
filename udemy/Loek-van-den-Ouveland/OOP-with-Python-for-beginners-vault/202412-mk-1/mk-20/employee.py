class Employee:
    def __init__(self, first_name:str, last_name:str, salary:int, shift):
        self._first_name: str = first_name
        self._last_name: str = last_name
        self.salary: int = salary
        self.shift = shift


    def get_full_name(self) -> str:
        return f"{self._first_name}, {self._last_name}"
    
class Mechanic(Employee):
    job_title = "Mechanic"

class Attendant(Employee):
    job_title = "Station Attendant"

class Cook(Employee):
    job_title = "Cook"

class Manager(Employee):
    job_title = "Manager"