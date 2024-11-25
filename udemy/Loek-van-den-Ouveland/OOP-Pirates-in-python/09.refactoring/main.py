"""
Udemy.com

Object Oriented (Programming) Pirates in Python.

Skcja 4. Inheritance

8. Refactoring

C: 2024.11.24
M: 2024.11.24

Zmiana: Splitting code up
"""
 
from data import DataLoader


loader = DataLoader()
pirates = loader.load_pirates()


ducates = 920
sum_of_ranks = sum(pirate.rank for pirate in pirates)

print("\n" + 45 * "*")
for pirate in pirates:
    share = pirate.rank / sum_of_ranks * ducates
    print(f"{pirate.title} {pirate.name} gets {share:.2f} Ducates")

print(45 * "*" , end="\n")