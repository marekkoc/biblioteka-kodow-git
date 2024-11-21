"""
Project: Daily weight analysis.

The main script.

Copyright: Marek

Created: 2024.11.17
Modified: 2024.11.18
"""
from folders import Folders
from sheets import ExcelSheet
from years import YearlyDF


print()
f = Folders()
ex = ExcelSheet(f.get_excel_file_path())

sheets = [
    YearlyDF(2017, ex.get_sheet(2017)),
    YearlyDF(2018, ex.get_sheet(2018)),
    YearlyDF(2019, ex.get_sheet(2019)),
    YearlyDF(2020, ex.get_sheet(2020)),
    YearlyDF(2021, ex.get_sheet(2021)),
    YearlyDF(2022, ex.get_sheet(2022)),
    YearlyDF(2023, ex.get_sheet(2023)),
    YearlyDF(2024, ex.get_sheet(2024)) ]

for s in sheets[:2]:
    print(f"name: {s.name}")
    print(s.get_mean_by_monty())
