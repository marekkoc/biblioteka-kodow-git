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
    def __init__(self, name):
        self.name :str = name

class Capitan(Pirate):
    title: str = "Capitan"
    rank: int = 10

class Quartermaster(Pirate):
    title: str = "Quartermaster"
    rank: int = 9

class Mate(Pirate):
    title: str = "Mate"
    rank: int = 7

class Gunner(Pirate):
    title: str = "Gunner"
    rank: int = 6


pirates: List[Pirate] = [
    Capitan("Harry"),
    Quartermaster("Isabel"),
    Mate("Bootstrap Bill"),
    Gunner("Powder Joe"),
    Mate("Four Finger Fritz"),
    Gunner("Lady Joyce")
    ]

ducats: int= 920
sum_of_ranks: int = sum(pirate.rank for pirate in pirates)

print()
for pirate in pirates:
    share: float = pirate.rank / sum_of_ranks * ducats
    print(f"{pirate.title} {pirate.name} gets {share:.2f} Ducats.")
