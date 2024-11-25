"""
Udemy.com

Object Oriented (Programming) Pirates in Python.

Skcja 4. Inheritance

8. Inheritance

C: 2024.11.24
M: 2024.11.24

Zmiana: Dziedziczenie
"""
class Pirate:
    def __init__(self, name):
        self.name = name
        
class Capitan(Pirate):
    # class variables are hard coded
    title = "Capitan"
    rank = 10      

class Quartermaster(Pirate):
    title = "Quartermaster"
    rank = 9

class Officer(Pirate):
    title = "Officer"
    rank = 7

class CannonOperator(Pirate):
    title = "Cannon Operator"
    rank = 6

  



pirates = [
    Capitan("Harry"),
    Quartermaster("Isabel"),
    Officer("Bootstrap Bill"),
    CannonOperator("Powder Joe"),
    Officer("Four Finger Fritz"),
    CannonOperator("Lady Joice")
]

ducates = 920
sum_of_ranks = sum(pirate.rank for pirate in pirates)

print("\n" + 45 * "*")
for pirate in pirates:
    share = pirate.rank / sum_of_ranks * ducates
    print(f"{pirate.title} {pirate.name} gets {share:.2f} Ducates")

print(45 * "*" , end="\n")