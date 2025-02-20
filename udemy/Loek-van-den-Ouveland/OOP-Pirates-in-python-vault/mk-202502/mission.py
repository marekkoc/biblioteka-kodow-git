from pirates import Pirate

class LootItem:
    def __init__(self, amount: int, currency_key: str):  
        self.amount = amount
        self.currency_key = currency_key

    def __str__(self):
        return f"{self.amount} {self.currency_key}"


class Mission:
    def __init__(self, name: str, crew: list[Pirate], loot: int):
        self.name = name
        self.crew = crew
        self.loot = loot

    def __str__(self):
        return f"=== Mission: {self.name}. Crew of {len(self.crew)} captured {len(self.loot)} loot items. ==="
