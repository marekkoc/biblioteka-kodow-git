#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Data block. Prepare and load data from JSON file (if needed).

Created on Sun Dec  1 17:59:45 2024

@author: marek
"""
from typing import List

from pirates import Capitan
from pirates import Quartermaster
from pirates import Mate
from pirates import Gunner


class DataLoader:
    def load_pirates(self) -> List:
        return [
                Capitan("Harry"),
                Quartermaster("Isabel"),
                Mate("Bootstrap Bill"),
                Gunner("Powder Joe"),
                Mate("Four Finger Fritz"),
                Gunner("Lady Joyce")
            ]
