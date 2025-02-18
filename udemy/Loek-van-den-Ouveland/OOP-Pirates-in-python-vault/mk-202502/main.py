from data import ( TestDataLoader,
                   JSONDataLoader)

#data_loader = TestDataLoader()
data_loader = JSONDataLoader()

pirates = data_loader.load_pirates()

ducats = 200

sum_of_ranks = sum([pirate.role.rank for pirate in pirates])

print()
for pirate in pirates:
    share: float = pirate.role.rank / sum_of_ranks * ducats
    print(f"{pirate.role.title}: {pirate.name} gets {share:.1f} Ducats.")
print()

