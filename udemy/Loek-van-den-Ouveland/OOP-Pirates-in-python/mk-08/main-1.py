"""
Udemy.com

Object Oriented (Programming) Pirates in Python.

Moje testy. Powtorzenie całego kursu jeszcze raz.

C: 2024.12.01
M: 2024.12.01

Zmiana:
"""
from typing import List

class Pirate:
    def __init__(self, name, title, rank):
        self.name :str = name
        self.title :str = title
        self.rank :int = rank


pirates: List[Pirate] = [
    Pirate("Harry", "Capitan", 10),
    Pirate("Isabel", "Quartermaster", 9),
    Pirate("Bootstrap Bill", "Mate", 7),
    Pirate("Powder Joe", "Gunner", 6),
    Pirate("Four Finger Fritz", "Mate", 7),
    Pirate("Lady Joyce", "Gunner", 6)
    ]

ducats: int= 920
sum_of_ranks: int = sum(pirate.rank for pirate in pirates)

print()
for pirate in pirates:
    share: float = pirate.rank / sum_of_ranks * ducats
    print(f"{pirate.title} {pirate.name} gets {share:.2f} Ducats.")
