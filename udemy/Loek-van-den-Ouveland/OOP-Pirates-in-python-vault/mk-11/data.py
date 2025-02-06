#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Data block. Prepare and load data from JSON file (if needed).

Created on Sun Dec  1 17:59:45 2024

@author: marek
"""
from typing import List
import json

from pirates import Capitan
from pirates import Quartermaster
from pirates import Officer
from pirates import CannonOperator


class DataLoader:
    def load_pirates(self) -> List:
        return [
                Capitan("Harry"),
                Quartermaster("Isabel"),
                Officer("Bootstrap Bill"),
                CannonOperator("Powder Joe"),
                Officer("Four Finger Fritz"),
                CannonOperator("Lady Joyce"),
                Officer("Calypso"),
                CannonOperator("Mustache Mike")
            ]

class JSONDataLoader:
    def load_pirates(self) -> List:
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
