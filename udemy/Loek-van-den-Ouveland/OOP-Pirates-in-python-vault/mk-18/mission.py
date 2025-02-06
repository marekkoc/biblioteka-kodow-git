#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 13:22:43 2024

@author: marek
"""
from typing import List
from pirates import Pirate

class LootItem:
    def __init__(self, amount: int, currency_key: str):
        self.amount: int = amount
        self.currency_key: str = currency_key

class Mission:
    def __init__(self, name: str, crew: List[Pirate], loot: List[LootItem]):
        self.name: str = name
        self.crew: List[Pirate] = crew
        self.loot: List[LootItem] = loot

    def __str__(self) -> str:
        return f"=== Mission: {self.name}. Crew of {len(self.crew)} captured {len(self.loot)} loot items.==="
