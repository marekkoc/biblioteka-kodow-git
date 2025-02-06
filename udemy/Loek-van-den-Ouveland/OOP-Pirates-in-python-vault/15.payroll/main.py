"""
Udemy.com

Object Oriented (Programming) Pirates in Python.


Skcja 7. Payroll

15. Payroll

C: 2024.11.25
M: 2024.11.26

Zmiana: 
"""
 
from data import TestDataLoader
from data import JSONDataLoader
from payroll import Payroll


##### LOADING DATA ######################

loader = TestDataLoader()
#loader = JSONDataLoader()
pirates = loader.load_pirates()

ducates = 100
payroll = Payroll()
shares = payroll.calculate_shares(pirates, ducates)

print("\n" + 45 * "*")
for share in shares:
    print(share)
print(45 * "*" , end="\n")