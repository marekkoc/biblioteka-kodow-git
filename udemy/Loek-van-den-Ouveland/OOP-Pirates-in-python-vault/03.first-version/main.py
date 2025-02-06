pirates = ["Harry", "Isabel", "Bootstrap Bill", "Morgan", "Powder Joe"]

# the loot
ducates = 480

# share for each pirate, the same amount
share = ducates / len(pirates)

# print a pirat an its share
for pirate in pirates:
    print(f"{pirate} gets {share} Ducates.")