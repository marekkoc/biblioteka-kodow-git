#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Data block. Prepare and load data from JSON file (if needed).

Created on Sun Dec  1 17:59:45 2024

@author: marek
"""
from typing import List
import json

from pirates import Pirate
from pirates import Role


class TestDataLoader:
    def load_pirates(self) -> List:
        return [
            Pirate("Zork", Role("Grand Nagus", 10)),
            Pirate("Wonka Tonka", Role("Snow Queen", 8)),
            Pirate("Spartacus", Role("Gladiator", 2)),
            ]

class JSONDataLoader:
    def load_pirates(self) -> List:
        with open("data.json") as file:
            data = json.load(file)
        pirates = [Pirate(pirate["name"], Role(pirate["title"], pirate["rank"])) for pirate in data["pirates"]]
        return pirates
