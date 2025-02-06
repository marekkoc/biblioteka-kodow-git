"""
Udemy.com

Object Oriented (Programming) Pirates in Python.


Skcja 7. Payroll

16. Missions

C: 2024.11.26
M: 2024.11.26

Zmiana: 
"""
 
from data import TestDataLoader
from data import JSONDataLoader
from payroll import Payroll


##### LOADING DATA ######################

loader = TestDataLoader()
#loader = JSONDataLoader()

payroll = Payroll()
missions = loader.load_missions()
for mission in missions:
    print(mission)
    shares = payroll.calculate_shares(mission.crew, mission.loot)    
    for share in shares:
        print(share)
    print()
    