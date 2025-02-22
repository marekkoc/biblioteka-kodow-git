from data import ( TestDataLoader,                  
                   JSONDataLoader)
from payroll import Payroll


#data_loader = TestDataLoader()
data_loader = JSONDataLoader()

missions = data_loader.load_missions()

payroll = Payroll()

for mission in missions:
    print(80*"*")
    print(mission)    
    shares = payroll.calculate_shares(mission.crew, mission.loot)
    for share in shares:
        print(share) 
    print(80*"*")
    print()
