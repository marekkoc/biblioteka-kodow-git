pirates = ["Harry", "Isabel", "Bootstrap Bill", "Morgan", "Powder Joe"]

# the loot
ducates = 480
sum_of_ranks = 0

# print a pirat an its share
for pirate in pirates:
    if pirate == "Harry":
        sum_of_ranks += 5
    elif pirate == "Isabel" or pirate == "Bootstrap Bill" or pirate == "Morgan":
        sum_of_ranks += 3
    elif pirate == "Powder Joe":
        sum_of_ranks += 2

for pirate in pirates:
    share = 0
    if pirate == "Harry":
        share = 5 / sum_of_ranks * ducates
    elif pirate == "Isabel" or pirate == "Bootstrap Bill" or pirate == "Morgan":
        share = 3 / sum_of_ranks * ducates
    elif pirate == "Powder Joe":
        share = 2 / sum_of_ranks * ducates
    print(f"{pirate} gets {share} Ducates.")