from datetime import datetime
import json
from employee import (
    Employee,
    Manager,
    StationAttendant,
    Cook,
    Mechanic
)

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
            print(f"{emp.get_full_name()}, {emp.shift.get_shift_info()}")



class JSONReport(Report):
    def print_report(self):
        report_data_dct:dict[str, list[str]] = {}
        
        for emp in self._emp_list:
            job:str = emp.job_title.lower().replace(' ', '_') + 's'
            if job not in report_data_dct:
                report_data_dct[job] = []
            report_data_dct[job].append(emp.get_full_name())

        with open("raport.json", "w", encoding="utf-8") as f:
            json.dump(report_data_dct, f, indent=4, ensure_ascii=False)

class DetailedJSONReport(Report):
    def print_report(self):
        report_data  = {
            "report_date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "company_stats": {
                "total_employees": len(self._emp_list),
                "departments": {}
            },
            "staff_details": {}
        }

        # Grupowanie pracowników według stanowisk
        for emp in self._emp_list:
            job = emp.job_title.lower().replace(' ', '_') + 's'
            
            # Inicjalizacja kategorii jeśli nie istnieje
            if job not in report_data["staff_details"]:
                report_data["staff_details"][job] = []
                report_data["company_stats"]["departments"][job] = {
                    "count": 0,
                    "average_salary": 0.0
                }
            
            # Dodawanie szczegółów pracownika
            employee_details = {
                "name": emp.get_full_name(),
                "salary": emp.salary,
                "contact": {
                    "email": f"{emp.get_full_name()}@company.com".lower().replace(' ', '.'  ),
                    "phone": emp.phone if hasattr(emp, 'phone') else "N/A"
                }
            }
            
            report_data["staff_details"][job].append(employee_details)
            
            # Aktualizacja statystyk
            dept_stats = report_data["company_stats"]["departments"][job]
            dept_stats["count"] += 1
            dept_stats["average_salary"] = (
                (dept_stats["average_salary"] * (dept_stats["count"] - 1) + emp.salary)
                / dept_stats["count"]
            )

        with open("detailed_report.json", "w", encoding="utf-8") as f:
            json.dump(report_data, f, indent=4, ensure_ascii=False)


