import json

from pirates import (
    Pirate,
    Role,
)

class TestDataLoader:
    def load_pirates(self) -> list[Pirate]:
        return  [
                Pirate("Zork", Role("Grand Nagus", 10)),
                Pirate("Wonka Tonka", Role("Snow Queen", 8)),
                Pirate("Spartacus", Role("Gladiator", 2))
                ]
    
class JSONDataLoader:
    def load_pirates(self):
        with open("data.json", "r") as file:
            data = json.load(file)
                
        pirates = [Pirate(pirate["name"], Role(pirate["title"], pirate["rank"])) for pirate in data["pirates"]]
        return pirates