"""
Udemy.com

Object Oriented (Programming) Pirates in Python.


Skcja 8. Bank Exchange

18. Exchange loot

C: 2024.11.27
M: 2024.11.27

Zmiana: 
"""
 
from data import TestDataLoader
from data import JSONDataLoader
from payroll import Payroll


##### LOADING DATA ######################

#loader = TestDataLoader()
loader = JSONDataLoader()


ducates = 100
payroll = Payroll()
missions = loader.load_missions()
for mission in missions:
    print(mission)
    shares = payroll.calculate_shares(mission.crew, mission.loot)    
    for share in shares:
        print(share)
    print()
    