
from pirates import Pirate
from pirates import Role
import json

class TestDataLoader:
    def load_pirates(self):
        return [
            Pirate("Zork", Role("Grand Nagus", 10)),
            Pirate("Wonka Tonka", Role("Snow Queen", 8)),
            Pirate("Spartacus", Role("Gladiator", 2))       
        ]
    

class JSONDataLoader:
    def load_pirates(self):
        with open("data.json") as file:
            data = json.load(file)
        
        pirates = [Pirate(pirate["name"], Role(pirate["title"], pirate["rank"])) for pirate in data["pirates"]]
        
        return pirates
