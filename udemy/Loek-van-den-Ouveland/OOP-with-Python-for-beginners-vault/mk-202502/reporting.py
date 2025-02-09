from employee import Employee

class Report:
    def __init__(self, emp_list: list[Employee]):
        self._emp_list = emp_list


class AccountingReport(Report):
    def print_report(self):
        print("Accounting report")
        print("-" * 40)
        for emp in self._emp_list:
            print(f"{emp.get_full_name()}, ${emp.salary}")


class StaffingReport(Report):
    def print_report(self):
        print("Staffing report")
        print("-" * 40)
        for emp in self._emp_list:
            print(f"{emp.get_full_name()},  {emp.job_title}")

class ScheduleReport(Report):
    def print_report(self):
        print("Schedule report")
        print("-" * 40)
        for emp in self._emp_list:
            print(f"{emp.get_full_name()}, {emp.start_time:%H:%M} to {emp.end_time:%H:%M}")

