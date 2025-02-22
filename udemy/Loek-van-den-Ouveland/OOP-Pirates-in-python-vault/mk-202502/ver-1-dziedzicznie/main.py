from data import ( DataLoader,
                   JSONDataLoader)

#data_loader = DataLoader()
data_loader = JSONDataLoader()

pirates = data_loader.load_pirates()

ducats = 1430

sum_of_ranks = sum([pirate.rank for pirate in pirates])

print()
for pirate in pirates:
    share: float = pirate.rank / sum_of_ranks * ducats
    print(f"{pirate.title}: {pirate.name} gets {share:.1f} Ducats.")
print()

