from data import ( TestDataLoader,                  
                   JSONDataLoader)
from payroll import Payroll

data_loader = TestDataLoader()
#data_loader = JSONDataLoader()
pirates = data_loader.load_pirates()

ducats = 100

payroll = Payroll()
shares = payroll.calculate_shares(pirates, ducats)

print(80*"*")
for share in shares:
    print(share) 
print(80*"*")
