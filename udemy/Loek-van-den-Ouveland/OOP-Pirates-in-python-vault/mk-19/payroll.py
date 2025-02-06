#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 21:55:04 2024

@author: marek
"""
from typing import List

from pirates import Pirate


class Share:
    def __init__(self, pirate: Pirate, ducates: int):
        self.pirate: Pirate = pirate
        self.ducates: float = ducates

    def __str__(self) -> str:
        return f"{self.pirate.role.title} {self.pirate.name} rank {self.pirate.role.rank} gets share {self.ducates:.2f} Ducats."


class Payroll:
    def calculate_shares(self, crew: List[Pirate], total_ducates: int) -> List[Share]:
        sum_of_ranks = sum(pirate.role.rank for pirate in crew)
        return [Share(pirate, pirate.role.rank / sum_of_ranks * total_ducates) for pirate in crew]
