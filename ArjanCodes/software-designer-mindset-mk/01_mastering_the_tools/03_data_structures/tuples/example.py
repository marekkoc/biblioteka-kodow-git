from enum import StrEnum
from typing import Union

# Grouping several values
coordinates = (10.0, 20.5)
print(coordinates)


class Month(StrEnum):
    JANUARY = "January"
    FEBRUARY = "February"


def get_birthday() -> tuple[Month, int]:
    # Example function returning a tuple of month (StrEnum) and year (integer)
    return (Month.JANUARY, 1990)


result = get_birthday()
print(result)


hash = hash(result)  # Tuples are hashable

my_dict = {hash: result}
print(my_dict)

# Simple combination of a few variables
person_info = ("John Doe", 30, "Engineer")
print(person_info)

# Tuples typically contain objects of different types
person_details = (
    "Jane Doe",
    Month.FEBRUARY,
    1985,
    True,
)  # Name, birth month, birth year, resident
print(person_details)

# Access by index, order matters
name, age, profession = person_info
print(f"Name: {name}, Age: {age}, Profession: {profession}")

month, year = get_birthday()
print(f"Month: {month}, Year: {year}")


# Tuples are not ideal for ordered collections of the same type
numbers = (1, 2, 3)  # A list would be more suitable for this purpose


# Define a command as a tuple with various possible types
Command = Union[tuple[str, int], tuple[str, int, int], tuple[str]]


def handle_command(command: Command):
    match command:
        case ("add", x, y):
            print(f"Adding {x} and {y}: {x + y}")
        case ("increment", x):
            print(f"Incrementing {x}: {x + 1}")
        case ("reset",):
            print("Resetting to zero")
        case _:
            print("Unknown command")


def main() -> None:
    handle_command(("add", 1, 2))  # Output: Adding 1 and 2: 3
    handle_command(("increment", 10))  # Output: Incrementing 10: 11
    handle_command(("reset",))  # Output: Resetting to zero
    handle_command(("unknown", 123))  # Output: Unknown command


if __name__ == "__main__":
    main()
