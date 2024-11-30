
from pirates import Pirate
from pirates import Role
from mission import Mission
from mission import LootItem
from exchange import Currency
import json

class TestDataLoader:
    def load_pirates(self):
        return [
            Pirate("Zork", Role("Grand Nagus", 10)),
            Pirate("Wonka Tonka", Role("Snow Queen", 8)),
            Pirate("Spartacus", Role("Gladiator", 2))       
        ]
    def load_missions(self):
        pirates = self.load_pirates()
        return [
            Mission("Sea Battle 1", pirates[:2], [LootItem(100, "DCT"), LootItem(10, "GCH")]),  # First two pirates
            Mission("Sea Battle 2", pirates, [LootItem(50, "DCT"), LootItem(20, "GCH")])       # All pirates
        ]
    
    def load_currencies(self):
        return {
            "DCT": Currency("Ducat", 1),
            "GCH": Currency("Gold Chain", 16)
        }
    

class JSONDataLoader:
    def load_pirates(self):
        with open("data.json") as file:
            data = json.load(file)
        
        pirates = [Pirate(pirate["name"], Role(pirate["title"], pirate["rank"])) for pirate in data["pirates"]]
        return pirates
    
    def load_missions(self):
        with open("data.json") as file:
            data = json.load(file)
        pirates = self.load_pirates()
        return [Mission(m['name'], [p for p in pirates if p.name in m["crew"]], [LootItem(l["amount"], l["currency_key"]) for l in m["loot"]]) for m in data["missions"]]

    def load_currencies(self):
        with open("currencies.json") as file:
            data = json.load(file)
        return {k:Currency(v["name"], v["exchange_rate"]) for (k,v) in data["currencies"].items()}