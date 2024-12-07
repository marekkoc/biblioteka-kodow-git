from typing import Callable

global_variable = 0


def G() -> None:
    global global_variable
    global_variable += 1


def F(func: Callable[[], None]) -> None:
    func()


def main() -> None:
    print(f"Initial global_variable: {global_variable}")

    F(G)

    print(f"Final global_variable: {global_variable}")


if __name__ == "__main__":
    main()
