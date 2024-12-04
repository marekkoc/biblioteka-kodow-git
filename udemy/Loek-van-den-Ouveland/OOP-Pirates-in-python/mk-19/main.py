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
from exchange import Bank
print()

#loader: TestDataLoader = TestDataLoader()
loader: JSONDataLoader = JSONDataLoader()
missions = loader.load_missions()
payroll: Payroll = Payroll()
bank = Bank(loader)

for mission in missions:
    print(mission)
    ducats = bank.exchange(mission.loot)
    print(f"Loot exchanged for {ducats} Ducats.")
    shares = payroll.calculate_shares(mission.crew, ducats)
    for share in shares:
        print(share)
    print()
