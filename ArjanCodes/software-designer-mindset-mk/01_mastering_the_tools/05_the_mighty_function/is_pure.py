from typing import Callable


def G(a: int, b: int) -> int:
    return a + b


def F(func: Callable[[int, int], int]) -> None:
    func(1, 2)


def main() -> None:
    F(G)


if __name__ == "__main__":
    main()
