pirates = [
    ("Harry", 5),
    ("Isabel", 3)
]

ducats = 100
sum_of_ranks = sum(rank for name, rank in pirates)

for name, rank in pirates:
    share = rank / sum_of_ranks * ducats
    print(f"{name} gets {share} Ducates")