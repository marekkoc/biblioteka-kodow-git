from pirates import Pirate

class Mission:
    def __init__(self, name: str, crew: list[Pirate], loot: int):
        self.name = name
        self.crew = crew
        self.loot = loot

    def __str__(self):
        return f"=== Mission: {self.name}. Crew of {len(self.crew)} captured {self.loot} Ducats ==="
