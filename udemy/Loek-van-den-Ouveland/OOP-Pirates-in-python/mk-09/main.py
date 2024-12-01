"""
Udemy.com

Object Oriented (Programming) Pirates in Python.

Moje testy. Powtorzenie całego kursu jeszcze raz.

C: 2024.12.01
M: 2024.12.01

Zmiana:
"""
from typing import List

from data import DataLoader


loader: DataLoader = DataLoader()
pirates: List = loader.load_pirates()


ducats: int= 920
sum_of_ranks: int = sum(pirate.rank for pirate in pirates)

print()
for pirate in pirates:
    share: float = pirate.rank / sum_of_ranks * ducats
    print(f"{pirate.title} {pirate.name} gets {share:.2f} Ducats.")
