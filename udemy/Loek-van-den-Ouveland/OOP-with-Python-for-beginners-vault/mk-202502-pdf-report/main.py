#!/usr/bin/env python3
from employee import (
    Employee,
    Manager, 
    StationAttendant, 
    Cook, 
    Mechanic
)
from reporting import(
    AccountingReportPDF,
    StaffingReportPDF,
    ScheduleReportPDF
)
from shift import(
    MorningShift,
    AfternoonShift,
    NightShift
)
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.pagesizes import A4

custom_style = ParagraphStyle(
    'CustomStyle',
    fontSize=12,
    leading=14,
    textColor=colors.black,
    spaceAfter=6
)

def header(canvas, doc):
    canvas.saveState()
    canvas.setFont('Helvetica', 10)
    canvas.drawString(30, 750, "Company Report")
    canvas.restoreState()

if __name__ == "__main__":
    employees: list[Employee]   = [
        Manager("Vera", "Schmidt", 2000, MorningShift()),
        StationAttendant("Chuck", "Norris", 1800, MorningShift()),
        StationAttendant("Samantha", "Carrginton", 1800, AfternoonShift()),
        Cook("Roberto", "Jacketti", 2100, MorningShift()),
        Mechanic("Dave", "Drebig", 2200, MorningShift()),
        Mechanic("Tina", "River", 2300, MorningShift()),
        Mechanic("Ringo", "Rama", 1900, AfternoonShift()),
        Mechanic("Chuck", "Rainey", 1800, NightShift()),
        
    ]
    
    # Tworzymy jeden dokument PDF
    doc = SimpleDocTemplate("combined_report.pdf", pagesize=A4)
    
    # Zbieramy zawartość ze wszystkich raportów
    all_content = []
    
    # Generujemy raporty i zbieramy ich zawartość
    accounting_report = AccountingReportPDF(employees)
    staffing_report = StaffingReportPDF(employees)
    schedule_report = ScheduleReportPDF(employees)
    
    # Dodajemy zawartość każdego raportu do wspólnej listy
    all_content.extend(accounting_report.generate_content())
    all_content.extend(staffing_report.generate_content())
    all_content.extend(schedule_report.generate_content())
    
    # Budujemy jeden dokument ze wszystkimi raportami
    doc.build(all_content)

