"""
Udemy.com

Object Oriented (Programming) Pirates in Python.


Skcja 5. Polyorphism

10. Extra Officer and Cannon Operator

C: 2024.11.24
M: 2024.11.24

Zmiana: 
"""
 
from data import DataLoader
from data import JSONDataLoader


# loader = DataLoader()
loader = JSONDataLoader()
pirates = loader.load_pirates()


ducates = 1024
sum_of_ranks = sum(pirate.rank for pirate in pirates)

print("\n" + 45 * "*")
for pirate in pirates:
    share = pirate.rank / sum_of_ranks * ducates
    print(f"{pirate.title} {pirate.name} gets {share:.2f} Ducates")

print(45 * "*" , end="\n")