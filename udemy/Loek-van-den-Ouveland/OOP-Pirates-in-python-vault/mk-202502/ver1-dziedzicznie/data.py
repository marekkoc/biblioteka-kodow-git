import json

from pirates import (
    Capitan,
    QuarterMaster,
    Officer,
    CannonOperator,
    Cook,
    DeckScrubber
)

class DataLoader:
    def load_pirates(self) -> list[Capitan | QuarterMaster | Officer | CannonOperator]:
        return  [
                Capitan("Harry"),
                QuarterMaster("Isabel"),
                Officer("Bootstrap Bill"),
                CannonOperator("Powder Joe"),
                Officer("Four Finger Fritz"),
                CannonOperator("Lady Joyce"),
                Officer("Calypso"),
                CannonOperator("Moustache Mike")
                ]
    
class JSONDataLoader:
    def load_pirates(self) -> list[Capitan | QuarterMaster | Officer | CannonOperator]:
        with open("data.json", "r") as file:
            data = json.load(file)
            
        pirtes = []
        for pirate in data["pirates"]:
            if pirate["title"] == "Capitan":
                pirtes.append(Capitan(pirate["name"]))
            elif pirate["title"] == "Quartermaster":
                pirtes.append(QuarterMaster(pirate["name"]))
            elif pirate["title"] == "Officer":
                pirtes.append(Officer(pirate["name"]))
            elif pirate["title"] == "Cannon Operator":
                pirtes.append(CannonOperator(pirate["name"]))
            elif pirate["title"] == "Cook":
                pirtes.append(Cook(pirate["name"]))
            elif pirate["title"] == "Deck Scrubber":
                pirtes.append(DeckScrubber(pirate["name"]))
        return pirtes