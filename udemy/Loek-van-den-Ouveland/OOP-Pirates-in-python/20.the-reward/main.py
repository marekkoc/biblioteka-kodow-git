"""
Udemy.com

Object Oriented (Programming) Pirates in Python.


Skcja 8. Bank Exchange

20. The reward

C: 2024.11.30
M: 2024.11.30

Zmiana: 
"""
 
from data import TestDataLoader
from data import JSONDataLoader
from payroll import Payroll
from exchange import Bank


##### LOADING DATA ######################

#loader = TestDataLoader()
loader = JSONDataLoader()

bank = Bank(loader)
payroll = Payroll()

missions = loader.load_missions()
for mission in missions:
    print(mission)
    ducates = bank.exhange(mission.loot)
    print(f"Loot exhanges for {ducates} Ducats.")
    shares = payroll.calculate_shares(mission.crew, ducates)    
    for share in shares:
        print(share)
    print()
    