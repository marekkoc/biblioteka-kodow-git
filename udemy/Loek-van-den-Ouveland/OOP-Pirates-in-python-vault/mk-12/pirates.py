#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
All pirate classes definitions.

Created on Sun Dec  1 13:36:21 2024

@author: marek
"""
class Pirate:
    def __init__(self, name):
        self.name :str = name

class Capitan(Pirate):
    title: str = "Capitan"
    rank: int = 10

class Quartermaster(Pirate):
    title: str = "Quartermaster"
    rank: int = 9

class Officer(Pirate):
    title: str = "Officer"
    rank: int = 7

class CannonOperator(Pirate):
    title: str = "Cannon Operator"
    rank: int = 6

class Cook(Pirate):
    title: str = "Cook"
    rank: int = 3

class DeckScrubber(Pirate):
    title: str = "Deck Scrubber"
    rank: int = 1
