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
from mission import Mission


class TestDataLoader:
    def load_pirates(self) -> List[Pirate]:
        return [
            Pirate("Zork", Role("Grand Nagus", 10)),
            Pirate("Wonka Tonka", Role("Snow Queen", 8)),
            Pirate("Spartacus", Role("Gladiator", 2)),
            ]
    def load_missions(self) -> List[Mission]:
        pirates = self.load_pirates()
        return [
            Mission("Sea battle 1", pirates[:2], 100),
            Mission("Sea battle 2", pirates, 200)
            ]


class JSONDataLoader:
    def load_pirates(self) -> List[Pirate]:
        with open("data.json") as file:
            data = json.load(file)
        pirates = [Pirate(pirate["name"], Role(pirate["title"], pirate["rank"])) for pirate in data["pirates"]]
        return pirates

    def load_missions(self) -> List[Mission]:
        with open("data.json") as file:
            data = json.load(file)
        pirates = self.load_pirates()
        return [Mission(m["name"], [p for p in pirates if p.name in m["crew"] if p], m["loot"]) for m in data["missions"]]
