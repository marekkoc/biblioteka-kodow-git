class Employee:
    def __init__(self, first_name:str, last_name:str, salary:int):
        self._first_name: str = first_name
        self._last_name: str = last_name
        self.salary: int = salary

    def get_full_name(self):
        return f"{self._first_name} {self._last_name}"

    def __str__(self):
        return f" {self._first_name} {self._last_name}, ${self.salary}, {self.job_title}"


class Mechanic(Employee):
    job_title: str = "Mechanic"

class StationAttendant(Employee):
    job_title: str = "Station Attendant"

class Manager(Employee):
    job_title: str = "Manager"

class Cook(Employee):
    job_title: str = "Cook"    


    
        