import json
from pirates import (
    Pirate,
    Role,
)
from mission import Mission


class TestDataLoader:
    def load_pirates(self) -> list[Pirate]:
        return  [
                Pirate("Zork", Role("Grand Nagus", 10)),
                Pirate("Wonka Tonka", Role("Snow Queen", 8)),
                Pirate("Spartacus", Role("Gladiator", 2))
                ]
    def load_missions(self) -> list[Mission]:
        pirates = self.load_pirates()
        return [
            Mission("Sea Battle 1", pirates[:2], 100),
            Mission("Sea Battle 2", pirates, 200)
            ]


class JSONDataLoader:
    def load_pirates(self):
        with open("data.json", "r") as file:
            data = json.load(file)
                
        pirates = [Pirate(pirate["name"], Role(pirate["title"], pirate["rank"])) for pirate in data["pirates"]]
        return pirates
    
    def load_missions(self):
        with open("data.json", "r") as file:
            data = json.load(file)
        pirates = self.load_pirates()
        
        missions = [Mission(m["name"], [p for p in pirates if p.name in m["crew"]], m["loot"]) for m in data["missions"]]
        return missions
