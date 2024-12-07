limit: int = 10
name: str = "Arjan"

ages: list[int] = [23, 43, 35]


def verify_password(submitted_password: str, stored_hash: str) -> bool:
    return True


class Car:
    def __init__(self, name: str, cost: int, brand: str):
        self.name = name
        self.cost = cost
        self.brand = brand
