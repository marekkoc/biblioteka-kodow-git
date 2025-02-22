from mission import LootItem

class Currency:
    def __init__(self, name: str, exchange_rate: float):
        self.name = name
        self.exchange_rate = exchange_rate

    def value_in_ducats(self, amount: float) -> float:
        return amount * self.exchange_rate

    def __str__(self):
        return f"{self.name} ({self.exchange_rate})"


class Bank:
    def __init__(self, loader):
        self.loader = loader

    def exchange(self, loot: list[LootItem]) -> float:
        currencies = self.loader.load_currencies()
        total_ducats = 0
        for loot_item in loot:
            currency = currencies[loot_item.currency_key]
            total_ducats += currency.value_in_ducats(loot_item.amount)
        return total_ducats
