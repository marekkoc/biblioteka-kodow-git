"""
Udemy.com

Object Oriented (Programming) Pirates in Python.


Skcja 6. Composition

13. Composition over Inheritace

C: 2024.11.25
M: 2024.11.25

Zmiana: 
"""
 
from data import DataLoader
from data import JSONDataLoader


# loader = DataLoader()
loader = JSONDataLoader()
pirates = loader.load_pirates()


ducates = 1610
sum_of_ranks = sum(pirate.role.rank for pirate in pirates)

print("\n" + 45 * "*")
for pirate in pirates:
    share = pirate.role.rank / sum_of_ranks * ducates
    print(f"{pirate.role.title} {pirate.name} gets {share:.2f} Ducates")

print(45 * "*" , end="\n")