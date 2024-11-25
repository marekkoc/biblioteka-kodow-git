"""
Udemy.com

Object Oriented (Programming) Pirates in Python.


Skcja 6. Composition

14. Test with Test DataLoader

C: 2024.11.25
M: 2024.11.25

Zmiana: 
"""
 
from data import TestDataLoader
from data import JSONDataLoader

##### LOADING DATA ######################

loader = TestDataLoader()
#loader = JSONDataLoader()
pirates = loader.load_pirates()

####### DUCATES AND SUM OF RANKS ##########
ducates = 100
sum_of_ranks = sum(pirate.role.rank for pirate in pirates)


####### PRINTING REPORTS ################
print("\n" + 45 * "*")
for pirate in pirates:
    share = pirate.role.rank / sum_of_ranks * ducates
    print(f"{pirate.role.title} {pirate.name} gets {share:.2f} Ducates")

print(45 * "*" , end="\n")