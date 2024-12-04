#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 22:25:11 2024

@author: marek
"""


class Currency:
    def __init__(self, name: str, exchange_rate: int):
        self.name: str = name
        self.exchange_rate: int = exchange_rate

    def value_in_ducates(self, amount: int) -> int:
        return amount * self.exchange_rate


class Bank:
    def __init__(self, loader):
        self.loader = loader

    def exchange(self, loot):
        currencies = self.loader.load_currencies()
        total_ducates = 0
        for loot_item in loot:
            currency = currencies[loot_item.currency_key]
            ducats = currency.value_in_ducates(loot_item.amount)
            total_ducates += ducats
        return total_ducates
