pirates = [
    ("Harry", 5),
    ("Isabel", 3),
    ("Bootstrap Bill", 2),
    ("Powder Joe", 2),
    ("Four Finger Fritz", 2)
]

ducats = 850
sum_of_ranks = sum(rank for name, rank in pirates)

for name, rank in pirates:
    share = rank / sum_of_ranks * ducats
    print(f"{name} gets {share:.2f} Ducates")