from typing import Callable


def apply_function_to_list(
    elements: list[int], func: Callable[[int], int]
) -> list[int]:
    return [func(element) for element in elements]


def square(x: int) -> int:
    return x * x


def increment(x: int) -> int:
    return x + 1


def main() -> None:
    numbers = [1, 2, 3, 4, 5]
    squared_numbers = apply_function_to_list(numbers, square)

    print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

    incremented_numbers = apply_function_to_list(numbers, increment)
    print(incremented_numbers)  # Output: [2, 3, 4, 5, 6]


if __name__ == "__main__":
    main()
