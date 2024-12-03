"""
Udemy.com

Object Oriented (Programming) Pirates in Python.

Moje testy. Powtorzenie całego kursu jeszcze raz.

Wczytywanie listy piratow z pliku, zamiast wpisywanie jej recznie do modulu data.

C: 2024.12.01
M: 2024.12.02

Zmiana:
"""
from typing import List

from data import DataLoader
from data import JSONDataLoader


#loader: DataLoader = DataLoader()
loader: JSONDataLoader = JSONDataLoader()

pirates: List = loader.load_pirates()


ducats: int= 1430
sum_of_ranks: int = sum(pirate.rank for pirate in pirates)

print()
for pirate in pirates:
    share: float = pirate.rank / sum_of_ranks * ducats
    print(f"{pirate.title} {pirate.name} gets {share:.2f} Ducats.")
