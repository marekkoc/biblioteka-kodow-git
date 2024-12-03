"""
Udemy.com

Object Oriented (Programming) Pirates in Python.

Moje testy. Powtorzenie całego kursu jeszcze raz.


C: 2024.12.02
M: 2024.12.02

Zmiana:
"""
from typing import List

from data import TestDataLoader
from data import JSONDataLoader
from payroll import Payroll


loader: TestDataLoader = TestDataLoader()
#loader: JSONDataLoader = JSONDataLoader()
pirates: List = loader.load_pirates()

ducats: int= 100
payroll: Payroll = Payroll()
shares = payroll.calculate_shares(pirates, ducats)

print()
for share in shares:
    print(share)
