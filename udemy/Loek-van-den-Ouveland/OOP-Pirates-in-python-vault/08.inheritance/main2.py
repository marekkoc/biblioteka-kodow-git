"""
Udemy.com

Object Oriented (Programming) Pirates in Python.

Skcja 4. Inheritance

8. Inheritance

C: 2024.11.24
M: 2024.11.24

Zmiana: nazyw funkcji piratow:
    1. Gunner -> Cannon Operator
	2. Mate -> Officer
"""
class Pirate:
    def __init__(self, name, title, rank):
        self.name = name
        self.title = title
        self.rank = rank

pirates = [
    Pirate("Harry", "Capitan", 10),
    Pirate("Isabel", "Quartermaster", 9),
    Pirate("Bootstrap Bill", "Officer", 7),
    Pirate("Powder Joe", "Cannon Operator", 6),
    Pirate("Four Finger Fritz", "Officer", 7),
    Pirate("Lady Joice", "GuCannon Operatornner", 6)
]

ducates = 920
sum_of_ranks = sum(pirate.rank for pirate in pirates)

print("\n" + 45 * "*")
for pirate in pirates:
    share = pirate.rank / sum_of_ranks * ducates
    print(f"{pirate.title} {pirate.name} gets {share:.2f} Ducates")

print(45 * "*" , end="\n")