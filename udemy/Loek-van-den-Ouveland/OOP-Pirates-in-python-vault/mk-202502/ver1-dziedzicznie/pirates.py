from abc import ABC, abstractmethod

class Pirate(ABC):
    def __init__(self, name: str):
        self.name = name
    

class Capitan(Pirate):
    title = "Captain"
    rank = 10
    

class QuarterMaster(Pirate):
    title = "Quarter Master"
    rank = 9
 

class Officer(Pirate):
    title = "Officer"
    rank = 7
 

class CannonOperator(Pirate):
    title = "Cannon Operator"
    rank = 6

class Cook(Pirate):
    title = "Cook"
    rank = 3

class DeckScrubber(Pirate):
    title = "Deck Scrubber"
    rank = 1 
  