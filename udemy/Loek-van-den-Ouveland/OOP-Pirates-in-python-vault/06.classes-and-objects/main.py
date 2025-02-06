
class Pirate:
    def __init__(self, name, title, rank):
        self.name = name
        self.title = title
        self.rank = rank

pirates = [
    Pirate("Harry", "Capitan", 10),
    Pirate("Isabel", "Quartermaster", 9),
    Pirate("Bootstrap Bill", "Mate", 7),
    Pirate("Powder Joe", "Gunner", 6),
    Pirate("Four Finger Fritz", "Mate", 7)
]

ducates = 850
sum_of_ranks = sum(pirate.rank for pirate in pirates)

print("\n" + 45 * "*")
for pirate in pirates:
    share = pirate.rank / sum_of_ranks * ducates
    print(f"{pirate.title} {pirate.name} gets {share:.2f} Ducates")

print(45 * "*" , end="\n")