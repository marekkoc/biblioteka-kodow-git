from pirates import Capitan
from pirates import Quartermaster
from pirates import Officer
from pirates import CannonOperator
import json

class DataLoader:
    def load_pirates(self):
        return [
        Capitan("Harry"),
        Quartermaster("Isabel"),
        Officer("Bootstrap Bill"),
        CannonOperator("Powder Joe"),
        Officer("Four Finger Fritz"),
        CannonOperator("Lady Joice"),
        Officer("Calypso"),
        CannonOperator("Moustache Mike")
        ]
    

class JSONDataLoader:
    def load_pirates(self):
        with open("data.json") as file:
            data = json.load(file)
        pirates = []
        for pirate in data["pirates"]:
            if pirate["title"] == "Capitan":
                pirates.append(Capitan(pirate["name"]))
            elif pirate["title"] == "Quartermaster":
                pirates.append(Quartermaster(pirate["name"]))
            elif pirate["title"] == "Officer":
                pirates.append(Officer(pirate["name"]))
            elif pirate["title"] == "Cannon Operator":
                pirates.append(CannonOperator(pirate["name"]))
        return pirates
