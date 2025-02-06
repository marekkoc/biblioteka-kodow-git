class LootItem:
    def __init__(self, amount, currency_key):
        self.amount = amount
        self.currency_key = currency_key

class Mission:
    def __init__(self, name, crew, loot):
        self.name = name
        self.crew = crew
        self.loot = loot

    # dunder string that returns Mission info
    def __str__(self):
        return f"=== Mission: {self.name}. Crew of {len(self.crew)} captured {len(self.loot)} loot items. ==="