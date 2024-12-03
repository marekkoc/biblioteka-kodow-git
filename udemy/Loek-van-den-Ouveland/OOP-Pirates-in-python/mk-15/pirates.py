#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
All pirate classes definitions.

Created on Sun Dec  1 13:36:21 2024

@author: marek
"""
class Role:
    def __init__(self, title: str, rank: int):
        self.title: str = title
        self.rank: int = rank

class Pirate:
    def __init__(self, name: str, role: Role):
        self.name: str = name
        self.role: Role = role
