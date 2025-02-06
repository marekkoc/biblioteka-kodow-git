"""
Udemy.com

Object Oriented (Programming) Pirates in Python.

Moje testy. Powtorzenie całego kursu jeszcze raz.


C: 2024.12.02
M: 2024.12.02

Zmiana:
"""
from typing import List

from data import TestDataLoader
from data import JSONDataLoader


#loader: TestDataLoader = TestDataLoader()
loader: JSONDataLoader = JSONDataLoader()

pirates: List = loader.load_pirates()


ducats: int= 100
sum_of_ranks: int = sum(pirate.role.rank for pirate in pirates)

print()
for pirate in pirates:
    share: float = pirate.role.rank / sum_of_ranks * ducats
    print(f"{pirate.role.title} {pirate.name} gets {share:.2f} Ducats.")
