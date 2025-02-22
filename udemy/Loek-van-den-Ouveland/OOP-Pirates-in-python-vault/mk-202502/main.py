from data import ( TestDataLoader,                  
                   JSONDataLoader)
from payroll import Payroll
from exchange import Bank

# data_loader = TestDataLoader()
data_loader = JSONDataLoader()

missions = data_loader.load_missions()

payroll = Payroll()

bank = Bank(data_loader)


for mission in missions:
    print(80*"*")
    print(mission)    
    ducats = bank.exchange(mission.loot)
    print(f"Loot exchanged for {ducats} Ducats")
    shares = payroll.calculate_shares(mission.crew, ducats)
    for share in shares:
        print(share) 
    print(80*"*")
    print()
