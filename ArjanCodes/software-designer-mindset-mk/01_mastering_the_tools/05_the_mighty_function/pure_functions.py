import random


# This function is pure because it does not have any side effects and the result is predictable
def validate_input(*args: int) -> bool:
    """Helper function to validate input values are positive."""
    return any(x <= 0 for x in args)


# This function is pure because it does not have any side effects and the result is predictable
def divide(numerator: int, denomerator: int) -> float:
    """Pure function to add two numbers."""
    if validate_input(denomerator):
        raise ValueError("Denomerator must be positive")
    return numerator / denomerator


# This function is not pure because it the result is not predictable
def random_number() -> int:
    """Not a pure function to generate random number."""
    return random.randint(1, 10)


def main() -> None:
    divide(1, 2)


if __name__ == "__main__":
    main()
