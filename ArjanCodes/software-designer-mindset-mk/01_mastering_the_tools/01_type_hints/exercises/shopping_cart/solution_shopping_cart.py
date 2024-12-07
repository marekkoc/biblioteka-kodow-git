from typing import Callable


class ShoppingCart:
    def __init__(self, owner: str) -> None:
        """
        Initializes a shopping cart.

        Args:
            owner (str): The owner of the shopping cart.
        """
        self.owner = owner
        self.items: list[dict[str, int | float]] = []

    def add_item(self, id: int, quantity: int, price: float) -> None:
        """
        Adds an item to the shopping cart.

        Args:
            id (int): The name of the item.
            quantity (int): The quantity of the item.
            price (float): The price per unit of the item.
        """
        item = {"id": id, "quantity": quantity, "price": price}
        self.items.append(item)

    def calculate_total(self) -> float:
        """
        Calculates the total cost of items in the shopping cart.

        Returns:
            float: The total cost.
        """
        total_cost = sum(item["quantity"] * item["price"] for item in self.items)
        return total_cost

    def filter_items(
        self, filter_func: Callable[[dict[str, int | float]], bool]
    ) -> list[dict[str, int | float]]:
        """
        Filters the items in the shopping cart.

        Args:
            filter_func (function): The function used to filter the items.
        """

        filtered_items = [item for item in self.items if filter_func(item)]
        return filtered_items


def main() -> None:
    # Exercise usage
    # Creating an instance of ShoppingCart, adding items, and calculating the total cost

    alice_cart = ShoppingCart("Alice")

    alice_cart.add_item(1, 3, 1.50)
    alice_cart.add_item(2, 2, 0.75)
    alice_cart.add_item(3, 1, 15.99)

    total_cost_alice = alice_cart.calculate_total()
    print(total_cost_alice)


if __name__ == "__main__":
    main()
