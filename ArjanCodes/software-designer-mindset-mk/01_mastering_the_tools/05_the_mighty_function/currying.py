from typing import Callable


def apply_tax_and_discount(
    tax_rate: float,
) -> Callable[[float], Callable[[float], float]]:
    def apply_discount(discount: float) -> Callable[[float], float]:
        def calculate_total(price: float) -> float:
            taxed_price = price + (price * tax_rate)
            discounted_price = taxed_price - (taxed_price * discount)
            return discounted_price

        return calculate_total

    return apply_discount


def main() -> None:
    # Specify the tax rate and discount through currying
    tax_rate: float = 0.05  # 5% tax
    discount: float = 0.10  # 10% discount

    # Create a curried function for these specific rates
    calculate_with_specific_rates: Callable[[float], float] = apply_tax_and_discount(
        tax_rate
    )(discount)

    # Now, apply this curried function to different prices
    price1: float = 100  # Original price of the first item
    price2: float = 200  # Original price of the second item

    total1: float = calculate_with_specific_rates(price1)
    total2: float = calculate_with_specific_rates(price2)

    print(f"Total cost after tax and discount for price {price1}: ${total1:.2f}")
    print(f"Total cost after tax and discount for price {price2}: ${total2:.2f}")


if __name__ == "__main__":
    main()
