from abc import ABC, abstractmethod

class Role:
    def __init__(self, title: str, rank: int):
        self.title = title
        self.rank = rank

class Pirate:
    def __init__(self, name: str, role: Role):
        self.name = name
        self.role    = role


