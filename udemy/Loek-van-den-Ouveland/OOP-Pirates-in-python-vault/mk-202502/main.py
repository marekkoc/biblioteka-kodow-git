from data import DataLoader

data_loader = DataLoader()
pirates = data_loader.load_pirates()

ducats = 920

sum_of_ranks = sum([pirate.rank for pirate in pirates])

print()
for pirate in pirates:
    share: float = pirate.rank / sum_of_ranks * ducats
    print(f"{pirate.title}: {pirate.name} gets {share:.1f} Ducats.")
print()
