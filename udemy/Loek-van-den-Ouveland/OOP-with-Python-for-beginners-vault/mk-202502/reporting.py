from abc import ABC, abstractmethod
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from employee import Employee

class Report(ABC):
    def __init__(self, emp_list: list[Employee]):
        self._emp_list = emp_list
        self.styles = getSampleStyleSheet()
        self.content = []  # Dodajemy atrybut content do klasy bazowej
        
    @abstractmethod
    def generate_content(self):
        """Generuje zawartość raportu"""
        pass

class AccountingReportPDF(Report):
    def generate_content(self):
        self.content.append(Paragraph("Accounting Report", self.styles['Heading1']))
        self.content.append(Spacer(1, 12))
        
        # Tworzenie tabeli
        data = [["Name", "Salary"]]  # Nagłówki
        for emp in self._emp_list:
            data.append([emp.get_full_name(), f"${emp.salary}"])
        
        table = Table(data)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))
        
        self.content.append(table)
        self.content.append(Spacer(1, 20))
        return self.content

class StaffingReportPDF(Report):
    def generate_content(self):
        self.content.append(Paragraph("Staffing Report", self.styles['Heading1']))
        self.content.append(Spacer(1, 12))
        
        # Tworzenie tabeli
        data = [["Name", "Position"]]  # Nagłówki
        for emp in self._emp_list:
            data.append([emp.get_full_name(), emp.job_title])
        
        table = Table(data)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))
        
        self.content.append(table)
        self.content.append(Spacer(1, 20))
        return self.content

class ScheduleReportPDF(Report):
    def generate_content(self):
        self.content.append(Paragraph("Schedule Report", self.styles['Heading1']))
        self.content.append(Spacer(1, 12))
        
        # Tworzenie tabeli
        data = [["Name", "Schedule"]]  # Nagłówki
        for emp in self._emp_list:
            data.append([emp.get_full_name(), emp.shift.get_shift_info()])
        
        table = Table(data)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))
        
        self.content.append(table)
        self.content.append(Spacer(1, 20))
        return self.content

def generate_combined_pdf(reports: list[Report], filename: str):
    """Generuje jeden plik PDF zawierający wszystkie raporty jeden pod drugim"""
    doc = SimpleDocTemplate(filename, pagesize=A4)
    all_content = []
    
    for report in reports:
        all_content.extend(report.generate_content())
    
    doc.build(all_content)

