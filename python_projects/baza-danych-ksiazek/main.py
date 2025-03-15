"""
Baza danych książek

Copyright (c) 2025 Marek Kocinski

Created: 2025.02.17
Modified: 2025.02.17
"""


from dane import TestData
from report import Report

data = TestData()
ksiazki =data.load_data()

print()
raport = Report(ksiazki)
raport.generuj_raport()

print("\n")
raport.generuj_raport(sort_by='autor')

print("\n")
raport.generuj_raport(sort_by='rok')

print("\n")
raport.generuj_raport(sort_by='tytul')



